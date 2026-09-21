#!/usr/bin/env python3
"""Build one POST /emails request for the GENERIC offer, v4 (2026-09-21, Stan's OK):
no per-prospect site, one demo link per niche, the personalised version is offered on reply.

usage: build-email-v4.py niche.json prospect.json > out.json
niche    = {"demo_url","subject","intro","link_hint","closing","title_prefix"}   (outreach/niches/<niche>.json)
prospect = {"name","to","code"}
"""
import html as H, json, sys

def btn(url, label):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" style="margin:18px 0"><tr>'
            '<td style="background:#0f7a5a;border-radius:10px">'
            f'<a href="{H.escape(url)}" style="display:inline-block;padding:14px 30px;color:#fff;'
            f'font-weight:600;text-decoration:none;font-size:15px">{label}</a></td></tr></table>')

def p(t): return f"<p>{t}</p>"
def ul(items): return '<ul style="margin:6px 0 14px;padding-left:20px">' + "".join(f"<li style='margin:3px 0'>{i}</li>" for i in items) + "</ul>"

def main():
    n = json.load(open(sys.argv[1])); s = json.load(open(sys.argv[2]))
    name = H.escape(s["name"])
    url = f"{n['demo_url']}?utm_source=email&utm_medium=oferta&utm_campaign={n['campaign']}&utm_content={s['code']}"
    body = (p("Dzień dobry,")
        + p(n["intro"])
        + btn(url, "Zobacz przykładową stronę →")
        + p(n["link_hint"])
        + p(f"Wersję dla {name} — z Waszą nazwą, usługami, zdjęciami i numerem — przygotujemy do obejrzenia zanim cokolwiek zapłacicie. "
            "Wystarczy odpisać „tak” albo nazwę firmy.")
        + p("<strong>Oferta</strong>")
        + ul(["<strong>249 zł/mies.</strong> — bez umowy, rezygnacja w każdej chwili",
              "<strong>Budowa strony gratis</strong> i <strong>pierwszy miesiąc gratis</strong>",
              "Uruchomienie na Waszej domenie w 2 dni"])
        + p("<strong>W cenie</strong>")
        + ul(["utrzymanie, zmiany i poprawki — piszecie, my robimy",
              "rozwój strony i nowe funkcje bez dopłat",
              "rezerwacja online i formularz kontaktowy — każde zgłoszenie od razu na Wasz e-mail",
              "e-maile do Waszych klientów (potwierdzenia, przypomnienia) — bez dopłat",
              "możliwość dodania SMS-ów do klientów",
              n["closing"]])
        + p("<strong>Jak się skontaktować:</strong> zadzwońcie do mnie na <a href=\"tel:+48571088012\" style=\"color:#0f7a5a;font-weight:600\">571 088 012</a> "
            "albo po prostu odpiszcie na tego maila — odpowiem tego samego dnia.")
        + p("Pozdrawiam,<br>Stanisław<br>Givyx · 571 088 012 · info@givyx.com"))
    req = {"to": [s["to"]], "subject": n["subject"], "layout": "givyx", "locationId": "l_givyx",
           "eyebrow": "Oferta", "title": f"{n['title_prefix']} {name}", "badge": "",
           "replyTo": "info@givyx.com", "html": body}
    print(json.dumps(req, ensure_ascii=False))

if __name__ == "__main__":
    main()
