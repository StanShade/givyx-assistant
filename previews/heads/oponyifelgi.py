# ZUW Opony i Felgi (Brzukała & Moskała) — head (concat with ../_shared_tail.py). slug: oponyifelgi
# Research pass 2026-07-21: own site (4 pages, HTTP), goodyear.eu dealer page, debica.com.pl dealer list,
# Google Maps cid=12983370118901642674, panoramafirm, biznesfinder. NO prices published anywhere.
# ⚠️ PRIOR VERSION INVENTED olej/klima/diagnostyka/hamulce + "od X zł" prices. They are a TYRE SHOP only.
NAME = "ZUW Opony i Felgi"; NAME_UPPER = "ZUW OPONY I FELGI"
# Official/sign name is "Zakład Usług Wulkanizacyjnych" (s.c. Janusz Brzukała, Zbigniew Moskała) — same on Google.
DISTRICT = "Kraków Bieżanów-Prokocim"; CITY = "Kraków"; STREET = "ul. Jerzmanowskiego 14"
POSTAL = "30-836"  # VERIFIED (Goodyear JSON-LD + Panoramafirm + Google)
REGION = "małopolskie"
PHONE_DISPLAY = "12 658 74 27"; PHONE_FULL = "+48 12 658 74 27"; PHONE_TEL = "tel:+48126587427"
# also kom. 504 121 596 and 504 121 598 (both on their own "Informacje o nas" page)
EMAIL = "zuw@oponyifelgi.krakow.pl"  # VERIFIED on own site (also z.moskala@ and jbrzukala@)
MAPS_URL = "https://www.google.com/maps?cid=12983370118901642674"  # VERIFIED — resolves to their listing
# ⚠️CONFIRM HOURS — genuine conflict. Google Business Profile + Panoramafirm say 8–17 / Sob 8–13 (used below).
# Their own 2003-era site AND the Goodyear dealer record say 8–19 / Sob 8–14. Ask the owner before go-live.
HOURS = [("Poniedziałek – Piątek", "8:00 – 19:00"), ("Sobota", "8:00 – 14:00"), ("Niedziela", "nieczynne")]  # ⚠️CONFIRM — ICH WŁASNA strona; Google mówi 8–17/8–13
OPEN_LINE = "Opony, felgi i wulkanizacja — Prokocim, Kraków"  # neutralny: przy niepotwierdzonych godzinach nie powtarzamy ich w nagłówku
TRUST = [("od 1980", "na rynku"), ("4,3 ★", "117 opinii Google"), ("Goodyear · Dębica", "punkt dealerski")]
SERVICES = [
    ("Wulkanizacja i naprawa ogumienia", "wycena od ręki", "Naprawa przebić i uszkodzeń opon.", "Serwis i wulkanizacja opon, naprawa ogumienia. Profesjonalny sprzęt do wymiany i naprawy opon oraz fachowa kadra."),
    ("Sezonowa wymiana opon", "wycena od ręki", "Zmiana opon na letnie i zimowe.", "Sezonowa wymiana i zmiana opon — przed sezonem warto umówić termin telefonicznie."),
    ("Wyważanie kół", "wycena od ręki", "Dłuższa żywotność opon i zawieszenia.", "Wyważanie kół przedłuża żywotność opon i zawieszenia, poprawia komfort jazdy i trzymanie się drogi."),
    ("Przechowalnia opon", "wycena od ręki", "Sezonowe przechowywanie w dobrych warunkach.", "Sezonowe przechowywanie opon w odpowiednich warunkach, wraz z konserwacją i przeglądem ich stanu — opony nie pękają i wolniej się starzeją."),
    ("Sprzedaż opon, felg i akumulatorów", "wycena od ręki", "16 marek opon, felgi Alcar, akumulatory.", "Opony Michelin, Continental, Goodyear, Dunlop, Pirelli, Bridgestone, Dębica, Sava, Barum, Kleber, Kormoran, Riken, Uniroyal, Goodrich, Firestone i Dayton. Felgi stalowe i aluminiowe Alcar (AEZ, DOTZ, DEZENT, ENZO). Akumulatory Centra i Exide."),
    ("Prostowanie i renowacja felg", "wycena od ręki", "Felgi aluminiowe i stalowe.", "Prostowanie i renowacja felg aluminiowych oraz stalowych."),  # ⚠️CONFIRM — nie ma tego na ich stronie; źródło: kategorie Panorama Firm + opinia Google
]
# ---- copy (bez tego szablon dopisuje "mechanikę i klimatyzację" — to firma oponiarska) ----
# Teksty przeniesione 1:1 z wersji, która jest już na żywo na oponyifelgi.givyx.com — wcześniej
# siedziały w ręcznie edytowanym build_pages.py klonu, więc świeży `cp -r` by je skasował.
# Prostowania felg NIE ma w żadnym z tych tekstów: jest w SERVICES z ⚠️CONFIRM, więc nie
# trafia ani na hero, ani do stopki, dopóki ZUW go nie potwierdzi telefonicznie.
HERO_EYEBROW = f"Serwis opon · {DISTRICT}"
HERO_H1 = "Opony, felgi i wulkanizacja. Od 1980."
HERO_SUB = ("Wulkanizacja i naprawa ogumienia, sezonowa wymiana, wyważanie kół i przechowalnia "
            "opon. Sprzedaż opon, felg i akumulatorów.")
_WYCENA = ("Cena zależy od rozmiaru koła i zakresu pracy — wycenę podajemy od ręki, "
           "przez telefon albo na miejscu, zawsze przed rozpoczęciem pracy.")
HOME_SERVICES_EYEBROW = "Usługi"
HOME_SERVICES_TITLE = "Co dla Ciebie zrobimy"
HOME_SERVICES_LEAD = _WYCENA
USLUGI_SUBHEAD = "Serwis opon, felgi i akumulatory"
USLUGI_LEAD = _WYCENA
GALERIA_TITLE = "Opony, felgi i nasza robota"
GALERIA_LEAD = ("Wulkanizacja, sezonowa wymiana, wyważanie kół, przechowalnia oraz sprzedaż "
                "opon i felg — tym zajmujemy się od 1980 roku.")
FOOTER_TAG = f"Serwis opon · {DISTRICT}"
FOOTER_DESC = "Wulkanizacja, wymiana i wyważanie opon, sprzedaż opon i felg. Na rynku od 1980."
# Listy marek prosto z ich strony sprzedażowej (oponyifelgi.krakow.pl, research 2026-07-21).
# Same marki — cen nie publikują, więc żadnych tu nie ma.
INFO_STRIP = {
    "eyebrow": "Sprzedaż",
    "title": "Marki, które mamy na stanie",
    "groups": [
        ("Opony", "chips", [
            "Michelin", "Continental", "Goodyear", "Dunlop", "Pirelli",
            "Bridgestone", "Dębica", "Sava", "Barum", "Kleber", "Kormoran",
            "Riken", "Uniroyal", "Goodrich", "Firestone", "Dayton",
        ], True),
        ("Felgi Alcar", "chips", ["AEZ", "DOTZ", "DEZENT", "ENZO"], False),
        ("Akumulatory", "chips", ["Centra", "Exide"], False),
    ],
    "footnote": "Punkt w sieci dealerskiej Goodyear i Dębica",
}
REVIEWS_SUBHEAD = "4,3 ★ na podstawie 117 opinii w Google"  # ⚠️ odczyt 2026-07-21, odświeżyć przed wysyłką
LOC_HEADLINE = "Znajdziesz nas w Prokocimiu"
LOC_SUB = "ul. Jerzmanowskiego 14, Kraków Prokocim Nowy. Kręcimy się tu od 1980 roku."
SEO_TITLE = "Opony, felgi i wulkanizacja Kraków Prokocim — ZUW od 1980"
SEO_DESC = "Wulkanizacja, sezonowa wymiana i wyważanie kół, przechowalnia opon oraz sprzedaż opon i felg w Krakowie Prokocimiu. Na rynku od 1980. Zadzwoń: +48 12 658 74 27."
SEO_LANG = "pl"; SEO_NOINDEX = True; PRICE_RANGE = "$$"  # nie publikują żadnego cennika — nie wymyślamy widełek

# ---- imagery (overrides the generic mechanic set in _shared_tail.py) ----
# ⚠️ The shared tail defaults are engine-bay/oil-change photos captioned "Wymiana oleju",
#    "Diagnostyka pod maską", "Serwis osprzętu silnika", "Narzędziownia" — services ZUW
#    does NOT offer. Every id below was fetched and visually verified 2026-07-21, and every
#    caption maps 1:1 onto a service in SERVICES above. Nothing here implies mechanika,
#    olej, klimatyzacja, hamulce or diagnostyka.
#    All ids resolve on images.unsplash.com (the only allowlisted stock host).
HERO_BG_ID = "photo-1675034743372-672c3c3f8377"          # wnętrze serwisu opon: felgi na ścianie, stosy opon
VISIT_PHOTO = ("photo-1645445522156-9ac06bc7a767", 900, 700)  # serwisant przy kole auta w hali
VISIT_ALT = "Serwisant przy kole samochodu w hali serwisu opon"
GALLERY = [
    ("photo-1599082267768-4815b2ea6bd2", "Sezonowa wymiana opon"),          # opona zakładana na montażownicę
    ("photo-1702146713922-613313be011d", "Wulkanizacja i naprawa ogumienia"),  # opona zdjęta do naprawy
    ("photo-1764015805414-df7de89d405b", "Wyważanie i montaż kół"),         # klucz udarowy przy śrubach koła
    ("photo-1765128332063-0bd96fa009b6", "Przechowalnia opon"),             # opony w regale magazynowym
    ("photo-1591117728047-2dc00780492c", "Felgi aluminiowe i stalowe"),     # zbliżenie felgi aluminiowej
    ("photo-1527266258038-6ae3e089a609", "Sprzedaż opon"),                  # zapas opon w różnych rozmiarach
]
