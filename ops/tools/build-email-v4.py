#!/usr/bin/env python3
"""Build one POST /emails request for the GENERIC offer, v4 (2026-09-21, Stan's OK):
no per-prospect site, one demo link per niche, the personalised version is offered on reply.
Look (pill, CTA, signature by language, text part) comes from email_parts.py — v4.1, Stan's OK 21 Sep.

usage: build-email-v4.py niche.json prospect.json > out.json
niche    = {"campaign","demo_url","subject","intro","link_hint","closing","title_prefix","lang"?,
            "version_with"?,"booking_line"?}   (outreach/niches/<niche>.json; the two optional keys
            override the workshop wording "usługami" / "rezerwacja online i formularz kontaktowy")
prospect = {"name","to","code"}
"""
import html as H, json, re, sys
from email_parts import p, ul, cta, signature, request, tagged, PHONE, PHONE_TEL, ACCENT

def main():
    n = json.load(open(sys.argv[1])); s = json.load(open(sys.argv[2]))
    lang = n.get("lang", "pl")
    name = H.escape(s["name"])
    # utm_campaign = the prospect code, not the niche: analytics drops utm_content, and one generic demo
    # serves every prospect, so the code is the only thing that says who clicked.
    url = tagged(n["demo_url"], "oferta", s["code"])
    bare = re.sub(r"^https?://|/$", "", n["demo_url"])
    body = (p("Dzień dobry,")
        + p(n["intro"])
        + cta(url, "Zobacz przykładową stronę&nbsp;→", f"{bare} · otwiera się na telefonie")
        + p(n["link_hint"])
        + p(f"Wersję dla {name} — z Waszą nazwą, {n.get('version_with', 'usługami')}, zdjęciami i numerem — przygotujemy do obejrzenia zanim cokolwiek zapłacicie. "
            "Wystarczy odpisać „tak” albo nazwę firmy.")
        + p("<strong>Oferta</strong>")
        + ul(["<strong>249 zł/mies.</strong> — bez umowy, rezygnacja w każdej chwili",
              "<strong>Budowa strony gratis</strong> i <strong>pierwszy miesiąc gratis</strong>",
              "Uruchomienie na Waszej domenie w 2 dni"])
        + p("<strong>W cenie</strong>")
        + ul(["utrzymanie, zmiany i poprawki — piszecie, my robimy",
              "rozwój strony i nowe funkcje bez dopłat",
              n.get("booking_line", "rezerwacja online i formularz kontaktowy") + " — każde zgłoszenie od razu na Wasz e-mail",
              "e-maile do Waszych klientów (potwierdzenia, przypomnienia) — bez dopłat",
              "możliwość dodania SMS-ów do klientów",
              n["closing"]])
        + p(f"<strong>Jak się skontaktować:</strong> zadzwońcie do mnie na <a href=\"tel:{PHONE_TEL}\" style=\"color:{ACCENT};font-weight:600\">{PHONE}</a> "
            "albo po prostu odpiszcie na tego maila — odpowiem tego samego dnia.")
        + p("Pozdrawiam,")
        + signature(lang, s["code"]))
    print(json.dumps(request(s["to"], n["subject"], f"{n['title_prefix']} {name}", body, lang), ensure_ascii=False))

if __name__ == "__main__":
    main()
