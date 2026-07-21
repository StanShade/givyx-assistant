# D.W. Serwis (J. i M. Wójcik) — head (concat with ../_shared_tail.py). slug: dwserwis
# Research pass 2026-07-21: own site opony.krakow.pl (live, cert OK), Google Maps cid=8277491864947805917,
# Panoramafirm, znajdzmechanika. NO prices published. Pure serwis opon — NIE mechanika ogólna.
# ⚠️ PRIOR VERSION INVENTED przechowalnia/TPMS/olej/diagnostyka/hamulce/klima + "od X zł". Stripped.
# ⚠️ duet@oponykrakow.pl and the 160–390 zł cennik on oponykrakow.pl belong to a DIFFERENT company
#    (P.H.U. DUET s.c., ul. Wolska 1). Never use them.
NAME = "D.W. Serwis"; NAME_UPPER = "D.W. SERWIS"
# Legal: "D. W. Serwis" S.C. Jolanta i Mariusz Wójcik
DISTRICT = "Kraków Bieńczyce"; CITY = "Kraków"; STREET = "ul. gen. Leopolda Okulickiego 71"
POSTAL = "31-637"  # VERIFIED (own site + Google + Panoramafirm)
REGION = "małopolskie"
PHONE_DISPLAY = "502 402 802"; PHONE_FULL = "+48 502 402 802"; PHONE_TEL = "tel:+48502402802"
# also 12 648 02 15 (Panorama Firm / znajdzmechanika)
EMAIL = "pomoc@opony.krakow.pl"  # VERIFIED — z ich własnej, żywej strony (drugi: oponyserwis@poczta.onet.pl)
MAPS_URL = "https://www.google.com/maps?cid=8277491864947805917"  # VERIFIED — resolves to their listing
HOURS = [("Poniedziałek – Piątek", "8:00 – 18:00"), ("Sobota", "8:00 – 14:00"), ("Niedziela", "nieczynne")]  # VERIFIED — own site AND Google Business Profile agree
OPEN_LINE = "Pn–Pt 8:00–18:00 · Sob 8:00–14:00"  # day-agnostic, nie kłamie w sobotę
TRUST = [("od 1994", "w branży oponiarskiej"), ("4,8 ★", "282 opinie Google"), ("Maruni", "japońskie naprawy opon")]
SERVICES = [
    ("Wymiana opon z wyważeniem", "wycena od ręki", "Koła zdejmiemy, wymienimy i wyważymy.", "Wymienimy i wyważymy Twoje koła, a w razie potrzeby wymienimy także zawory w felgach. Bez umawiania — wjeżdżasz w kolejkę."),
    ("Naprawa opon", "wycena od ręki", "Naprawa japońskimi materiałami Maruni.", "Opona uległa uszkodzeniu? Po zdemontowaniu ocenimy uszkodzenie i jeśli tylko to możliwe, naprawimy ją za pomocą japońskich materiałów Maruni."),
    ("Wyważanie kół", "wycena od ręki", "Wibracje na kierownicy? To znak.", "W trakcie użytkowania opona się ściera i zmienia się rozkład masy na kole. Producenci opon zalecają wyważanie co 10 tys. km."),
    ("Wymiana zaworów w felgach", "wycena od ręki", "Robimy przy okazji wymiany.", "Zawory wymieniamy przy wymianie opon, jeśli jest taka potrzeba — bez osobnej wizyty."),
    ("Zmiana na drugi komplet kół", "wycena od ręki", "Sezonowa zmiana z Twoich kół.", "Zakładamy Twój drugi komplet kół. Pamiętaj o pierścieniach centrujących i śrubach, jeśli są inne niż w pierwszym komplecie."),
]
# ---- copy (bez tego szablon dopisuje "diagnostykę komputerową, mechanikę i klimatyzację",
#      a to warsztat WYŁĄCZNIE oponiarski — patrz SERVICES powyżej) ----
# Teksty przeniesione 1:1 z wersji, która jest już na żywo na dwserwis.givyx.com — wcześniej
# siedziały w ręcznie edytowanym build_pages.py klonu, więc świeży `cp -r` by je skasował.
HERO_EYEBROW = f"Serwis opon · {DISTRICT}"
HERO_H1 = "Opony to nasza jedyna robota. Od 1994."
HERO_SUB = ("Wymiana opon z wyważeniem, naprawa opon japońskimi materiałami Maruni i wyważanie kół. "
            "Bez umawiania — wjeżdżasz w kolejkę.")
_WYCENA = ("Cena zależy od rozmiaru koła i zakresu pracy — wycenę podajemy od ręki, "
           "przez telefon albo na miejscu, zawsze przed rozpoczęciem pracy.")
HOME_SERVICES_EYEBROW = "Usługi"
HOME_SERVICES_TITLE = "Co dla Ciebie zrobimy"
HOME_SERVICES_LEAD = _WYCENA
USLUGI_SUBHEAD = "Serwis opon i wulkanizacja"
USLUGI_LEAD = _WYCENA
GALERIA_LEAD = ("Opony, koła i felgi — od wymiany z wyważeniem po naprawę materiałami Maruni. "
                "Bez mechaniki, bez oleju: robimy jedno i robimy to dobrze.")
FOOTER_TAG = f"Serwis opon · {DISTRICT}"
FOOTER_DESC = "Wymiana, naprawa i wyważanie opon. W branży od 1994."
# "Zanim przyjedziesz" — trzy rzeczy, które D.W. Serwis sam wymienia na opony.krakow.pl,
# plus kolejka bez umawiania (własna strona) i gotówka (atrybut Google + opinie). Bez cen.
INFO_STRIP = {
    "eyebrow": "Zanim przyjedziesz",
    "title": "Krótka lista przed wizytą",
    "groups": [
        ("Weź ze sobą", "list", [
            "końcówka do śrub antykradzieżowych",
            "pierścienie centrujące do drugiego kompletu kół",
            "śruby, jeśli inne niż w pierwszym komplecie",
        ], False),
        ("Dobrze wiedzieć", "list", [
            "Bez umawiania — wjeżdżasz w kolejkę",
            "Płatność gotówką",
        ], False),
    ],
}
REVIEWS_SUBHEAD = "4,8 ★ na podstawie 282 opinii w Google"  # ⚠️ odczyt 2026-07-21, odświeżyć przed wysyłką
LOC_HEADLINE = "Znajdziesz nas w Bieńczycach"
LOC_SUB = "ul. gen. Leopolda Okulickiego 71, Kraków. W tym miejscu od 2003 roku. Płatność gotówką."  # ⚠️CONFIRM "gotówką" — atrybut Google + 3 opinie
SEO_TITLE = "Serwis opon i wulkanizacja Kraków Bieńczyce — D.W. Serwis od 1994"
SEO_DESC = "Wymiana opon z wyważeniem, naprawa opon materiałami Maruni i wyważanie kół w Krakowie Bieńczycach. W branży od 1994, 4,8★ w Google. Zadzwoń: +48 502 402 802."
SEO_LANG = "pl"; SEO_NOINDEX = True; PRICE_RANGE = "$$"  # nie publikują cennika; cennik z oponykrakow.pl to INNA firma

# ---- imagery (overrides the generic mechanic set in _shared_tail.py) ----
# ⚠️ The shared tail defaults are engine-bay/oil-change photos captioned "Wymiana oleju",
#    "Diagnostyka pod maską", "Serwis osprzętu silnika", "Narzędziownia" — services D.W.
#    Serwis does NOT offer. Every id below was fetched and visually verified 2026-07-21,
#    and every caption maps 1:1 onto a service in SERVICES above. Nothing here implies
#    sprzedaż opon, przechowalnia, mechanika, TPMS, klimatyzacja or diagnostyka.
#    All ids resolve on images.unsplash.com (the only allowlisted stock host).
HERO_BG_ID = "photo-1657307913178-97cb5a4d0cd7"          # makro bieżnika opony — ciemne, bez żadnej deklaracji usługi
VISIT_PHOTO = ("photo-1599082267768-4815b2ea6bd2", 900, 700)  # opona zakładana na montażownicę
VISIT_ALT = "Montaż opony na felgę na montażownicy w serwisie opon"
GALLERY = [
    ("photo-1645445522156-9ac06bc7a767", "Wymiana opon z wyważeniem"),   # dłonie serwisanta przy kole auta w hali
    ("photo-1702146713922-613313be011d", "Naprawa opon"),                # opona na feldze zdjęta do naprawy
    ("photo-1764015805414-df7de89d405b", "Zmiana na drugi komplet kół"), # klucz udarowy przy śrubach koła
    ("photo-1591117728047-2dc00780492c", "Wymiana zaworów w felgach"),   # zbliżenie felgi aluminiowej z oponą
    ("photo-1578844251758-2f71da64c96f", "Drugi komplet opon na sezon"), # komplety opon letnich i zimowych
]
