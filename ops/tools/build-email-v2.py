#!/usr/bin/env python3
"""Build one POST /emails request for a personalised-site offer, v2 (2026-09-15, Stan's brief):
249 zł/mies., site built free, first month free, benefits list, and three personal fields per prospect.

usage: build-email-v2.py spec.json > out.json
spec = {"slug","name","to","code","hook","fakt","na_stronie","dlaczego", "lang": "pl"|"en"}  (no Google-rating clause anywhere — Stan 2026-09-15)   (all facts from the research pack)
"""
import html as H, json, sys
from email_parts import p, ul, cta, signature, request, ADDRESS

# Look (pill, CTA, signature by language, text part, no shell contact block) = email_parts.py, v4.1 (21 Sep).

def main():
    s = json.load(open(sys.argv[1]))
    name = H.escape(s["name"]); slug = s["slug"]
    url = f"https://{slug}.givyx.com/?utm_source=email&utm_medium=oferta&utm_campaign={slug}&utm_content={s['code']}"
    body = (p("Dzień dobry,")
        + p(s["hook"])
        + cta(url, "Zobacz stronę&nbsp;→", f"{slug}.givyx.com · otwiera się na telefonie")
        + p(f"Z tej strony Stanisław z Givyx, z Krakowa. Zanim napisałem, sprawdziłem, jak pracujecie: {s['fakt']}. "
            f"Na stronie jest {s['na_stronie']}.")
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
        + p("<strong>Jak się skontaktować:</strong> zadzwońcie do mnie na <a href=\"tel:+48571088012\" style=\"color:#0f7a5a;font-weight:600\">571 088 012</a> "
            "albo po prostu odpiszcie na tego maila — odpowiem tego samego dnia. Jeśli coś ma wyglądać inaczej (usługi, ceny, zdjęcia), dopasuję.")
        + p("Pozdrawiam,")
        + s.get("append_html", "")   # optional extra block (e.g. a RU version) before the signature
        + signature("pl", s["code"]))
    if s.get("lang","pl") == "en":
        url = f"https://{slug}.givyx.com/?utm_source=email&utm_medium=offer&utm_campaign={slug}&utm_content={s['code']}"
        body = (p("Hi,")
            + p(s["hook"])
            + cta(url, "See your site&nbsp;→", f"{slug}.givyx.com · opens on your phone")
            + p(f"Stan here, from Givyx. Before writing I looked at how you work: {s['fakt']}. On the site: {s['na_stronie']}.")
            + p(s["dlaczego"])
            + p("<strong>The offer</strong>")
            + ul(["<strong>$49/month</strong> — no contract, cancel any time",
                  "<strong>Site built free</strong> and <strong>first month free</strong>",
                  "Live on your own domain in 2 days"])
            + p("<strong>Included</strong>")
            + ul(["maintenance, changes and fixes — you write, we do it",
                  "further development and new features at no extra cost",
                  "online booking and contact form — every request straight to your email",
                  "emails to your customers (confirmations, reminders) at no extra cost",
                  "option to add SMS to customers",
                  "works on the phone; we keep the site current, you keep fixing cars"])
            + p("<strong>How to reach me:</strong> just reply to this email, or call / WhatsApp "
                "<a href=\"tel:+48571088012\" style=\"color:#0f7a5a;font-weight:600\">+48 571 088 012</a> — I answer the same day. "
                "If anything should look different (services, prices, photos), I'll adjust it.")
            + p("Best,")
            + signature("en", s["code"])
            # CAN-SPAM: the postal address must be in words (the signature only has a map icon now).
            + f'<p style="color:#6b7280;font-size:13px;margin-top:16px">This is an advertisement. Givyx, {ADDRESS}, Poland. '
              'Reply "unsubscribe" and you won\'t hear from me again.</p>')
        print(json.dumps(request(s["to"], f"A site for {s['name']} — preview and offer", f"A site for {s['name']}", body, "en"), ensure_ascii=False)); return
    print(json.dumps(request(s["to"], f"Strona dla {s['name']} — podgląd i oferta", f"Strona dla {s['name']}", body, "pl"), ensure_ascii=False))

if __name__ == "__main__":
    main()
