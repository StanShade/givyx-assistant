"""Intra Cars preview — personalized clone of AutoSerwis Kowalski config.

Drop-in replacement for givyx.claudeBrain/Givyx/demos/autoserwis/config.py when
building the intracars.givyx.com preview. Values marked  # ⚠️CONFIRM  are best-guess
from public directory data and should be verified with the owner before go-live
(the preview SMS already frames this as an adjustable draft).

Real public facts used: 424+ Google reviews, 4.1★, open to 23:00, al. 29 Listopada 153,
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
EMAIL = "intracars2000@gmail.com"   # VERIFIED public — cylex/directory listings + search, 2026-07-23
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Intra+Cars+al.+29+Listopada+153+Krak%C3%B3w"

HOURS = [                          # VERIFIED 7 days: DobryMechanik + Localo + search all agree
    ("Poniedziałek – Niedziela", "8:00 – 23:00"),
]
OPEN_LINE = "Otwarte codziennie do 23:00"   # day-agnostic — a static site must never say "dziś"

# ---- trust strip (real public differentiators) ----
TRUST = [
    ("424+", "opinii w Google"),
    ("4,1 ★", "średnia ocena"),
    ("do 23:00", "otwarte także wieczorem"),
]

# ---- services ----
# No prices: Intra Cars publishes none we can verify, so every column is "wycena od ręki"
# (the standing rule — never print a price the owner didn't set). Prior "od X zł" values were
# illustrative guesses and were removed 2026-07-23 before the offer email.
SERVICES = [
    ("Wulkanizacja i opony", "wycena od ręki",
     "Wymiana, wyważanie, przechowalnia.",
     "Sezonowa wymiana opon z wyważaniem, naprawa przebitych opon, wymiana zaworków i czujników TPMS. Prowadzimy też przechowalnię kół — nie musisz targać opon do piwnicy."),
    ("Wymiana oleju i filtrów", "wycena od ręki",
     "Olej + filtr na poczekaniu.",
     "Wymiana oleju silnikowego i kompletu filtrów (olejowy, powietrza, kabinowy, paliwa). Używamy olejów zgodnych ze specyfikacją producenta. Zwykle na poczekaniu."),
    ("Serwis klimatyzacji", "wycena od ręki",
     "Nabicie, odgrzybianie, test szczelności.",
     "Pełny serwis klimatyzacji: kontrola i uzupełnienie czynnika, test szczelności układu, odgrzybianie, wymiana filtra kabinowego."),
    ("Diagnostyka komputerowa", "wycena od ręki",
     "Odczyt błędów i jasna wycena naprawy.",
     "Profesjonalny odczyt i analiza błędów sterowników (silnik, ABS, airbag, DPF). Mówimy dokładnie co się dzieje i ile będzie kosztować naprawa."),
    ("Układ hamulcowy", "wycena od ręki",
     "Tarcze, klocki, płyn — od ręki.",
     "Wymiana tarcz i klocków, przewodów oraz płynu hamulcowego, naprawa zacisków. Sprawdzimy cały układ i powiemy uczciwie, co wymaga wymiany."),
    ("Mechanika ogólna", "wycena od ręki",
     "Naprawy bieżące i sezonowe przeglądy.",
     "Naprawy bieżące, przeglądy sezonowe, wymiana zawieszenia, rozrządu i osprzętu. Jasna wycena przed rozpoczęciem pracy."),
]
SERVICES_NOTE = "Nie widzisz swojej usterki? Zadzwoń — powiemy od razu, czy pomożemy i ile to kosztuje."

# ---- reviews ----
# Honest reviews section: no fabricated named testimonials. We show the real
# aggregate Google rating and link to the live Google listing. The owner can add
# real, hand-picked quotes here (list of (body, author, stars)) after signing.
REVIEWS = []
REVIEWS_BADGE = "Opinie z Google"
REVIEWS_SUBHEAD = "4,1 / 5 — średnia z ponad 424 opinii w Google"
GOOGLE_REVIEWS_CTA = "Zobacz opinie w Google"
# No stable Google Maps place/CID URL is publicly exposed for this listing, so we
# link to a Maps search for the business, which surfaces the profile and reviews.
GOOGLE_REVIEWS_URL = MAPS_URL

# ---- callback form ----
FORM_SLUG = "oddzwonimy"
FORM_NAME = "Oddzwonimy — callback"
FORM_HEADLINE = "Zostaw numer — oddzwonimy do 15 min"
FORM_SUB = "w godzinach pracy"
FORM_SUCCESS = "Dziękujemy! Oddzwonimy do 15 minut w godzinach pracy."
FORM_SUBMIT = "Zamów rozmowę"
FORM_FOOTER = "Wysyłając numer zgadzasz się na kontakt telefoniczny w sprawie Twojego zapytania."
# Leads must reach a human before this link is ever advertised (P0 lesson: forms went live empty).
FORM_NOTIFY_EMAILS = "stan.zak.inf@gmail.com"

# ---- photos, theme, SEO: keep from autoserwis config.py (same look) ----
# Only override SEO strings:
SEO_TITLE = "Warsztat i wulkanizacja Kraków — Intra Cars (Prądnik Czerwony)"
SEO_DESC = ("Autoserwis i wulkanizacja w Krakowie na al. 29 Listopada (Prądnik Czerwony). "
            "Mechanika, wymiana oleju, klimatyzacja, opony. Otwarte codziennie do 23:00. "
            "Zadzwoń: +48 12 311 02 01.")
SEO_LANG = "pl"
SEO_NOINDEX = True   # flip to False at go-live (after owner confirms details)
PRICE_RANGE = ""     # empty on purpose — no verifiable prices, so schema asserts no range
                     # (prior "40–1500 zł" was invented, removed 2026-07-23)

# ---- photos (Unsplash, host allowlisted in givyx.websites) — kept from autoserwis ----
def u(pid, w, h=None):
    hp = f"&h={h}" if h else ""
    return f"https://images.unsplash.com/{pid}?q=75&w={w}{hp}&auto=format&fit=crop"

HERO_BG = u("photo-1625047509168-a7026f36de04", 1800)   # dark workshop bay
VISIT_PHOTO = ("photo-1615906655593-ad0386982a0f", 900, 700)  # mechanic at engine, cropped landscape
GALLERY = [  # (unsplash id, caption) — all cropped to uniform 4:3 (800x600)
    ("photo-1615906655593-ad0386982a0f", "Diagnostyka pod maską"),
    ("photo-1625047509168-a7026f36de04", "Hala serwisowa"),
    ("photo-1530046339160-ce3e530c7d2f", "Narzędziownia"),
    ("photo-1487754180451-c456f719a1fc", "Wymiana oleju"),
    ("photo-1486262715619-67b85e0b08d3", "Serwis osprzętu silnika"),
    ("photo-1632823469850-2f77dd9c7f93", "Dbałość o detale"),
]
GALLERY_W, GALLERY_H = 800, 600

# ---- theme / palette — kept from autoserwis ----
BG0 = "#0B0E11"      # page background
BG1 = "#10141A"      # alternate section
CARD = "#151B22"     # card surface
BORDER = "#242C36"
FG = "#F2F4F6"
MUTED = "#9AA6B2"
ACCENT = "#F5A524"        # amber — accents, prices, stars
ACCENT_INK = "#14181D"    # dark text on amber buttons
BTN_FORM = "#E8590C"      # form submit bg (white text needs darker orange)
OK_GREEN = "#4ADE80"
