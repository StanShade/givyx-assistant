#!/usr/bin/env python3
"""Build one POST /emails request for a personalised-site offer, v2 (2026-09-15, Stan's brief):
249 zł/mies., site built free, first month free, benefits list, and three personal fields per prospect.

usage: build-email-v2.py spec.json > out.json
spec = {"slug","name","to","code","fakt","na_stronie","dlaczego"}   (all facts from the research pack)
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
    s = json.load(open(sys.argv[1]))
    name = H.escape(s["name"]); slug = s["slug"]
    url = f"https://{slug}.givyx.com/?utm_source=email&utm_medium=oferta&utm_campaign={slug}&utm_content={s['code']}"
    body = (p("Dzień dobry,")
        + p(f"Z tej strony Stan z Givyx, z Krakowa. Zanim napisałem, sprawdziłem, jak pracujecie: {s['fakt']}.")
        + p(f"Przygotowaliśmy wersję strony dla {name}: {s['na_stronie']}.")
        + btn(url, "Zobacz stronę →")
        + p(s["dlaczego"])
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
              "strona działa na telefonie; my dbamy o stronę, Wy o auta"])
        + p("Jeśli coś ma wyglądać inaczej — usługi, ceny, zdjęcia — odpiszcie, dopasuję. Albo zadzwońcie.")
        + p("Pozdrawiam,<br>Stan<br>Givyx"))
    req = {"to": [s["to"]], "subject": f"Strona dla {s['name']} — podgląd i oferta", "layout": "givyx",
           "locationId": "l_givyx", "eyebrow": "Oferta", "title": f"Strona dla {s['name']}", "badge": "",
           "replyTo": "info@givyx.com", "html": body}
    print(json.dumps(req, ensure_ascii=False))

if __name__ == "__main__":
    main()
