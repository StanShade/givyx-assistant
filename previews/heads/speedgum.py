# Speed-Gum Serwis Opon (Tomasz Gil) — head (concat with ../_shared_tail.py). slug: speedgum
#
# REWRITTEN FROM SCRATCH 2026-07-22 against Speed-Gum/RESEARCH.md.
# ⛔ The 18-July version of this file is dead (moved aside unread). It carried FIVE
#    invented prices (od 40 zł/koło, od 200 zł, od 150 zł, "Diagnostyka komputerowa
#    od 100 zł", od 250 zł), PRICE_RANGE "40–1500 zł", and four services no source
#    supports (olej, hamulce, diagnostyka, mechanika ogólna). The 100 zł diagnostics
#    line is the exact error that cost us Bielarz. Nothing below is inherited from it.
#
# SOURCES — every line below is one of:
#   [R]  RESEARCH.md §1 (cabb.pl NIP registry / Panorama Firm / Stan's phone call)
#   [P]  Speed-Gum/photos/*.jpg — his OWN signage, photographed at the workshop.
#        Primary source, stronger than any directory. The photo is named inline.
#   [G]  Nominatim geocode of the [R]-verified street address, 2026-07-22.
# Nothing here is inferred. Facts that are only *probable* (przechowalnia opon,
# wymiana oleju, sobota) are listed at the bottom as questions, NOT on the site.

NAME = "Speed-Gum Serwis Opon"; NAME_UPPER = "SPEED-GUM SERWIS OPON"
# Registered: "Speed-Gum Serwis Opon Tomasz Gil", jednoosobowa działalność [R]
OWNER = "Tomasz Gil"                                  # [R] cabb.pl + Panorama Firm
NIP = "6760019563"                                    # [R] cabb.pl
DISTRICT = "Kraków Prądnik Biały"; CITY = "Kraków"; STREET = "ul. Grażyny 6"
POSTAL = "31-217"                                     # [R] cabb.pl + Panorama Firm agree
REGION = "małopolskie"
PHONE_DISPLAY = "537 326 327"                         # [R] Panorama; Stan dialled it
PHONE_FULL = "+48 537 326 327"; PHONE_TEL = "tel:+48537326327"
# The same number is painted on his own banner AND on the workshop door plate [P]
EMAIL = "speed-gum@op.pl"                             # [R] Panorama Firm detail page
MAPS_URL = "https://maps.google.com/maps?cid=16893387397691167494"   # [R]

# HOURS — was the blocking gap in BUILD-SPEC §1 (#3). CLOSED 2026-07-22 by the
# door plate in photos/unnamed-2.jpg: "SERWIS OPON / PN-PT 8:00-16:00 /
# Tel. 537 326 327". Saturday and Sunday are NOT on the plate, so they are NOT on
# the site — one confirmed row beats three plausible ones. [P]
HOURS = [("Poniedziałek – Piątek", "8:00 – 16:00")]
OPEN_LINE = "Pn–Pt 8:00–16:00"                        # [P] day-agnostic, never "dziś otwarte"

# Trust strip — BUILD-SPEC §2 allows only: "od 2023", "Prądnik Biały", and a
# service specialisation. No rating (Panorama shows "(0 opinii)"; our 5,0★ note
# was never refreshed), no counts, nothing numeric that isn't verified.
TRUST = [
    ("od 2023", "warsztat na Prądniku Białym"),        # [R] registered 09-10-2023
    ("Prostowanie felg", "nie tylko wymiana opon"),    # [R] jego własny spis usług
    ("Klimatyzacja", "serwis i nabijanie"),            # [R] + baner „KLIMATYZACJA” [P]
]

# SERVICES — exactly the six from his own Panorama Firm listing [R], verbatim in
# meaning. He publishes NO prices anywhere, so every price cell is "wycena od ręki".
# The long descriptions say what the service IS; they never claim a method, a time,
# a guarantee or a part brand that no source gives us.
_WYCENA = ("Cena zależy od rozmiaru koła i zakresu pracy — wycenę podajemy od ręki, "
           "przez telefon albo na miejscu, zanim zaczniemy robotę.")
SERVICES = [
    ("Wulkanizacja i naprawa opon", "wycena od ręki",
     "Uszkodzoną oponę oceniamy i naprawiamy, jeśli się da.",
     "Wulkanizacja i naprawa opon. Po zdjęciu opony z felgi oceniamy uszkodzenie i mówimy wprost, "
     "czy da się je naprawić, czy opona nadaje się już tylko do wymiany."),
    ("Wymiana opon i kół", "wycena od ręki",
     "Sezonowa zmiana i montaż nowych opon.",
     "Wymiana opon i kół — sezonowa zmiana na letnie i zimowe albo montaż nowego kompletu. "
     "Po wymianie i przejechaniu 50–100 km trzeba sprawdzić dokręcenie śrub; u nas zrobimy to bezpłatnie."),
    ("Wyważanie kół", "wycena od ręki",
     "Koło kręci się równo, kierownica nie drga.",
     "Wyważanie kół na wyważarce. Niewyważone koło daje drgania na kierownicy i szybciej zużywa "
     "oponę oraz elementy zawieszenia."),
    ("Prostowanie felg", "wycena od ręki",
     "Krzywa felga po dziurze — nie zawsze na złom.",
     "Prostowanie felg. Zakrzywiona po dziurze felga potrafi powodować ubytek powietrza i drgania — "
     "często da się ją wyprostować zamiast kupować nową."),
    ("Serwis i nabijanie klimatyzacji", "wycena od ręki",
     "Nie chłodzi tak jak kiedyś? Sprawdzimy.",
     "Serwis i nabijanie klimatyzacji samochodowej. Układ z czasem traci czynnik i chłodzi coraz "
     "słabiej — sprawdzamy stan układu i uzupełniamy czynnik."),
    ("Naprawy bieżące samochodów", "wycena od ręki",
     "Drobne naprawy przy okazji wizyty.",
     "Bieżące naprawy samochodów. Zadzwoń i powiedz, co się dzieje — powiemy od razu, czy bierzemy "
     "to u siebie, czy lepiej pojechać gdzie indziej."),
]
SERVICES_NOTE = ("Nie wiesz, czy to u nas? Zadzwoń pod 537 326 327 — powiemy wprost, "
                 "czy to robimy i ile mniej więcej zajmie.")
# Highlighted under the service list on the home page. Straight off the poster in
# his own bay (photos/unnamed-10.jpg) — the one thing on the page a competitor
# cannot copy, because it is his own offer. [P]
SERVICES_HIGHLIGHT = ("Po wymianie kół i przejechaniu 50–100 km trzeba sprawdzić dokręcenie "
                      "śrub. U nas zrobisz to bezpłatnie — wpadnij, to sprawa na chwilę.")

# ---- copy -------------------------------------------------------------------
# Angle (BUILD-SPEC §2): sell the man, not "profesjonalizm". A jednoosobowa firma
# [R] trading since 2023 [R] competes on trust, not scale. Plain Polish, no
# "kompleksowa obsługa", no superlatives, no claim we cannot source.
HERO_EYEBROW = f"Serwis opon · {DISTRICT}"
HERO_H1 = "Serwis opon na Prądniku Białym. Prowadzi Tomasz Gil."
# Short on purpose: the address and the hours sit on the meta rail directly below
# it, and on a 375px screen every extra line pushes the fold.
HERO_SUB = ("Opony, koła i felgi, klimatyzacja i bieżące naprawy. Jednoosobowy warsztat "
            "— dzwonisz i od razu rozmawiasz z tym, kto robi robotę.")
HOME_SERVICES_EYEBROW = "Usługi"
HOME_SERVICES_TITLE = "Co dla Ciebie zrobimy"
HOME_SERVICES_LEAD = _WYCENA
USLUGI_SUBHEAD = "Opony, felgi, klimatyzacja i bieżące naprawy"
USLUGI_LEAD = _WYCENA
GALERIA_TITLE = "Warsztat przy Grażyny 6"
GALERIA_LEAD = ("Zdjęcia z naszego warsztatu — hala, montażownica, wyważarka i podnośnik. "
                "Nic z katalogu.")
FOOTER_TAG = f"Serwis opon · {DISTRICT}"
FOOTER_DESC = "Wulkanizacja, wymiana i wyważanie kół, prostowanie felg. Na Prądniku Białym od 2023."
CTA_TITLE = "Zadzwoń — powiemy od razu, czy pomożemy."
CTA_SUB = ("Jeden telefon wystarczy, żeby wiedzieć, ile to potrwa i ile będzie kosztować. "
           "Pracujemy od poniedziałku do piątku, 8:00–16:00.")
THANKS_TITLE = "Dziękujemy! Oddzwonimy."
THANKS_SUB = "Oddzwaniamy w godzinach pracy, od poniedziałku do piątku, 8:00–16:00."
LOC_HEADLINE = "Znajdziesz nas przy ul. Grażyny 6"
LOC_SUB = ("Prądnik Biały, Kraków. Szukaj żółtej tablicy „SERWIS OPON” przy bramie garażowej — "
           "tak wygląda wjazd na zdjęciu.")

# Callback form — the "do 15 minut" promise from the template is a service level
# nobody at Speed-Gum ever gave us. Softened to something he can actually keep.
FORM_HEADLINE = "Zostaw numer — oddzwonimy"
FORM_SUB = "w godzinach pracy: Pn–Pt 8:00–16:00"
FORM_SUCCESS = "Dziękujemy! Oddzwonimy w godzinach pracy (Pn–Pt 8:00–16:00)."
# Preview phase: leads come to US, not to Tomasz — he has not signed anything yet.
FORM_NOTIFY_EMAILS = "stan.zak.inf@gmail.com"

# Reviews: Panorama shows "(0 opinii)" and the 5,0★ in our old note was read on
# 2026-07-20 and never refreshed. No number, and no section pointing at a listing
# whose review count we have not checked. Drop it entirely. (BUILD-SPEC §2)
SHOW_REVIEWS = False

# "Zanim przyjedziesz" — both blocks come off his own signage, photographed.
INFO_STRIP = {
    "eyebrow": "Dobrze wiedzieć",
    "title": "Zanim przyjedziesz",
    "groups": [
        # photos/unnamed-10.jpg — banner hanging in the bay [P]
        ("Po wymianie kół", "list", [
            "Po przejechaniu 50–100 km sprawdź dokręcenie śrub.",
            "Możesz to zrobić sam albo bezpłatnie u nas w warsztacie.",
        ], False),
        # photos/unnamed-13.jpg — what his own banner says he does [P]
        ("Jeden telefon", "list", [
            "Powiemy od razu, czy bierzemy to u siebie.",
            "Wycenę usłyszysz przed robotą, nie po niej.",
        ], False),
        # "Jak trafić" is deliberately NOT here: the Dojazd section below already
        # carries the address, the hours, the yellow-board landmark and the map.
    ],
    "footnote": f"Speed-Gum Serwis Opon {OWNER} · NIP {NIP} · {STREET}, {POSTAL} {CITY}",
}

# Map — BUILD-SPEC §3 / BUILD.md: a coordinate is a fact like any other and the
# most checkable one on the page. Geocoded from the [R]-verified street address
# via Nominatim 2026-07-22: an exact house-number node ("6, Grażyny, Prądnik
# Biały, Kraków, 31-217") — NOT a district centroid, and NOT the 50.0651/19.9553
# Grzegórzki test fixture from the component docs. Pin opened and checked. [G]
MAP = {
    "lat": 50.0890116,
    "lon": 19.9502113,
    "zoom": 17,
    # `cid` = his real Google listing. givyx-map only loads Google on FULL consent
    # (OSM otherwise), and what it then shows is Google's own data about his own
    # business — not a claim we are making. Nothing third-party on first paint.
    "cid": "16893387397691167494",
    "caption": "Szukaj żółtej tablicy „SERWIS OPON” przy bramie garażowej.",
    "height": 340,
}

SEO_TITLE = "Serwis opon Kraków Prądnik Biały — Speed-Gum, ul. Grażyny 6"
SEO_DESC = ("Wulkanizacja i naprawa opon, wymiana i wyważanie kół, prostowanie felg, serwis "
            "klimatyzacji i bieżące naprawy. Kraków, ul. Grażyny 6. Pn–Pt 8:00–16:00. "
            "Zadzwoń: +48 537 326 327.")
SEO_LANG = "pl"
SEO_NOINDEX = True          # stays True until Tomasz signs (BUILD-SPEC §3)
PRICE_RANGE = "$$"          # nie publikuje żadnego cennika — nie wymyślamy widełek

# ---- theme ------------------------------------------------------------------
# Near-black with his own yellow. #FFC02E is picked off the "SERWIS OPON" board
# and the banner lettering in photos/unnamed-2.jpg and unnamed-13.jpg [P], so the
# site's accent is literally his sign colour rather than the template amber.
BG0 = "#07080A"; BG1 = "#0C0E12"; CARD = "#101319"; BORDER = "#1E2229"
FG = "#F4F6F8"; MUTED = "#8B939F"
ACCENT = "#FFC02E"; ACCENT_INK = "#14181D"
# Second colour, used structurally and sparingly (index numerals, check marks):
# the blue of the four icon tiles on his own banner. Two colours, both his.
ACCENT_2 = "#2E7FD1"
BTN_FORM = "#E8590C"; OK_GREEN = "#4ADE80"

LAYOUT = "editorial"        # photography-led page set (demos/autoserwis/editorial.py):
                            # display type at scale, numbered 01–06 service list,
                            # full-bleed statement band, double-bezel panels,
                            # sticky mobile call bar. Needs the `gx-shop` CSS kit.
MOTION = True               # gated gx-* motion layer (scroll reveal, stagger, hover).
                            # The hero opts out so the phone number never waits.
PRICE_QUIET = True          # he publishes no prices — "wycena od ręki" as a chip,
                            # not the same 24px headline six times.

# ---- photos -----------------------------------------------------------------
# REAL photos of his workshop, uploaded to the tenant's own image store
# (images.givyx.com — allowlisted by the renderer). Source: the shots Stan pulled
# from his Google listing 2026-07-22, cropped to 4:3 for the gallery. Every
# caption describes what is actually visible in the frame; none of them claims a
# service that is not in SERVICES. Two of the uploaded originals were obvious
# third-party stock (AC manifold gauges, a studio tyre-changer shot) and are NOT
# used. Swap in shots Tomasz sends us as soon as he sends them.
_IMG = "https://images.givyx.com/l-image/a_22a879a/l_c3c234e/"
HERO_BG = _IMG + "speedgum-hero-podnosnik.webp"     # auto na podnośniku, koła zdjęte
VISIT_PHOTO = (_IMG + "sg-g-wjazd.webp", 1200, 900)
VISIT_ALT = "Wjazd do warsztatu Speed-Gum przy ul. Grażyny 6 — brama garażowa i żółta tablica „SERWIS OPON”"
GALLERY_W, GALLERY_H = 1200, 900
GALLERY = [
    (_IMG + "sg-g-hala.webp", "Hala serwisowa przy ul. Grażyny 6"),
    (_IMG + "sg-g-montazownica.webp", "Wymiana opon i kół"),
    (_IMG + "sg-g-wywazarka.webp", "Wyważanie kół"),
    (_IMG + "sg-g-kola.webp", "Koła zdjęte do wymiany"),
    (_IMG + "sg-g-naprawy.webp", "Auto na podnośniku"),
    (_IMG + "sg-g-magazyn.webp", "Zaplecze — opony na regałach"),
]
# His own banner, photographed. Not decoration: it is the shop's own wording.
# (Used by the default layout; the editorial layout uses STATEMENT instead.)
PHOTO_BAND = {
    "src": _IMG + "speedgum-baner.webp",
    "alt": "Baner Speed-Gum: SERWIS OPON, KLIMATYZACJA – SZYBKIE NAPRAWY, tel. 537 326 327",
    "w": 1360, "h": 257,
}
# Full-bleed band. Both lines describe only what is visible in that photograph:
# two Redats posts, an Invento tyre changer, an M&B WB640N balancer, tyre racks.
STATEMENT = {
    "src": _IMG + "sg-g-hala.webp",
    "position": "center 62%",
    "title": "Montażownica, wyważarka i podnośnik — wszystko przy Grażyny 6.",
    "sub": ("Jedna hala, w której koło zdejmiemy, oponę naprawimy albo wymienimy, "
            "felgę wyprostujemy i koło wyważymy. Bez odsyłania w trzy miejsca."),
}

# ---- NOT on the site: things we saw but cannot stand behind ------------------
# Ask Tomasz before any of these ships:
#  1. Sobota/niedziela — the door plate only covers Pn–Pt. Otwarte w soboty?
#  2. "PRZECHOWALNIA OPON I KÓŁ" banner in photos/unnamed-11.jpg — clearly a real
#     service, but half the wording and the price ("Cena 100...") are hidden
#     behind the lift post. Service AND price stay off the site until confirmed.
#  3. Oil-can icon on the main banner [P] — suggests wymiana oleju, but no source
#     says it in words. Not published.
#  4. Rating — Panorama says "(0 opinii)". Confirm from Google before any star
#     goes anywhere near this site.
#  5. The free bolt re-torque wording is reconstructed from a poster that is cut
#     off at the right edge. Meaning is unambiguous; confirm it verbally anyway.
#  6. Photos are his Google-listing shots. Ask him to send originals (and one of
#     himself — for a one-man shop that beats every other image on the page).
