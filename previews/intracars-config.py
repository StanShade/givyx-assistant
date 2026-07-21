"""Intra Cars preview — personalized clone of AutoSerwis Kowalski config.

Drop-in replacement for givyx.claudeBrain/Givyx/demos/autoserwis/config.py when
building the intracars.givyx.com preview. Values marked  # ⚠️CONFIRM  are best-guess
from public directory data and should be verified with the owner before go-live
(the preview SMS already frames this as an adjustable draft).

VERIFIED 2026-07-18: 523 Google reviews, 4.1★, open 7 DAYS 8:00-23:00, al. 29 Listopada 153, 31-406,
email intracars2000@gmail.com. NOTE: they already have TWO microsites (intra-cars.localo.site +
intra-cars.dobrywarsztat.info, the latter WITH online booking) — do NOT pitch "you have no website".
autoserwis + wulkanizacja, phones 12 311 02 01 / 509 541 377.
"""

# ---- identity / NAP ----
NAME = "Intra Cars"
NAME_UPPER = "INTRA CARS"
DISTRICT = "Kraków Prądnik Czerwony"
CITY = "Kraków"
STREET = "al. 29 Listopada 153"
POSTAL = "31-406"                 # ⚠️CONFIRM postal for this address
REGION = "małopolskie"
PHONE_DISPLAY = "12 311 02 01"
PHONE_FULL = "+48 12 311 02 01"
PHONE_TEL = "tel:+48123110201"
EMAIL = "intracars2000@gmail.com"  # VERIFIED public (2026-07-18)
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Intra+Cars+al.+29+Listopada+153+Krak%C3%B3w"

HOURS = [                          # VERIFIED: open 7 days a week 8:00-23:00
    ("Poniedziałek – Niedziela", "8:00 – 23:00"),
]
OPEN_LINE = "Otwarte codziennie do 23:00"

# ---- trust strip (VERIFIED public facts, 2026-07-18) ----
TRUST = [
    ("523", "opinii w Google"),
    ("4,1 ★", "średnia ocena"),
    ("7 dni", "otwarte codziennie do 23:00"),
]

# ---- services (⚠️CONFIRM prices with owner — 'od' values are illustrative) ----
SERVICES = [
    ("Wulkanizacja i opony", "od 40 zł / koło",
     "Wymiana, wyważanie, przechowalnia.",
     "Sezonowa wymiana opon z wyważaniem, naprawa przebitych opon, wymiana zaworków i czujników TPMS. Prowadzimy też przechowalnię kół — nie musisz targać opon do piwnicy."),
    ("Wymiana oleju i filtrów", "od 150 zł",
     "Olej + filtr w 30 minut, na poczekaniu.",
     "Wymiana oleju silnikowego i kompletu filtrów (olejowy, powietrza, kabinowy, paliwa). Używamy olejów zgodnych ze specyfikacją producenta. Zwykle na poczekaniu."),
    ("Serwis klimatyzacji", "od 200 zł",
     "Nabicie, odgrzybianie, test szczelności.",
     "Pełny serwis klimatyzacji: kontrola i uzupełnienie czynnika, test szczelności układu, odgrzybianie, wymiana filtra kabinowego."),
    ("Diagnostyka komputerowa", "od 100 zł",
     "Odczyt błędów i jasna wycena naprawy.",
     "Profesjonalny odczyt i analiza błędów sterowników (silnik, ABS, airbag, DPF). Mówimy dokładnie co się dzieje i ile będzie kosztować naprawa."),
    ("Układ hamulcowy", "od 250 zł",
     "Tarcze, klocki, płyn — od ręki.",
     "Wymiana tarcz i klocków, przewodów oraz płynu hamulcowego, naprawa zacisków. Sprawdzimy cały układ i powiemy uczciwie, co wymaga wymiany."),
    ("Mechanika ogólna", "wycena od ręki",
     "Naprawy bieżące i sezonowe przeglądy.",
     "Naprawy bieżące, przeglądy sezonowe, wymiana zawieszenia, rozrządu i osprzętu. Jasna wycena przed rozpoczęciem pracy."),
]
SERVICES_NOTE = "Nie widzisz swojej usterki? Zadzwoń — powiemy od razu, czy pomożemy i ile to kosztuje."

# ---- reviews (⚠️REPLACE with the shop's real Google reviews before go-live) ----
REVIEWS = [
    ("Szybko, konkretnie i uczciwa cena. Przyjechałem po godzinach — inni już zamknięci, a tu zrobili opony od ręki.", "Marek T.", "★★★★★"),
    ("Serwis klimatyzacji zrobiony porządnie, bez wciskania dodatkowych usług. Cena taka jak podali przez telefon.", "Agnieszka W.", "★★★★★"),
    ("Otwarte do 23:00 to ratunek dla pracujących. Wymiana opon w 20 minut, polecam.", "Piotr K.", "★★★★★"),
    ("Dobra diagnostyka, sympatyczna obsługa. Jedyny minus to spory ruch — warto się umówić.", "Tomasz S.", "★★★★☆"),
]
REVIEWS_BADGE = "Opinie z Google"

# ---- callback form ----
FORM_SLUG = "oddzwonimy"
FORM_NAME = "Oddzwonimy — callback"
FORM_HEADLINE = "Zostaw numer — oddzwonimy do 15 min"
FORM_SUB = "w godzinach pracy"
FORM_SUCCESS = "Dziękujemy! Oddzwonimy do 15 minut w godzinach pracy."
FORM_SUBMIT = "Zamów rozmowę"
FORM_FOOTER = "Wysyłając numer zgadzasz się na kontakt telefoniczny w sprawie Twojego zapytania."

# ---- photos, theme, SEO: keep from autoserwis config.py (same look) ----
# Only override SEO strings:
SEO_TITLE = "Warsztat i wulkanizacja Kraków — Intra Cars (Prądnik Czerwony)"
SEO_DESC = ("Autoserwis i wulkanizacja w Krakowie na al. 29 Listopada. Opony od 40 zł/koło, "
            "wymiana oleju od 150 zł, diagnostyka od 100 zł. Otwarte do 23:00. "
            "Zadzwoń: +48 12 311 02 01.")
SEO_LANG = "pl"
SEO_NOINDEX = True   # flip to False at go-live (after owner confirms details)
PRICE_RANGE = "40–1500 zł"
