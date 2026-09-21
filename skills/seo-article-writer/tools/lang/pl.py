#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lang/pl.py - Polish pattern pack for ai-cadence-check.py and read-aloud-check.py.

Same structure and names as en.py. All regexes run against LOWERCASED text
(str.lower() folds the Polish capitals), so no re.IGNORECASE is needed here.
Python's str regexes are Unicode-aware: \\b and \\w treat ą ć ę ł ń ó ś ź ż as
letters. Never write [a-z] in a Polish pattern - it skips every diacritic; use
LETTER_CLASS or \\w.

Calibrated against tools/tests/fixture-ai-pl.md (must fail) and
fixture-human-pl.md (must pass on both tools), then smoke-tested on the
AI-assisted Polish site copy of the givyx niche demos (remonty, fizjo). Add
new tells here when Stage 15 / Stage 16 finds one that slipped through, and
log them in checklists/anti-ai.md.

Polish-specific choices, for the next editor:
  - "nie X, ale Y" counts as an antithesis only when Y is not "ale i/też/
    także/również" (that is the Polish "not only ... but also", a flourish).
  - Bare "zamiast" is ordinary Polish; only the paired forms count.
  - "podróż" and "odblokować" are legitimate words in a car-service article;
    only their metaphorical frames are tells. "funkcjonalny" is a physio term
    (trening funkcjonalny) and is deliberately NOT a tell.
  - The usual empty Polish SME marketing words (profesjonalny, kompleksowy,
    najwyższa jakość, indywidualne podejście) sit in MARKETING_CLICHE and are
    counted with the LLM vocabulary: a language model writing for a warsztat
    reaches for exactly those.
"""

NAME = "Polish"
CALIBRATED = True

WORD_RE = r"[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż][A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż'\-]*"
LETTER_CLASS = "a-ząćęłńóśźż"

# Full stop after these does not end a sentence (the splitter glues the next
# piece back). Lowercase, without the final dot.
ABBREVIATIONS = {
    "np", "tzn", "tzw", "itp", "itd", "m.in", "ul", "al", "pl", "godz", "tel",
    "min", "max", "ok", "ww", "dr", "prof", "inż", "mgr", "św", "proc", "nr",
    "ust", "art", "pkt", "zob", "por", "ang", "łac", "tj", "wg", "ds", "str",
    "r", "ew", "cd", "jw", "ps", "poz", "lok", "woj", "pow", "gm",
}

# ---------------------------------------------------------------------------
# ai-cadence-check.py
# ---------------------------------------------------------------------------

# Function-word starts. Two consecutive sentences starting with one of these
# are normal Polish, not an AI parallelism, so category G ignores them.
CONNECTOR_STARTS = {
    "i", "a", "ale", "to", "ja", "ty", "my", "wy", "on", "ona", "ono", "oni",
    "one", "bo", "że", "ze", "jak", "gdy", "kiedy", "jeśli", "jeżeli", "tu",
    "tam", "nie", "tak", "czy", "w", "we", "na", "z", "do", "po", "od", "o",
    "u", "za", "przy", "przez", "pod", "nad", "dla", "bez", "ten", "ta", "te",
    "ci", "tego", "tej", "tym", "tych", "jest", "są", "był", "była", "było",
    "byli", "były", "będzie", "będą", "więc", "jednak", "też", "także", "co",
    "kto", "gdzie", "dlaczego", "jaki", "jaka", "jakie", "który", "która",
    "które", "ile", "może", "można", "trzeba", "mam", "masz", "mamy", "macie",
    "mają", "ma", "chcę", "mój", "moja", "moje", "twój", "twoja", "twoje",
    "nasz", "nasza", "nasze", "jego", "jej", "ich", "się", "no", "już",
    "jeszcze", "tylko", "nawet", "potem", "wtedy", "teraz", "dziś", "dzisiaj",
    "zawsze", "nigdy", "czasem", "każdy", "każda", "każde", "wszystko",
    "wszyscy", "ktoś", "nikt", "nic", "ani", "albo", "lub", "oraz", "żeby",
    "aby", "by", "dopiero", "właśnie", "im", "jako", "niech", "oto", "chyba",
    "pewnie", "raczej", "dlatego", "przecież", "zresztą", "natomiast", "zaś",
    "mimo", "choć", "chociaż", "skoro", "zanim", "ponieważ", "gdyż", "bowiem",
    "wiem", "wiesz", "widzę", "widzisz", "pamiętam", "kilka", "parę", "dwa",
    "dwie", "trzy", "raz", "druga", "drugi", "pierwsza", "pierwszy", "reszta",
    "u", "coś", "ktoś", "sam", "sama", "samo", "sami", "cała", "cały", "całe",
    "jedno", "jedna", "jeden", "tyle", "tak", "właściwie", "ogólnie", "poza",
}

# One-word sentences that are normal spoken Polish, not AI staccato.
ALLOWED_SHORT = {
    "tak", "nie", "dokładnie", "właśnie", "oczywiście", "jasne", "pewnie",
    "serio", "naprawdę", "prawie", "czasem", "czasami", "zawsze", "nigdy",
    "koniec", "kropka", "dobrze", "dobra", "okej", "spoko", "przykład",
    "podsumowanie", "uwaga", "dzięki", "przepraszam", "sorry", "niestety",
    "owszem", "otóż", "wcale", "absolutnie", "zdecydowanie", "raczej", "może",
    "chyba", "racja", "prawda", "błąd", "fakt", "nic", "nikt", "wszystko",
    "wszyscy", "gotowe", "załatwione", "zrobione", "sprawdzone", "wystarczy",
    "tyle", "dość", "ponownie", "znowu", "zresztą", "słuchaj", "patrz",
    "spójrz", "pytanie", "odpowiedź", "gorzej", "lepiej", "źle", "drogo",
    "tanio", "szybko", "wolno", "poważnie", "szczerze", "wreszcie",
    "nareszcie", "ostrożnie", "uważaj", "stop", "dalej", "zaraz", "chwila",
    "moment", "przykro", "szkoda", "bzdura", "bez", "no", "zgoda", "działa",
    "nieprawda", "przesada", "koniecznie", "niekoniecznie", "podobno",
    "ewentualnie", "mniej", "więcej", "nigdzie", "wszędzie", "tutaj", "tam",
    "teraz", "potem", "później", "wcześniej", "rzadko", "często", "zwykle",
    "warto", "faktycznie", "rzeczywiście", "owszem", "niezupełnie", "też",
}

# C) Literary flourishes and grandiose phrasing.
LITERARY = [
    r"\bw\s+dzisiejszym\s+(?:szybko\s+zmieniającym\s+się\s+|zabieganym\s+|cyfrowym\s+|nowoczesnym\s+)?świecie\b",
    r"\bw\s+dzisiejszych\s+czasach\b",
    r"\bwe\s+współczesnym\s+świecie\b",
    r"\bw\s+dobie\s+\w+",
    r"\bw\s+erze\s+\w+",
    r"\bw\s+epoce\s+\w+",
    r"\bw\s+czasach,?\s+(?:gdy|kiedy|w\s+których)\b",
    r"\bw\s+świecie,?\s+(?:w\s+którym|gdzie)\b",
    r"\bera\s+[^,.!?]{1,40}?\s+(?:dobiegła|dobiega)\s+końca\b",
    r"\bczasy\s+[^,.!?]{1,40}?\s+(?:minęły|się\s+skończyły|odeszły|dobiegły\s+końca)\b",
    r"\bodchodz\w*\s+(?:do\s+lamusa|w\s+zapomnienie|do\s+przeszłości)\b",
    r"\bnowa\s+era\b", r"\bnowy\s+rozdział\b", r"\bnowa\s+jakość\b", r"\bnowy\s+wymiar\b",
    r"\bprawdziw[aąey]\s+(?:rewolucj|przełom|skarb|sztuk)",
    r"(?<!prawdziwa )(?<!prawdziwą )\brewolucj[aeięą]\b", r"\brewolucyjn",
    r"\bprzełom\s+w\b", r"\bprzełomem\b",
    r"\bfundamentaln", r"\bradykaln", r"\bdiametraln", r"\bgruntownie\b",
    r"\bzmieni[ał]?\s+wszystko\b", r"\bzmienia\s+(?:reguły|zasady)\s+gry\b",
    r"\bna\s+zawsze\s+zmieni", r"\bzmienił\w*\s+świat\b",
    r"\bprzyszłość\s+należy\s+do\b", r"\bprzyszłość\s+zaczyna\s+się\b",
    r"\bto\s+coś\s+więcej\s+niż\b", r"\bto\s+więcej\s+niż\s+(?:tylko|zwykł[aey]|kolejn[aey]|sam[aoey])\b",
    r"\bnie\s+tylko\s+[^,.!?]{1,40}?,?\s+(?:ale|lecz)\s+(?:i|też|także|również|przede\s+wszystkim)\b",
    r"\btym,?\s+co\s+(?:nas\s+)?wyróżnia\b", r"\bco\s+wyróżnia\s+[^,.!?]{1,30}?,?\s+to\b",
    r"\bw\s+(?:stale|ciągle|dynamicznie|nieustannie)\s+(?:zmieniając|rozwijając|ewoluując)",
    r"\bprawda\s+jest\s+taka\b",
    r"\b(?:siła|magia|piękno|sekret|klucz|tajemnica|istota)\s+(?:tkwi|leży|polega)\b",
    r"\bjak\s+nigdy\s+(?:dotąd|wcześniej|przedtem)\b",
    r"\bna\s+wagę\s+złota\b", r"\bnie\s+do\s+przecenienia\b", r"\btrudno\s+przecenić\b",
    r"\b(?:jest|stanowi|to)\s+(?:najlepszym\s+)?dow[oó]d(?:em)?\s+na\b",
    r"\bświadczy\s+o\s+(?:jakości|profesjonalizmie|klasie|doświadczeniu)\b",
    r"\bwyznacza\w*\s+nowe\s+standardy\b",
    r"\bna\s+(?:zupełnie\s+)?(?:wyższy|nowy|inny)\s+poziom\b",
    r"\bkamień\s+(?:milowy|węgielny)\b",
    r"\bnic\s+nie\s+jest\s+w\s+stanie\b",
    r"\bbez\s+cienia\s+wątpliwości\b",
    r"\bw\s+ostatecznym\s+rozrachunku\b",
    r"\bto\s+(?:właśnie|dokładnie)\s+(?:dlatego|to,?\s+co)\b",
    r"\bi\s+to\s+(?:właśnie\s+)?(?:robi|czyni)\s+(?:całą\s+)?różnicę\b",
    r"\bsprawia,?\s+że\s+(?:wszystko|całość)\s+nabiera\b",
]

# D) Bureaucratese and filler connectors.
CLERICAL = [
    r"\bw\s+związku\s+z\s+(?:powyższym|tym)\b", r"\bwobec\s+powyższego\b",
    r"\btym\s+samym\b", r"\bwobec\s+tego\b",
    r"\bz\s+uwagi\s+na\b", r"\bze\s+względu\s+na\s+fakt\b", r"\bz\s+tego\s+względu\b",
    r"\bmając\s+na\s+uwadze\b", r"\bbiorąc\s+pod\s+uwagę\s+powyższe\b",
    r"\bw\s+świetle\s+powyższego\b", r"\bjak\s+wynika\s+z\s+powyższego\b",
    r"\bw\s+celu\b", r"\bcelem\s+\w+nia\b", r"\bw\s+zakresie\b",
    r"\bw\s+przypadku,?\s+gdy\b", r"\bw\s+sytuacji,?\s+gdy\b", r"\bw\s+razie\s+gdyby\b",
    r"\bw\s+kontekście\b", r"\bw\s+odniesieniu\s+do\b", r"\bw\s+stosunku\s+do\b",
    r"\bodnośnie\b", r"\bw\s+oparciu\s+o\b", r"\bz\s+punktu\s+widzenia\b",
    r"\bw\s+kwestii\b", r"\bw\s+tym\s+zakresie\b", r"\bw\s+tej\s+materii\b",
    r"\bniniejsz", r"(?<!z )\bpowyższ", r"\bwyżej\s+wymienion", r"\bww\.\s",
    r"\bjak\s+(?:już\s+)?wspomn(?:iano|iałem|ieliśmy|iałam)\b", r"\bjak\s+wyżej\b",
    r"\bponadto\b", r"\bco\s+więcej\b", r"\bdodatkowo,", r"\bniemniej\s+jednak\b",
    r"\bniemniej,", r"\bjednakże\b", r"\baczkolwiek\b", r"\bzatem\b", r"\btym\s+niemniej\b",
    r"\bw\s+rezultacie\b", r"\bw\s+konsekwencji\b", r"\bw\s+efekcie\s+czego\b",
    r"\bpodsumowując\b", r"\breasumując\b", r"\bw\s+podsumowaniu\b", r"\bkonkludując\b",
    r"\bna\s+zakończenie\b", r"\bna\s+koniec\s+warto\b",
    r"\bwarto\s+(?:zauważyć|podkreślić|zaznaczyć|wspomnieć|dodać|nadmienić|odnotować)\b",
    r"\bnależy\s+(?:zauważyć|podkreślić|zaznaczyć|pamiętać|dodać|wspomnieć|zwrócić\s+uwagę|mieć\s+na\s+uwadze)\b",
    r"\btrzeba\s+(?:podkreślić|zaznaczyć|przyznać)\b",
    r"\b(?:istotne|ważne|kluczowe|niezbędne|konieczne)\s+jest,?\s+(?:aby|by|żeby)\b",
    r"\b(?:istotnym|kluczowym|ważnym|niezbędnym|nieodzownym)\s+(?:aspektem|elementem|czynnikiem|zagadnieniem|krokiem)\b",
    r"\bodgrywa\w*\s+(?:kluczową|ważną|istotną|znaczącą|niebagatelną|ogromną)\s+rolę\b",
    r"\bstanowi\w*\s+(?:istotny|ważny|niezbędny)\s+(?:element|część|składnik)\b",
    r"\bnieodłączn", r"\bintegraln",
    r"\bz\s+jednej\s+strony\b.{1,120}?\bz\s+drugiej\s+(?:strony|zaś)\b",
    r"\bnie\s+sposób\s+(?:nie|pominąć|przecenić)\b", r"\bnie\s+bez\s+(?:znaczenia|powodu|przyczyny)\b",
    r"\bszereg\s+\w+", r"\bszerok[ai]\s+(?:wachlarz|gam[aę]|zakres|oferta|spektrum)\b",
    r"\bwachlarz\b", r"\bw\s+dużej\s+mierze\b", r"\bw\s+znacznym\s+stopniu\b",
    r"\bw\s+sposób\s+(?:znaczący|istotny|kompleksowy|profesjonalny|rzetelny|efektywny)\b",
    r"\bposiada(?:my|ć|ją|cie|sz)?\b",
    r"\bdokona\w*\s+(?:wyboru|zakupu|analizy|oceny|wymiany|przeglądu|naprawy|oględzin)\b",
    r"\bprzeprowadz\w*\s+(?:analiz|weryfikacj|ocen)",
    r"\bw\s+chwili\s+obecnej\b", r"\bna\s+dzień\s+dzisiejszy\b", r"\bna\s+chwilę\s+obecną\b",
    r"\bw\s+obecnej\s+chwili\b", r"\bw\s+obecnych\s+czasach\b",
    r"\bcechuje\s+się\b", r"\bcharakteryzuje\s+się\b",
    r"\bumożliwia\w*\b", r"\bzapewnia\w*\s+(?:pełn|komfort|bezpieczeństwo\s+i|najwyższ)",
    r"\bprzedmiotow", r"\brzeczon",
    r"\bw\s+głównej\s+mierze\b", r"\bjeśli\s+chodzi\s+o\b",
]

# E) Impersonal lecturing tone, hook lead-ins, template openers/closers and
#    guru-marketing markers (checklists/anti-ai.md sections 6-10).
IMPERSONAL = [
    # lecturing / meta
    r"\bw\s+(?:tym|niniejszym|dzisiejszym|poniższym)\s+(?:artykule|wpisie|poradniku|tekście|materiale|przewodniku)\b",
    r"\bdowie(?:sz|cie)\s+się\b", r"\bpozna(?:sz|cie)\s+(?:najważniejsze|najlepsze|sposoby|zasady)\b",
    r"\bprzyjrz(?:yjmy|ymy)\s+się\b", r"\bsprawdźmy\b", r"\bzobaczmy\b", r"\bspójrzmy\b",
    r"\bzacznijmy\b", r"\bprzejdźmy\s+do\b", r"\bomówimy\b", r"\bprzeanalizujmy\b",
    r"\bzanurz(?:my|yć|amy)\s+się\b", r"\bzagłęb(?:my|ić|iamy|imy)\s+się\b",
    r"\brozłóżmy\s+(?:to\s+)?na\s+czynniki\b",
    r"\b(?:a\s+teraz\s+)?wyobraź\s+sobie\b", r"\bpomyśl\s+o\s+tym\b", r"\bzastanów\s+się\b",
    r"\bczy\s+(?:kiedykolwiek\s+)?zastanawiał[ea]ś\s+się\b",
    r"\bczy\s+wiesz,?\s+że\b", r"\bczy\s+wiedział[ea]ś,?\s+że\b",
    r"\bbrzmi\s+znajomo\b", r"\bnie\s+jesteś\s+sam[a]?\b", r"\bnie\s+martw\s+się\b",
    r"\b(?:i\s+)?tu\s+(?:zaczyna|robi)\s+się\s+(?:ciekawie|najciekawsze|najważniejsze)\b",
    r"\b(?:i\s+)?tu\s+(?:pojawia|zaczyna)\s+się\s+(?:problem|pytanie|haczyk|sedno|schody|prawdziwa)\b",
    r"\bnajważniejsze\s+jest\s+to\b", r"\b(?:i\s+)?co\s+najważniejsze\b",
    r"\bco\s+(?:ciekawe|istotne|ważne|zabawne)\b",
    r"\bnaj(?:lepsze|ciekawsze|gorsze)\s+jest\s+to\b",
    r"\b(?:dobra|zła)\s+(?:wiadomość|informacja)\s+jest\s+taka\b",
    r"\bmam\s+dla\s+ciebie\s+(?:dobrą|złą)\s+wiadomość\b",
    r"\bczytaj\s+dalej\b", r"\bkontynuuj\s+czytanie\b", r"\bzostań\s+z\s+nami\b", r"\bbądź\s+na\s+bieżąco\b",
    r"\b(?:pod\s+koniec|na\s+końcu)\s+tego\s+(?:artykułu|wpisu|tekstu)\b",
    r"\bpo\s+przeczytaniu\s+(?:tego\s+)?(?:artykułu|wpisu|tekstu)\b",
    r"\bgotow[ya],?\s+(?:aby|by|żeby)\b", r"\bjesteś\s+gotow[ya]\s+na\b",
    r"\bpamiętaj,?\s+(?:że|aby|by|żeby)\b", r"\bmiej\s+na\s+uwadze\b", r"\bzwróć\s+uwagę,?\s+że\b",
    r"\bnie\s+zapom(?:inaj|nij)\b",
    r"\b(?:kluczowe|najważniejsze)\s+wnioski\b", r"\bw\s+skrócie:", r"\bkrótko\s+mówiąc\b",
    r"\binnymi\s+słowy\b", r"\bmówiąc\s+wprost\b",
    r"\bco\s+to\s+(?:oznacza|znaczy)\s+(?:dla\s+ciebie|w\s+praktyce)\b",
    r"\bdobrze\s+trafił[ea]ś\b", r"\bjesteś\s+we\s+właściwym\s+miejscu\b", r"\bnie\s+(?:musisz\s+)?szuka[jć]\s+dalej\b",
    # openers
    r"(?:^|\n)\s*(?:cześć|hej|witajcie|witam|dzień\s+dobry|siema|hello)\b[^.!?\n]{0,30}[!.,]",
    r"\bdrodzy\s+(?:czytelnicy|przyjaciele|państwo)\b", r"\bkochani\b", r"\bwitam\s+(?:serdecznie|wszystkich)\b",
    r"\bdzi(?:ś|siaj)\s+(?:opowiem|porozmawiamy|zajmiemy\s+się|chciał[a]?bym|przyjrzymy|pokażę)\b",
    r"\bchciał[a]?bym\s+(?:się\s+)?(?:z\s+wami\s+)?podzielić\b",
    # closers
    r"\bdzięk(?:uję|i|ujemy)\s+za\s+(?:uwagę|przeczytanie|lekturę|poświęcony\s+czas)\b",
    r"\bzaprasza(?:m|my)\s+do\s+(?:komentowania|dyskusji|komentarzy|śledzenia|subskrypcji|polubienia|udostępnienia|lektury)\b",
    r"\b(?:daj|dajcie)\s+znać\s+w\s+komentarz", r"\bnapisz\s+w\s+komentarz", r"\bzostaw\s+komentarz\b",
    r"\bpodziel\s+się\s+w\s+komentarz", r"\budostępnij\s+(?:ten\s+)?(?:artykuł|wpis|post)\b",
    r"\bdo\s+zobaczenia\b", r"\bdo\s+następnego\s+razu\b", r"\bdo\s+usłyszenia\b",
    r"\bma(?:m|my)\s+nadzieję,?\s+że\s+(?:ten|ta|to|artykuł|wpis|tekst|pomog|udało)\b",
    r"\btrzymaj(?:cie)?\s+się\b", r"\bpowodzenia!", r"\bto\s+(?:tyle|wszystko)\s+na\s+dzi(?:ś|siaj)\b",
    r"\bto\s+by\s+było\s+na\s+tyle\b", r"\bśledź\s+nas\b", r"\bobserwuj\s+nas\b",
    r"\bzapisz\s+się\s+(?:do|na)\s+newsletter",
    # guru-marketing
    r"\bgwarantuj(?:ę|emy|e|ą)\b", r"\bgwarantowan[yaąe]\s+(?:efekt|rezultat|sukces|wynik|zysk|skutecznoś)",
    r"\b(?:(?:zostało|pozostało|mamy)\s+)?tylko\s+\d+\s+(?:miejsc|wolnych)", r"\bostatnie\s+\d+\s+miejsc\b",
    r"\btylko\s+(?:dziś|dzisiaj|teraz|do\s+końca)\b", r"\bnie\s+przegap\b", r"\bnie\s+(?:czekaj|zwlekaj)\b",
    r"\bdziałaj\s+teraz\b",
    r"\bzanim\s+będzie\s+za\s+późno\b", r"\buda\s+ci\s+się\b", r"\bdasz\s+radę\b",
    r"\bwierz(?:ę|ymy)\s+w\s+ciebie\b", r"\bjesteś\s+w\s+stanie\b",
    r"\bstworzon[yae]\s+(?:specjalnie\s+)?(?:z\s+myślą\s+o|dla)\s+(?:ciebie|was|twoich)\b",
    r"\b(?:szyt[yae]|skrojon[yae])\s+na\s+miarę\b",
    r"\b(?:tajemnica|przepis|sekret|gwarancja)\s+sukcesu\b", r"\bodmieni\s+twoje\s+życie\b",
    r"\bzmieni\s+twoje\s+życie\b", r"\bbez\s+(?:wysiłku|ryzyka|stresu\s+i\s+nerwów)\b",
    r"\bnic\s+nie\s+tracisz\b", r"\bnie\s+masz\s+nic\s+do\s+stracenia\b",
    r"\bpasywn\w+\s+dochód\b", r"\bwolność\s+finansow", r"\boczywist[ya]\s+wyb[oó]r\b",
    r"\bcena\s+(?:idzie|pójdzie)\s+w\s+górę\b", r"\bcena\s+wzrośnie\b", r"\bpromocja\s+kończy\s+się\b",
    r"\bostatnia\s+szansa\b", r"\b(?:wyjątkow|niepowtarzaln|jedyn)[ae]\s+(?:w\s+swoim\s+rodzaju\s+)?okazj",
]

# LLM vocabulary tells: words and phrases a Polish LLM reaches for by default
# (calques of the English list plus native overused words).
LLM_VOCAB = [
    r"\bkluczow", r"\bkompleksow", r"\binnowacyjn", r"\bholistyczn",
    r"\bz?optymaliz", r"\bwykorzysta\w*\s+(?:pełn\w+\s+)?potencjał", r"\bw\s+pełni\s+potencjału\b",
    r"\bkrajobraz", r"\bekosystem", r"\bparadygmat", r"\bsynergi", r"\btransformacj", r"\bewoluuj",
    r"\b(?:ta|tej|tę|twoja|twojej|twoją|swoją|swojej|wasza|w\s+tej|na\s+tej)\s+podróż",
    r"\bpodróż\w*\s+(?:klienta|ku|w\s+stronę|do\s+(?:sukcesu|lepszego|celu))\b", r"\bwyrusz\w*\s+w\s+podróż",
    r"\bodblok\w*\s+(?:potencjał|możliwoś|pełn|nowe|nowy|swój|swoje|drzwi|dostęp\s+do\s+(?:nowych|pełnych))",
    r"\bbezproblemow", r"\bprzełomow", r"\bsolidn", r"\bdedykowan", r"\befektywn",
    r"\bdynamicznie\s+(?:rozwijając|zmieniając|rosnąc)", r"\bprężnie\s+(?:rozwijając|działając)",
    r"\bcyfrow[ea]j?\s+transformacj",
    r"\bnie\s+da\s+się\s+ukryć\b", r"\bnie\s+ma\s+co\s+ukrywać\b",
    r"\bbez\s+wątpienia\b", r"\bniewątpliwie\b", r"\bnie\s+ulega\s+wątpliwości\b", r"\bbezsprzecznie\b", r"\bbezdyskusyjnie\b",
    r"\bwarto\s+wiedzieć\b", r"\bkoniec\s+końców\b", r"\bostatecznie,", r"\bw\s+gruncie\s+rzeczy\b",
    r"\bbez\s+zbędnych\s+wstępów\b", r"\bprzejdźmy\s+do\s+rzeczy\b", r"\bnie\s+owijając\s+w\s+bawełnę\b",
    r"\bniezależnie\s+od\s+tego,?\s+czy\b", r"\bbez\s+względu\s+na\s+to,?\s+czy\b",
    r"\bnawigowa", r"\bporusza\w*\s+się\s+po\s+(?:krajobrazie|świecie|meandrach)\b", r"\bmeandr",
    r"\bwspiera\w*\s+(?:rozwój|w\s+osiąganiu|w\s+drodze\s+do)\b",
    r"\busprawni\w*\s+(?:procesy|proces|działanie|funkcjonowanie)\b",
    r"\bzwiększ\w*\s+(?:efektywność|wydajność|produktywność)\b",
    r"\bwszechstronn", r"\bwieloaspektow", r"\bwielowymiarow", r"\bwielopłaszczyznow",
    r"\bniezwykle\b", r"\bnieocenion", r"\bniebagateln",
    r"\bwisienk[aą]\s+na\s+torcie\b", r"\bprawdziw[ya]\s+skarb\b",
    r"\bsprawdzon[yea]\s+(?:sposób|sposoby|metod[aęy]|rozwiązani[ae]|receptur)",
    r"\bzarówno\s+[^,.!?]{1,40}?,\s+jak\s+i\b",
    r"\bpodnieś\w*\s+(?:komfort|jakość|poziom)",
    r"\bnowoczesn[ey]\s+(?:rozwiązani|technologi|podejści)",
    r"\bwyjątkow[eya]\s+(?:doświadczeni|przeżyci)", r"\bniezapomnian",
    r"\bzadba\w*\s+o\s+(?:każdy\s+szczegół|najdrobniejsze|najmniejsze)",
    r"\bszczególn[ąe]\s+uwagę\s+(?:przywiązuj|zwracaj|poświęc)",
]

# Empty Polish SME marketing words: a language model writing for a warsztat,
# szkoła jazdy or gabinet reaches for exactly these. Counted in category H.
MARKETING_CLICHE = [
    r"\bprofesjonaln", r"\bnajwyższ(?:a|ą|ej)\s+jakoś", r"\bna\s+najwyższym\s+poziomie\b",
    r"\bwysok(?:a|ą|iej)\s+jakoś", r"\bindywidualn[ea]\s+podejści", r"\bpodejści[ea]\s+do\s+(?:każdego\s+)?klienta\b",
    r"\bz\s+pasją\b", r"\bz\s+myślą\s+o\s+(?:tobie|was|kliencie|klientach|twoich)\b",
    r"\bwychodz\w*\s+naprzeciw\b", r"\bsprosta\w*\s+oczekiwani", r"\bspełni\w*\s+oczekiwani",
    r"\b(?:zadowolenie|satysfakcja)\s+(?:naszych\s+)?klient", r"\b(?:bogate|wieloletnie|długoletnie)\s+doświadczeni",
    r"\bszerok[ai]\s+ofert", r"\b(?:atrakcyjn|konkurencyjn)[ey]\s+cen", r"\b(?:nowoczesn|najnowocześniejsz)\w*\s+(?:sprzęt|park\s+maszynowy|urządzeni|wyposażeni)",
    r"\bwykwalifikowan", r"\bdoświadczon[ya]\s+(?:zespół|kadra|personel|specjaliś)",
    r"\bzespół\s+(?:profesjonalistów|specjalistów|ekspertów|pasjonatów)\b",
    r"\bbezpieczeństwo\s+i\s+komfort\b", r"\bkomfort\s+i\s+bezpieczeństwo\b",
    r"\bszybko\s+i\s+sprawnie\b", r"\bszybko,?\s+sprawnie\s+i\b", r"\bsprawnie\s+i\s+bezpiecznie\b",
    r"\brzeteln", r"\bterminow",
    r"\bpełn[ya]\s+(?:zakres|gam[aę]|profesjonalizm)",
    r"\bna\s+każdym\s+etapie\b", r"\bod\s+a\s+do\s+z\b",
    r"\bgodn[ya]\s+zaufania\b", r"\bzaufał[oy]\s+nam\b", r"\bzaufaj\s+(?:nam|specjalist|ekspert|doświadcz)",
    r"\bprzekonaj\s+się\s+sam", r"\bjuż\s+dziś\b",
    r"\bnasz[ay]m\s+(?:priorytetem|celem)\s+jest\b", r"\bstawiamy\s+na\b",
    r"\bkażdy\s+klient\s+jest\s+dla\s+nas\b", r"\btwoje\s+zadowolenie\b", r"\bpełn[ae]\s+satysfakcj",
]
LLM_VOCAB = LLM_VOCAB + MARKETING_CLICHE

# A) Antithesis. Inline forms are searched over the whole lowercased text.
#    "nie X, a Y" / "nie X, lecz Y" / "nie X, tylko Y" within ~45 characters.
#    ", ale" counts only in the "to nie X, ale Y" frame: a bare "nie ..., ale"
#    is the ordinary concession ("nie mogę w sobotę, ale w niedzielę tak").
#    "nie tylko X, ale i Y" is a flourish (LITERARY), not this.
ANTITHESIS_INLINE = [
    r"(?<![a-ząćęłńóśźż])nie\s+(?!tylko\b)[^,.!?:;]{1,45}?,\s+(?:a|lecz|tylko)\s+(?!i\b|też\b|także\b|również\b|przede\b)",
    r"\bto\s+nie\s+(?:tylko\s+|jest\s+)?[^,.!?:;]{1,45}?,\s+ale\s+(?!i\b|też\b|także\b|również\b|przede\b)",
    # same-sentence split: "to nie (tylko) X - to Y" / "nie chodzi o X, chodzi o Y"
    r"\bto\s+nie\s+(?:tylko\s+|jest\s+)?[^.!?,;-]{1,60}?(?:,|;|\s-)\s*to\s+(?!nie\b)",
    r"\bnie\s+chodzi\s+(?:tu\s+|tutaj\s+)?o\s+[^.!?]{1,60}?[,;]?\s+-?\s*(?:ale\s+|lecz\s+|tylko\s+|a\s+)?chodzi\s+o\b",
    r"\bnie\s+chodzi\s+(?:tu\s+|tutaj\s+)?o\s+to,?\s+(?:żeby|aby|by)\s+[^.!?]{1,60}?[,;]\s+(?:ale|lecz|tylko)\s+(?:o\s+to,?\s+)?(?:żeby|aby|by)\b",
    # trailing inversion in a LONG sentence: "... to partner, a nie dostawca."
    # (60+ characters before the comma; short sentences are ANTITHESIS_INVERSION's
    # job, so the two never count the same sentence twice)
    r"(?<=[^.!?]{60}),\s+a\s+nie\s+[^,.!?]{1,30}[.!?]",
    r"(?<=[^.!?]{60}),\s+nie\s+(?:na|w|we|z|ze|do|za|dla|o|po|przez|od|jako|tylko|jego|jej|ich|twoj\w*|swoj\w*|wasz\w*|nasz\w*|ten|ta|to|tego|tej|te|tych|tym|żaden|żadna|żadne)\b[^,.!?]{0,30}[.!?]",
]
# Split form across a sentence boundary: "To nie X. To Y." / "Nie chodzi o X. Chodzi o Y."
ANTITHESIS_S1 = [
    r"\bto\s+nie\s+(?:jest\s+)?(?!tak\b|prawda\b|wszystko\b|koniec\b|przypadek\b|znaczy\b|oznacza\b|zawsze\b|musi\b|ma\b|zależy\b|działa\b|pomaga\b|wystarczy\b|wina\b)\w",
    r"\bnie\s+chodzi\s+(?:tu\s+|tutaj\s+)?o\b",
    r"\bnie\s+jest\s+to\b",
    r"\bnie\s+o\s+to\s+(?:tu\s+)?chodzi\b",
]
ANTITHESIS_S2 = [
    r"^[\"'\-\s(]*(?:i\s+|a\s+|ale\s+|bo\s+)?(?:to\b|chodzi\s+o\b|liczy\s+się\b|ważn[ea]\s+jest\b|istotn[ea]\s+jest\b)",
]
# Sentence-initial inversion: a whole short sentence "X, a nie Y." / "X, nie Y."
ANTITHESIS_INVERSION = [
    r"^[\"'\-\s(]*(?!(?:tak|no|nie|niestety|cóż|ok|okej|owszem|jasne|dobrze|dobra|jeśli|jeżeli|gdy|kiedy|jak|skoro|choć|chociaż|mimo|bo|dopóki|zanim|póki|nawet|gdyby|jakby|im|kto|co|gdzie|dlaczego|czy|a|i|ale|więc|dlatego|jeżeli|żeby|aby)\b)[a-ząćęłńóśźż][^,.;:!?]{0,40},\s+(?:a\s+)?nie\s+(?!(?:więcej|mniej|wiem|wiemy|wcześniej|później|dłużej|krócej|zawsze|nigdy|od\s+razu|tylko|ma|mam|masz|musisz|trzeba|warto|da\s+się|było|jest|będzie|ma\s+co)\b)[^,.;:!?]{1,40}[.!?]*$",
]
# Semantic variants, reported in a separate sub-bucket.
ANTITHESIS_SEMANTIC = [
    r"\braczej\s+[^,.!?]{1,40}?\s+niż\b", r"\braczej\s+niż\b",
    r"\bmniej\s+(?:o|chodzi\s+o)\s+[^.!?]{1,60}?\bbardziej\s+(?:o\b|chodzi)",
    r"\bbardziej\s+(?:o|chodzi\s+o)\s+[^.!?]{1,60}?\bniż\s+o\b",
    r"\bnie\s+tyle\s+[^,.!?]{1,60}?,?\s+(?:ile|co)\b",
    r"\bzamiast\s+[^,.!?]{1,40}?,\s+(?:lepiej|warto|postaw|wybierz|zrób|pomyśl)\b",
    r"\bw\s+przeciwieństwie\s+do\b",
]

# ---------------------------------------------------------------------------
# read-aloud-check.py
# ---------------------------------------------------------------------------

VOWELS = "aeiouyąęó"

# Passive and impersonal forms (Polish has three ways to hide the doer):
#   1. zostać/być + participle: "został wymieniony", "jest realizowane",
#      "będą sprawdzone" (one adverb may sit in between: "został już wymieniony")
#   2. the -no/-to impersonal past: "wymieniono", "sprawdzono", "zamknięto"
#   3. "się" impersonal with a short list of typical verbs: "zaleca się",
#      "wykonuje się" (reflexive verbs like "opłaca się" are not listed)
_COPULA = (
    r"(?:jest|są|był|była|było|byli|były|będzie|będą|bywa|bywają|"
    r"został|została|zostało|zostali|zostały|zostanie|zostaną|zostać|zostając)"
)
_PARTICIPLE = (
    r"[a-ząćęłńóśźż]{3,}(?:an[yaei]|on[yaei]|en[yaei]|ęt[yaei]|ięt[yaei]|yt[yaei]|ut[yaei]|art[yaei]|ęci|eni|ani)"
)
_SIE_VERBS = (
    r"(?:zaleca|stosuje|uważa|przyjmuje|wykonuje|przeprowadza|dokonuje|realizuje|montuje|"
    r"wymienia|używa|powinno|mówi|twierdzi|zakłada|ustala|planuje|proponuje|rekomenduje|"
    r"sugeruje|podaje|szacuje|obserwuje|zauważa|stwierdza|oczekuje|wymaga|oferuje|"
    r"dostarcza|zapewnia|gwarantuje|udziela|prowadzi|obsługuje|naprawia|serwisuje|"
    r"przechowuje|magazynuje|składuje|kontroluje|sprawdza\s+się\s+stan)"
)
PASSIVE_RE = (
    r"\b" + _COPULA + r"\s+(?:(?:nie|już|jeszcze|zwykle|zawsze|często|też|także|również|"
    r"dopiero|właśnie|następnie|potem|wtedy|[a-ząćęłńóśźż]+ie)\s+)?" + _PARTICIPLE + r"\b"
    r"|\b[a-ząćęłńóśźż]{4,}(?:ano|ono|ęto|ięto|yto|uto)\b"
    r"|\b" + _SIE_VERBS + r"\s+się\b"
)
# Adjectives with participle-like endings that follow a copula in normal
# Polish ("jest zielony", "są zadowoleni") plus -no/-to nouns ("siano").
PASSIVE_EXCLUDE = {
    "zielony", "zielona", "zielone", "zieloni", "czerwony", "czerwona", "czerwone",
    "czerwoni", "słony", "słona", "słone", "szalony", "szalona", "szalone",
    "zmęczony", "zmęczona", "zmęczone", "zmęczeni", "zadowolony", "zadowolona",
    "zadowolone", "zadowoleni", "spragniony", "przekonany", "przekonana",
    "przekonani", "zaskoczony", "zaskoczona", "zaskoczeni", "zdziwiony",
    "zdziwiona", "drewniany", "drewniana", "drewniane", "szklany", "szklana",
    "szklane", "blaszany", "blaszana", "blaszane", "wełniany", "lniany",
    "gliniany", "srebrny", "otwarty", "otwarta", "otwarte", "zamknięty",
    "zamknięta", "zamknięte", "żółty", "żółta", "żółte", "złoty", "złota",
    "złote", "bogaty", "bogata", "bogate", "prosty", "prosta", "proste",
    "czysty", "czysta", "czyste", "pusty", "pusta", "puste", "gęsty", "gęsta",
    "gęste", "tłusty", "tłusta", "tłuste", "święty", "święta", "święte",
    "gotowy", "gotowa", "gotowe", "gotowi", "znany", "znana", "znane", "znani",
    "tani", "tania", "tanie", "sam", "sami", "pewny", "pewna", "pewne", "pewni",
    "ważny", "ważna", "ważne", "ciepły", "ciepła", "ciepłe", "zimny", "zimna",
    "zimne", "ciemny", "ciemna", "ciemne", "równy", "równa", "równe",
    "właściwy", "właściwa", "właściwe", "podobny", "podobna", "podobne",
    "podobni", "wolny", "wolna", "wolne", "wolni", "kolano", "siano", "rano",
    "grono", "łono", "auto", "żyto", "koryto", "kimono", "domino", "wino",
    "piano", "konto", "tempo", "lotto", "brutto", "netto", "dobrze", "trzeba",
    "sami", "same", "samo", "ostatni", "ostatnia", "ostatnie", "obecni",
    "obecna", "obecne", "obecny", "nieobecni", "uparty", "uparta", "uparte",
    "napięty", "napięta", "napięte", "spięty", "spięta", "spięte", "zajęty",
    "zajęta", "zajęte", "zajęci", "wyjęty", "ukryty", "ukryta", "ukryte",
    # nouns that happen to end like a participle: "są zmiany", "jest wymiana"
    "zmiana", "zmiany", "wymiana", "wymiany", "ściana", "ściany", "strona",
    "strony", "ochrona", "ochrony", "membrana", "membrany", "zasłona",
    "zasłony", "dywany", "korona", "brama", "rama", "ramy", "plany", "plamy",
    "opony", "opona", "sezony", "salony", "zagony", "wagony", "balony",
    "kolumny", "rośliny", "godziny", "dziewczyny", "maszyny", "kabiny",
}

# Nominalisations: -anie/-enie (verbal nouns), -ość, -cja, -izm, 8+ letters,
# all case endings. The exclusion regex below (prefix stems, any ending) skips
# concrete everyday nouns ("mieszkanie", "jakość") and the trade nouns of the
# target niches (zawieszenie, ogumienie, ćwiczenia, hydroizolacja) so only
# real process nominalisations (składowanie, przetwarzanie) are counted.
NOMINAL_RE = (
    r"\b[a-ząćęłńóśźż]{4,}(?:ani[eau]|aniem|aniach|aniom|eni[eau]|eniem|eniach|eniom|"
    r"ość|ości|ością|ościach|ościom|cj[aięą]|cjach|cjom|izm|izmu|izmie|izmy|izmów|izmach)\b"
)
NOMINAL_EXCLUDE = set()
NOMINAL_EXCLUDE_RE = (
    r"(?:mieszk|zd|pyt|zad|spotk|zebr|śniad|ubr|wyd|obic|szkl|karm|ubezpiecz|"
    r"jedz|picie|życie|ziemi|zdjęc|przyjęc|zajęc|pojęc|wejśc|wyjśc|przejśc|dojśc|"
    r"życ|szycie|myc|bic|pic|cięc|tyci|wycie|"
    r"pomieszcz|urządz|narzędz|nasion|nasien|kamien|ramien|imien|plemien|marz|"
    r"znacz|doświadcz|zamówi|zaprosz|połącz|ustawi|szkol|badani|lecz|"
    r"zawiesz|ogumi|oświetl|chłodz|ogrzew|wyposaż|uszczelni|zasil|sterow|"
    r"ćwicz|ruchom|obciąż|przeciąż|odciąż|aktywn|sprawn|"
    r"ciśni|prędk|wysok|szerok|długo|głębok|wilgot|twardo|ostro|jasno|ciemno|"
    r"jak|wart|całoś|rzeczywist|przyszł|przeszł|młod|staro|wol|rad|mił|nowo|"
    r"nieruchom|własn|możliw|odległ|szybk|wielk|ilo|"
    r"inform|stac|polic|akc|porc|recepc|kolac|operac|instalac|hydroizolac|"
    r"stabilizac|aplikac|rezerwac|lokaliz|wentyl|rejestrac|konsultac|amortyz|"
    r"geometr|diagnost|reklamac|gwaranc|dokumentac|specyfikac|kolekc|kondyc|"
    r"nawigac|pozyc|sekc|opc|lekc|dekorac|izolac|klimatyzac|racj|"
    r"fizjoter|rehabilit|reanim|inhal|"
    r"mechanizm|organizm|egoizm|turyst|kapital|realizm)"
    r"[a-ząćęłńóśźż]*"
)

# Stacked prepositions: count these in one sentence. Polish prepositions are
# short and frequent, so the pack raises the per-sentence threshold to 5.
STACK_PREPS = {"w", "we", "na", "do", "z", "ze", "od", "przy", "dla", "o", "po", "u", "przez", "za", "pod", "nad", "bez"}
STACK_PREPS_LABEL = "w/na/do/z/od/przy/dla/o/po/przez"
NOMINAL_LABEL = "-anie/-enie/-ość/-cja/-izm"

NUMBER_STOPWORDS = {
    "i", "a", "ale", "w", "we", "na", "do", "z", "ze", "od", "o", "po", "to",
    "jest", "są", "że", "się", "nie", "tak", "jak", "ten", "ta", "te", "ich",
    "go", "ją", "u", "za", "przy", "dla", "bez", "lub", "albo", "oraz", "czy",
    "bo", "by", "już", "też", "tylko", "nawet", "aż", "niż", "co", "tym", "tego",
}
NUMBER_UNITS = {
    "%", "proc", "proc.", "procent", "minut", "minuty", "minutę", "min", "min.",
    "godzin", "godziny", "godzinę", "godz", "godz.", "h", "dni", "dzień", "dnia",
    "tygodni", "tygodnie", "tydzień", "tyg", "tyg.", "miesięcy", "miesiące",
    "miesiąc", "mies", "mies.", "lat", "lata", "rok", "roku", "sezony", "sezonów",
    "sezon", "sekund", "sekundy", "sek", "sek.", "s", "km", "m", "cm", "mm", "kg",
    "g", "l", "ml", "t", "zł", "zl", "pln", "eur", "euro", "usd", "gr", "grosze",
    "groszy", "złotych", "złote", "tys", "tys.", "mln", "mld", "osób", "osoby",
    "osobę", "klientów", "klienci", "aut", "auta", "auto", "samochodów",
    "samochody", "sztuk", "szt", "szt.", "razy", "raz", "razem", "punktów",
    "punkty", "stron", "strony", "słów", "słowa", "km/h", "kw", "km", "hp", "obr",
    "obr.", "obr/min", "psi", "bar", "bary", "barów", "atm", "stopni", "stopnie",
    "st", "st.", "c", "mb", "gb", "kb", "x", "kroki", "kroków", "krok", "opon",
    "opony", "koła", "kół", "komplety", "komplet", "kompletów", "wizyt",
    "wizyty", "wizyta", "zabiegów", "zabiegi", "zabieg", "lekcji", "lekcje",
    "jazd", "jazdy", "prób", "pokoi", "pokoje", "łazienek", "m2", "m²", "mkw",
    "mb", "sztuki", "egzemplarzy", "warstwy", "warstw", "litrów", "litry", "litr",
    "tysięcy", "tysiące", "tysiąc", "milionów", "miliony", "milion",
}
NUMBER_PREFIX_WORDS = {
    "krok", "strona", "str", "str.", "rozdział", "część", "nr", "nr.", "numer",
    "punkt", "pkt", "pkt.", "tabela", "rysunek", "rys", "rys.", "wersja", "od",
    "do", "w", "we", "roku", "r", "r.", "etap", "lekcja", "dzień", "tydzień",
    "poziom", "piętro", "lok", "lok.", "m", "m.", "ul", "ul.", "al", "al.",
    "tel", "tel.", "kod", "sala", "pokój", "trasa", "linia", "faza", "runda",
    "seria", "grupa", "klasa", "kategoria", "kat", "kat.", "art", "art.", "ust",
    "ust.", "par", "par.", "poz", "poz.", "id", "godz", "godz.", "godzina",
    "około", "ok", "ok.", "ponad", "prawie", "niecałe", "przez", "co", "po",
}
CURRENCY_MARKS = ("zł", "zl", "pln", "eur", "€", "$", "usd")

# Polish digraphs are one sound: collapsed to a single consonant before the
# run count, so "przestrzeń" is p-rz-e-s-t-rz-e-ń, not a 4-consonant pile-up.
# Order matters: three-letter and dotted forms first.
CONSONANT_DIGRAPHS = ("dź", "dż", "dz", "sz", "cz", "rz", "ch")

# Words that still trip the counter after the digraph collapse (a legitimate
# 5-6 consonant run), plus the classic tongue-twisters that are real words.
HARD_TO_SAY_ALLOW = {
    "pierwszy", "pierwsza", "pierwsze", "pierwszych", "pierwszym", "wszystko",
    "wszystkich", "wszystkie", "wszystkim", "wszyscy", "bezwzględnie",
    "bezwzględny", "bezwzględna", "bezwzględne", "względnie", "względny",
    "względna", "względne", "względem", "przestrzeń", "przestrzeni",
    "chrząszcz", "chrząszcza", "źdźbło", "źdźbła", "pstrąg", "pstrągi",
    "złotówka", "wstrząs", "wstrząsy", "wstrząsów", "zmartwychwstanie",
    "przestępstwo", "mistrz", "mistrza", "mistrzowie", "krnąbrny",
    "nadwzroczność", "wzgląd", "względu", "wzgórze", "wzgórza", "wzbudza",
    "wzbudzać", "wzmocnić", "wzmocnienie", "wzmocniony", "wzmacniacz",
    "trzmiel", "źrebak", "źrebię", "drgnąć", "drgnięcie", "drgania",
    "drgań", "strząsnąć", "wstrzymać", "wstrzymanie", "wstrzykiwacz",
    "wstrzykiwacze", "wstrzykiwaczy", "wstrząsnąć", "przestrzegać",
    "przestrzeganie", "rozstrzygnąć", "rozstrzygnięcie", "tkwi", "tkwić",
    "krwi", "krwią", "brwi", "trwa", "trwać", "trwały", "trwałe", "trwała",
    "trwałość", "trwałości", "trwania", "drwal", "drzwi", "drzwiach",
    "mgły", "mgła", "łgarstwo", "łgarstwa", "mnóstwo", "mnóstwa",
    "państwo", "państwa", "państwu", "szczęście", "szczęścia", "szczęśliwy",
    "szczęśliwa", "szczęśliwe", "rzemieślnik", "rzemieślnicy", "sprzęgło",
    "sprzęgła", "sprzęgle", "wtrysk", "wtrysku", "wtryskiwacz", "wtryskiwacze",
    "wtryskiwaczy", "wtryskowy", "wtryskowa", "wtryskowe", "wtryskowego",
    "wtryskowej",
}

# Per-language read-aloud defaults (CLI flag and config.yaml still win).
THRESHOLD_DEFAULTS = {
    "max_word_len": 20,        # Polish words carry case endings; 17 flags ordinary words
    "max_consonant_run": 6,    # after the digraph collapse, 5 still hits "bezwzględny"
    "max_stacked_preps": 5,    # w/na/do/z are one letter and everywhere
}
