# Tłumiki Bielarz (Adam Bielarz) — head (concat with ../_shared_tail.py). slug: tlumiki
# Research pass 2026-07-21 (wszystkie źródła pobrane tego dnia):
#   • własna strona http://tlumiki.krakow.pl (HTTP 200; HTTPS ma wygasły cert innej domeny)
#     — 4 strony usługowe: /tlumiki-katalizatory/, /mechanika-pojazdowa/, /wulkanizacja/, /haki-holownicze/
#   • bielarz.supermechanik.pl (jego własna wizytówka) — najpełniejsza lista usług
#   • dobrymechanik.pl/mechanicy/krakow/adam-bielarz-tlumiki-mechanika.html — "Metody płatności: Gotówka"
#   • panoramafirm.pl (kategorie + e-mail), pkt.pl, biznesfinder.pl (NIP/REGON/PKD/rok),
#     polecanewarsztaty.net (jego własny opis), biznes-top.pl (mirror Google: ocena + rozkład gwiazdek)
#
# ⚠️ POPRZEDNIA WERSJA ZMYŚLIŁA: ceny ("od 100 zł", "od 250 zł", "od 150 zł", "od 40 zł/koło"),
#    "filtry DPF" oraz płatną "Diagnostykę komputerową". Nigdzie nie publikuje cennika, o DPF nie ma
#    ani słowa, a na własnej stronie DWA RAZY pisze: "Można u nas zdiagnozować każdą usterkę gratis".
#    Pomijała za to "Haki holownicze" — jedną z jego czterech własnych stron usługowych.
# ✅ Mechanika, hamulce, oleje/filtry i wulkanizacja są PRAWDZIWE — potwierdzone jego własną stroną.
#    To NIE jest warsztat wyłącznie od tłumików.
NAME = "Tłumiki Bielarz"; NAME_UPPER = "TŁUMIKI BIELARZ"
# Nazwa rejestrowa: "Adam Bielarz Mechanika Pojazdowa" (NIP 6761159935, REGON 350989110, PKD 45.20.Z)
DISTRICT = "Kraków Grzegórzki"; CITY = "Kraków"; STREET = "ul. Żółkiewskiego 28"
POSTAL = "31-539"  # VERIFIED (własna strona /kontakt/ + pkt.pl + panoramafirm + biznesfinder)
REGION = "małopolskie"
PHONE_DISPLAY = "601 489 603"; PHONE_FULL = "+48 601 489 603"; PHONE_TEL = "tel:+48601489603"
# stacjonarny 12 430 47 53 — VERIFIED (na każdej podstronie jego witryny). Płatność: GOTÓWKA.
EMAIL = "biuro@tlumiki.krakow.pl"  # VERIFIED w wizytówce Panorama Firm; ⚠️CONFIRM czy skrzynka działa
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=T%C5%82umiki+Bielarz+%C5%BB%C3%B3%C5%82kiewskiego+28+Krak%C3%B3w"
# Pn–Pt 8:30–18:00 zgodne na własnej stronie, polecanewarsztaty i w Google (mirror biznes-top).
# ⚠️CONFIRM sobota: własna strona / polecanewarsztaty / pkt / panoramafirm = 10:00–14:00,
#    Google i supermechanik = 10:00–13:00. Bierzemy jego własną stronę.
HOURS = [("Poniedziałek – Piątek", "8:30 – 18:00"), ("Sobota", "10:00 – 14:00"), ("Niedziela", "nieczynne")]  # ⚠️CONFIRM sobota
# non-day-specific (godziny różnią się w sobotę; statyczne "otwarte do 18:00" kłamałoby w sobotę)
OPEN_LINE = "Tłumiki, mechanika i wulkanizacja — Grzegórzki, Kraków"
TRUST = [("od 1990", "warsztat w Krakowie"), ("4,8 ★", "308 opinii Google"), ("Tłumiki · Katalizatory", "specjalizacja")]
# Każda pozycja poniżej ma pokrycie w jego własnych materiałach. Żadnych cen — nigdzie ich nie publikuje
# (przeciwnie: "Wszystkie w cenach hurtowych", "Najniższe ceny", diagnoza gratis).
SERVICES = [
    ("Tłumiki i układy wydechowe", "wycena od ręki", "Spawanie, wymiana, sondy lambda.", "Naprawa uszkodzonych układów wydechowych (spawanie) i wymiana zużytych elementów na nowe. Wymieniamy też sondy lambda oraz złącza elastyczne (tzw. tłumiki drgań). Montujemy tłumiki Asmet, Bosal, Walker, Tesch, Ferroz."),
    ("Katalizatory", "wycena od ręki", "Wymiana zużytego katalizatora.", "Katalizator to element układu wydechowego. Norma to ok. 100 000 km — po tym przebiegu nie dopala już spalin, a wręcz przytyka układ wydechowy. Uszkodzony wymienimy na nowy."),
    ("Tłumiki sportowe i końcówki", "wycena od ręki", "Przeróbki na sportowe i basowe.", "Przeróbka układów tradycyjnych na sportowe i basowe, końcówki ozdobne oraz montaż strumienic. Tłumiki sportowe i końcówki basowe firmy Ulter."),
    ("Mechanika pojazdowa", "wycena od ręki", "Naprawiamy każdą markę.", "Kompleksowe naprawy i wymiany eksploatacyjne podzespołów: zawieszenie i wahacze, amortyzatory, hamulce (tarcze, klocki, szczęki), oleje i filtry, paski, łożyska, pompy wody, sprzęgła. Wykonujemy również regulacje i remonty silników benzynowych. Usterkę zdiagnozujemy bez opłaty."),  # ⚠️CONFIRM "bez opłaty" — jego własne słowa ("zdiagnozować każdą usterkę gratis") na tlumiki.krakow.pl i polecanewarsztaty.net
    ("Wulkanizacja i opony", "wycena od ręki", "Wymiana, naprawa, przechowanie.", "Wymiana opon letnich, zimowych i wielosezonowych, naprawa opon oraz pompowanie azotem. Przechowujemy opony klientów poza sezonem. Opony nowe i używane. Pracujemy na nowych maszynach."),
    ("Haki holownicze", "wycena od ręki", "Montaż z wiązką elektryczną.", "Montaż haków holowniczych wraz z wiązkami elektrycznymi do wszystkich aut osobowych i busów. Haki tradycyjne (odkręcane) oraz tzw. automaty z szybkim demontażem kuli. Po montażu potrzebne jest jeszcze zaświadczenie ze stacji diagnostycznej i wpis w wydziale komunikacji."),
]
# Boilerplate copy that names usługi — bez tych trzech linii szablon sam dopisywał
# "diagnostykę komputerową i klimatyzację", których w żadnym jego źródle nie ma.
HERO_SUB = ("Tłumiki i katalizatory, mechanika pojazdowa, wulkanizacja i haki holownicze — "
            "w jednym miejscu, w Krakowie od 1990 roku. Wycenę podajemy od ręki.")
FOOTER_DESC = "Tłumiki, katalizatory, mechanika pojazdowa i wulkanizacja. W Grzegórzkach od 1990."
USLUGI_SUBHEAD = "Tłumiki, mechanika, wulkanizacja i haki"
REVIEWS_SUBHEAD = "4,8 ★ na podstawie 308 opinii w Google"  # odczyt 2026-07-21 (mirror Google: 5★ 282 / 4★ 12 / 3★ 2 / 2★ 1 / 1★ 11 = 308) — odświeżyć przed wysyłką
LOC_HEADLINE = "Znajdziesz nas w Grzegórzkach"
LOC_SUB = "ul. Żółkiewskiego 28, Kraków. Blisko centrum, w tym miejscu od 1990 roku. Płatność gotówką."  # ⚠️CONFIRM gotówka — źródło: DobryMechanik ("Metody płatności: Gotówka")
SEO_TITLE = "Tłumiki, katalizatory i mechanika Kraków Grzegórzki — Bielarz od 1990"
SEO_DESC = "Naprawa i spawanie układów wydechowych, wymiana katalizatorów, mechanika pojazdowa, wulkanizacja i haki holownicze w Krakowie Grzegórzkach. Wycena od ręki. Zadzwoń: +48 601 489 603."
SEO_LANG = "pl"; SEO_NOINDEX = True; PRICE_RANGE = "$$"  # nie publikuje żadnego cennika — nie wymyślamy widełek

# ---- imagery (overrides the generic mechanic set in _shared_tail.py) ----
# Domyślny zestaw z _shared_tail.py ma podpisy "Wymiana oleju", "Narzędziownia", "Serwis osprzętu
# silnika" — nie kłamią one wprost (on robi mechanikę), ale nie mówią nic o tłumikach, czyli o jego
# głównej specjalizacji i pierwszej kategorii w Google. Każde zdjęcie poniżej zostało pobrane
# i OBEJRZANE 2026-07-21, a każdy podpis odpowiada 1:1 usłudze z SERVICES powyżej.
# Żadne nie sugeruje DPF, klimatyzacji, geometrii ani lakiernictwa. Wszystkie na images.unsplash.com
# (jedyny dopuszczony host stocku; plus.unsplash.com NIE ładuje się).
HERO_BG_ID = "photo-1765903916132-7d2fa8ad4c66"               # ciemny spód auta: rura wydechowa i tłumik
VISIT_PHOTO = ("photo-1702146713858-8e7d1cc29fe8", 900, 700)  # mechanik pracujący pod uniesionym autem
VISIT_ALT = "Mechanik przy pracy pod uniesionym samochodem"
GALLERY = [
    ("photo-1759419282068-eb664e0f0a17", "Katalizatory i sondy lambda"),        # ściana z katalizatorami i kolektorami
    ("photo-1743314777689-1bb71ae148ca", "Naprawa układu wydechowego"),         # szlifierka kątowa i iskry przy rurze pod autem
    ("photo-1692309175422-b9d614f4764e", "Tłumiki sportowe i końcówki"),        # ozdobne końcówki wydechu w zderzaku
    ("photo-1625047509168-a7026f36de04", "Mechanika pojazdowa"),                # auto z otwartą maską na stanowisku
    ("photo-1599082267768-4815b2ea6bd2", "Wulkanizacja i wymiana opon"),        # opona zakładana na montażownicę
]
