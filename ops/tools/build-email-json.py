#!/usr/bin/env python3
"""Build one POST /emails request (JSON) for a personalised-site offer.

usage: build-email-json.py <slug> "<Business name>" <to-email> <code> "<FAKT sentence>" [pl|en] > out.json
The FAKT sentence must come from the research pack (verified facts only). PL template = email 1
from outreach/email-1-template.md with the 2026-09-14 decision line (no contract, first month free).
"""
import html as H, json, sys

def btn(url, label):
    return ('<table role="presentation" cellspacing="0" cellpadding="0" style="margin:18px 0"><tr>'
            '<td style="background:#0f7a5a;border-radius:10px">'
            f'<a href="{H.escape(url)}" style="display:inline-block;padding:14px 30px;color:#fff;'
            f'font-weight:600;text-decoration:none;font-size:15px">{label}</a></td></tr></table>')

def p(t): return f"<p>{t}</p>"

def main():
    if len(sys.argv) < 6:
        sys.exit(__doc__)
    slug, name, to, code, fakt = sys.argv[1:6]
    lang = sys.argv[6] if len(sys.argv) > 6 else "pl"
    if lang == "pl":
        url = f"https://{slug}.givyx.com/?utm_source=email&utm_medium=oferta&utm_campaign={slug}&utm_content={code}"
        body = (p("Dzień dobry,")
            + p(f"Z tej strony Stan z Givyx, z Krakowa. Zanim napisałem, sprawdziłem Was: {fakt}.")
            + p("Zbudowaliśmy wersję Waszej strony — z Waszą nazwą, telefonem, usługami i oceną z Google:")
            + btn(url, "Zobacz stronę →")
            + p("Strona zaczyna się od wjazdu do hali i zjazdu pod maskę silnika, potem usługi na pierścieniu, "
                "rezerwacja wizyty i kontakt — wszystko działa na telefonie. Zobaczcie sami, to 30 sekund.")
            + p("Jeśli się podoba, uruchamiamy ją na Waszej domenie w 2 dni. Abonament:")
            + ("<p><strong>149 zł/mies.</strong> — ta strona, jak w podglądzie · <strong>249 zł/mies.</strong> — "
               "rozbudowana, nowoczesna, z rezerwacją online · <strong>750 zł/mies.</strong> — płatności online, "
               "bez brandingu Givyx.<br>Utrzymanie, zmiany i poprawki są w cenie — my dbamy o stronę, Wy o auta.<br>"
               "<strong>Bez umowy, rezygnacja w każdej chwili, pierwszy miesiąc gratis.</strong></p>")
            + p("Odpiszcie na tego maila albo zadzwońcie — chętnie dopasuję stronę pod Was.")
            + p("Pozdrawiam,<br>Stan"))
        req = {"to": [to], "subject": f"Strona dla {name} — podgląd", "layout": "givyx", "locationId": "l_givyx",
               "eyebrow": "Oferta", "title": f"Strona dla {name}", "badge": "", "replyTo": "info@givyx.com", "html": body}
    else:
        url = f"https://{slug}.givyx.com/?utm_source=email&utm_medium=offer&utm_campaign={slug}&utm_content={code}"
        body = (p("Hi,")
            + p(f"Stan here, from Givyx. Before writing I looked you up: {fakt}.")
            + p("We built a version of your site — your name, phone, services and reviews:")
            + btn(url, "See your site →")
            + p("It opens with a drive into the shop and a dive under the hood, then your services, online booking "
                "and contact — all on the phone. Takes 30 seconds to look.")
            + p("If you like it, it goes live on your own domain in 2 days. <strong>$60/month</strong>, maintenance and "
                "changes included — we keep the site current, you keep fixing cars. "
                "<strong>No contract, cancel any time, first month free.</strong>")
            + p("Reply to this email or call — happy to adjust anything.")
            + p("Stan")
            + '<p style="color:#6b7280;font-size:13px">This is an advertisement. Reply "unsubscribe" and you won\'t hear from me again.</p>')
        req = {"to": [to], "subject": f"A site for {name} — preview", "layout": "givyx", "locationId": "l_givyx",
               "eyebrow": "Offer", "title": f"A site for {name}", "badge": "", "replyTo": "info@givyx.com", "html": body}
    print(json.dumps(req, ensure_ascii=False))

if __name__ == "__main__":
    main()
