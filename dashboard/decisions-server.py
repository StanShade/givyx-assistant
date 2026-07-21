#!/usr/bin/env python3
"""Tiny local server for the Givyx decisions sheet.

Why this exists: a page opened as file:// cannot write to disk, and browser
localStorage is per-browser — Stan's answers never reached the instance Claude
could read. This serves the page over http://127.0.0.1 so the browser can POST
answers, and the server writes them to answers.json right next to this file.

Run:  python3 decisions-server.py        (binds 127.0.0.1 only — not exposed)
Then: open http://127.0.0.1:8848
"""
import json, os, http.server, socketserver
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DECISIONS = os.path.join(HERE, "decisions.json")
ANSWERS = os.path.join(HERE, "answers.json")
PAGE = os.path.join(HERE, "decisions.html")
PORT = 8848


def read_json(path, fallback):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return fallback


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.startswith("/api/decisions"):
            return self._send(200, json.dumps(read_json(DECISIONS, {"items": []})))
        if self.path.startswith("/api/answers"):
            return self._send(200, json.dumps(read_json(ANSWERS, {"answers": {}})))
        if self.path in ("/", "/index.html", "/decisions.html"):
            try:
                with open(PAGE, "rb") as f:
                    return self._send(200, f.read(), "text/html; charset=utf-8")
            except FileNotFoundError:
                return self._send(404, "decisions.html not found", "text/plain")
        return self._send(404, "not found", "text/plain")

    def do_POST(self):
        if not self.path.startswith("/api/answers"):
            return self._send(404, "not found", "text/plain")
        length = int(self.headers.get("Content-Length") or 0)
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self._send(400, json.dumps({"ok": False, "error": "bad json"}))

        # Write a self-documenting file: each answer carries its question text,
        # so Claude can read it without cross-referencing decisions.json.
        items = {i["id"]: i for i in read_json(DECISIONS, {"items": []}).get("items", [])}
        answers = payload.get("answers", {})
        out = {
            "savedAt": datetime.now().isoformat(timespec="seconds"),
            "answers": {
                k: {
                    "question": items.get(k, {}).get("q", k),
                    "answer": ("USE YOUR RECOMMENDATION" if v.get("mode") == "you" else v.get("text", "")),
                    "mode": v.get("mode"),
                }
                for k, v in answers.items()
                if v.get("mode") or v.get("text")
            },
        }
        with open(ANSWERS, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        return self._send(200, json.dumps({"ok": True, "count": len(out["answers"])}))

    def log_message(self, *args):
        pass  # quiet


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Givyx decisions → http://127.0.0.1:{PORT}   (answers → {ANSWERS})")
        httpd.serve_forever()
