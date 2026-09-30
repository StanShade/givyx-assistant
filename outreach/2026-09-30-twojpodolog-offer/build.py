#!/usr/bin/env python3
"""Offer e-mail to Bartek Nowak (Twój Podolog, Martyna Bassara-Nowak) after Stan's call, 30.09.2026.
Look = ops/tools/email_parts.py (v4.1). Writes request.json (to Bartek) and request-review.json (Stan's copy).

Facts: site content from givyx.claudeBrain/twojpodolog (research + build); plan contents and prices from
givyx.com/pricing?lang=pl (30.09); SEO lines from web searches and the Booksy page fetched 30.09.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "ops", "tools"))
from email_parts import p, ul, cta, signature, request, tagged, ACCENT

CODE = "twojpodolog"
TO = "nowak.bartek1996@gmail.com"
REVIEW_TO = "stan.zak.inf@gmail.com"
SITE = tagged("https://twojpodolog.givyx.com/", "oferta", CODE)
PRICING = tagged("https://givyx.com/pricing?lang=pl", "oferta", CODE)
TEL = f'<a href="tel:+48571088012" style="color:{ACCENT};font-weight:600">571 088 012</a>'

body = (
    p("Dzień dobry Panie Bartku,")
    + p("dziękuję za rozmowę. Tak jak mówiłem, strona dla gabinetu jest gotowa i dostajecie ją <strong>za darmo</strong>.")
    + cta(SITE, "Zobacz stronę gabinetu&nbsp;→", "twojpodolog.givyx.com · otwiera się na telefonie")
    + p("Wszystko na niej pochodzi z Waszej iPodologii i Instagrama: 28 zabiegów z cenami, Pani Martyna i Pani Monika, "
        "zasady wizyt i dojazd na Kujawską 3. Każdy przycisk „Umów wizytę” prowadzi prosto do iPodologii, "
        "więc w zapisach nic się nie zmienia.")
    + p("<strong>Za darmo</strong> dostajecie wszystko z planu Starter (normalnie 149 zł/mies.): stronę na subdomenie Givyx, "
        "podpięcie własnej domeny bez opłat, aktualizacje treści i podstawowe SEO. "
        f'Cennik wszystkich planów: <a href="{PRICING}" style="color:{ACCENT}">givyx.com/pricing</a>')
    + p("<strong>Propozycja: Studio w cenie Startera</strong>")
    + p("Plan Studio (normalnie 249 zł/mies.) za <strong>149 zł/mies.</strong> W nim:")
    + ul(["<strong>nowy, w pełni autorski design</strong>: nowoczesna, dopracowana strona, która wyróżni gabinet i przyciągnie więcej pacjentów",
          "<strong>zaawansowane SEO</strong>: podstrony pod zabiegi, których szukają pacjenci",
          "zmiany bez limitu i wsparcie priorytetowe",
          "panel analityczny: ile osób wchodzi na stronę i skąd"])
    + p("Zrobiłem też wstępną analizę SEO. Z zaawansowanym SEO w Studio możecie być na pierwszym miejscu "
        "w wyszukiwarkach, np. na hasło „podolog Rzeszów”, i oczywiście w odpowiedziach czatów AI, takich jak ChatGPT.")
    + p("<strong>Co dalej</strong>")
    + ul(["<strong>Strona za darmo:</strong> proszę ją obejrzeć i przetestować. Jeśli się podoba, chętnie coś zmienię "
          "na Wasze życzenie i podpowiem, jak ją aktywować i jakie są dalsze kroki.",
          "<strong>Studio:</strong> uruchomimy obecną wersję strony, żeby SEO zaczęło działać, a ja zacznę budowę nowej, "
          "zaawansowanej strony. Dopiero kiedy skończę i będziecie zadowoleni, rusza pierwszy miesiąc gratis, "
          "a potem 149 zł/mies. Bez umowy, rezygnacja w każdej chwili."])
    + p(f"<strong>Kontakt:</strong> proszę dzwonić na {TEL} albo po prostu odpisać na tego maila.")
    + p("Pozdrawiam,")
    + signature("pl", CODE)
)

SUBJECT = "Twój Podolog: strona gotowa za darmo + propozycja Studio"
TITLE = "Strona dla gabinetu Twój Podolog jest gotowa"
req = request(TO, SUBJECT, TITLE, body, "pl")
review = request(REVIEW_TO, "[DO AKCEPTACJI] " + SUBJECT, TITLE, body, "pl")

text = req["text"]
assert "Google" not in text and "opinii" not in text, "no Google/ratings in offer mails (Stan, 09-15)"
assert "—" not in text, "no em dashes"
for f, r in (("request.json", req), ("request-review.json", review)):
    with open(os.path.join(HERE, f), "w", encoding="utf-8") as fh:
        json.dump(r, fh, ensure_ascii=False, indent=1)
print(text)
