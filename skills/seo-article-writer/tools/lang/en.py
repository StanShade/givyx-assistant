#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lang/en.py - English pattern pack for ai-cadence-check.py and read-aloud-check.py.

All regexes run against LOWERCASED text. Keep patterns as raw strings. Add new
AI tells here (not in the tools) when Stage 15 or Stage 16 finds one that slipped
through; the methodology tells you to log them in checklists/anti-ai.md as well.

Calibrated against tools/tests/fixture-ai-en.md and fixture-human-en.md.
"""

NAME = "English"
CALIBRATED = True

# Word token for counting words and sentence lengths.
WORD_RE = r"[A-Za-z][A-Za-z'\-]*"
LETTER_CLASS = "a-z"

# Abbreviations after which a full stop does not end a sentence. Kept empty on
# purpose: the English fixtures were calibrated with the plain splitter.
ABBREVIATIONS = set()

# ---------------------------------------------------------------------------
# ai-cadence-check.py
# ---------------------------------------------------------------------------

# Function-word starts. Two consecutive sentences starting with one of these
# are normal English, not an AI parallelism, so category G ignores them.
CONNECTOR_STARTS = {
    "a", "an", "the", "and", "but", "or", "so", "if", "when", "then", "now",
    "i", "we", "you", "he", "she", "it", "they", "this", "that", "these", "those",
    "there", "here", "in", "on", "at", "for", "to", "of", "by", "with", "from",
    "as", "is", "are", "was", "were", "do", "does", "did", "can", "could", "will",
    "would", "should", "may", "might", "not", "no", "yes", "also", "still",
    "just", "because", "what", "which", "who", "how", "why", "where", "my",
    "your", "our", "its", "their", "one", "some", "most", "many", "all", "each",
    "every", "both", "let", "don't", "i'm", "it's", "that's", "there's", "he's",
    "she's", "we're", "you're", "they're", "after", "before", "once", "while",
    "another", "any", "even", "first", "second", "third", "last", "next",
}

# Short one-word sentences that are normal spoken English, not AI staccato.
ALLOWED_SHORT = {
    "yes", "no", "right", "exactly", "sure", "okay", "ok", "fine", "true",
    "wrong", "why", "how", "really", "almost", "maybe", "sometimes", "first",
    "second", "third", "example", "summary", "again", "anyway", "nope", "yep",
    "done", "enough", "nothing", "everything", "nobody", "period", "seriously",
    "honestly", "sorry", "thanks", "wait", "look", "listen", "note", "either",
    "neither", "whatever", "obviously", "usually", "often", "rarely", "never",
    "always", "sadly", "luckily", "correct", "incorrect", "worse", "better",
}

# C) Literary flourishes and grandiose phrasing.
LITERARY = [
    r"\b(?:the\s+)?(?:era|age|days?)\s+of\s+(?:\w+\s+){1,3}(?:is|are)\s+over\b",
    r"\ba\s+new\s+(?:era|age|dawn|chapter)\b",
    r"\bin\s+a\s+world\s+where\b",
    r"\bin\s+an?\s+(?:era|age)\s+(?:of|where|when)\b",
    r"\bnothing\s+short\s+of\b",
    r"\b(?:true|real|genuine)\s+revolution\b",
    r"\brevolutioni[sz](?:e|es|ed|ing)\b",
    r"\bfundamentally\b", r"\bradically\b", r"\bprofoundly\b",
    r"\bparadigm\s+shift\b",
    r"\bthe\s+future\s+belongs\s+to\b",
    r"\bchanges?\s+everything\b",
    r"\bforever\s+chang(?:e|ed|es)\b",
    r"\bchanged\s+the\s+world\b",
    r"\bthe\s+truth\s+is\b",
    r"\bat\s+its\s+(?:very\s+)?core\b",
    r"\bmore\s+than\s+just\s+an?\b",
    r"\bin\s+the\s+grand\s+scheme\b",
    r"\ba\s+(?:powerful|stark|sobering)\s+reminder\b",
    r"\bstands?\s+as\s+an?\b",
    r"\bserves?\s+as\s+an?\s+(?:testament|reminder|beacon|cornerstone)\b",
    r"\bbeacon\s+of\b", r"\bcornerstone\s+of\b",
    r"\bthe\s+(?:power|magic|beauty)\s+of\b",
    r"\bnot\s+only\s+.{1,40}?\bbut\s+also\b",
    r"\bwhat\s+sets\s+.{1,30}?\bapart\b",
    r"\bin\s+the\s+ever[\s-]+(?:changing|evolving)\b",
    r"\bever[\s-]+(?:changing|evolving|growing)\b",
]

# D) Bureaucratese and filler connectors.
CLERICAL = [
    r"(?:^|[.!?]\s+)however,",
    r"\bthus\b", r"\bhence\b", r"\btherefore,",
    r"\bas\s+(?:mentioned|noted|stated|discussed)\s+(?:above|earlier|previously|before)\b",
    r"\baforementioned\b",
    r"\bin\s+addition,",
    r"\bin\s+summary\b", r"\bto\s+sum\s+up\b", r"\ball\s+in\s+all\b",
    r"\bin\s+today'?s\s+(?:world|digital\s+age|market|economy|society)\b",
    r"\bin\s+the\s+modern\s+world\b",
    r"\bplays?\s+an?\s+(?:key|crucial|vital|important|pivotal|significant|central)\s+(?:role|part)\b",
    r"\b(?:an?\s+)?integral\s+part\s+of\b",
    r"\bon\s+the\s+one\s+hand\b.{1,120}?\bon\s+the\s+other\s+hand\b",
    r"\bit\s+should\s+be\s+noted\b",
    r"\bit\s+goes\s+without\s+saying\b", r"\bneedless\s+to\s+say\b",
    r"\b(?:with\s+)?that\s+(?:being\s+)?said,",
    r"\bin\s+order\s+to\b",
    r"\bdue\s+to\s+the\s+fact\s+that\b",
    r"\bfor\s+the\s+purpose\s+of\b",
    r"\bin\s+the\s+event\s+that\b",
    r"\ba\s+wide\s+(?:range|variety|array)\s+of\b",
    r"\ba\s+(?:variety|myriad|plethora|multitude)\s+of\b",
    r"\bin\s+terms\s+of\b",
    r"\bwhen\s+it\s+comes\s+to\b",
    r"\bit\s+is\s+(?:essential|imperative|vital|critical)\s+(?:to|that)\b",
    r"\bensur(?:e|es|ing)\s+that\b",
    r"\bfacilitat(?:e|es|ed|ing)\b",
    r"\butili[sz](?:e|es|ed|ing)\b",
    r"\bprior\s+to\b",
    r"\bsubsequently\b",
    r"\bin\s+conjunction\s+with\b",
    r"\bwith\s+regard\s+to\b", r"\bin\s+regard\s+to\b",
    r"\bit\s+is\s+(?:clear|evident|apparent)\s+that\b",
]

# E) Impersonal lecturing tone and hook lead-ins.
IMPERSONAL = [
    r"\bin\s+this\s+(?:article|guide|post|piece|blog\s+post)\b",
    r"\byou(?:'ll|\s+will)\s+(?:learn|discover|find\s+out)\b",
    r"\bwe(?:'ll|\s+will)\s+(?:explore|cover|walk\s+you\s+through|break\s+down|take\s+a\s+look)\b",
    r"\blet'?s\s+(?:explore|break\s+(?:it|this)\s+down|get\s+started|take\s+a\s+(?:closer\s+)?look|begin|unpack)\b",
    r"\bkeep\s+reading\b", r"\bread\s+on\b", r"\bstay\s+tuned\b",
    r"\b(?:now\s+)?imagine\s+(?:this|that|a|if)\b", r"\bpicture\s+this\b",
    r"\bthink\s+about\s+it\b",
    r"\b(?:the\s+)?key\s+takeaways?\b",
    r"\bthanks\s+for\s+reading\b",
    r"\bwe\s+hope\s+(?:this|you)\b", r"\bhope\s+this\s+helps\b",
    r"\bnow\s+you\s+know\b",
    r"\bby\s+the\s+end\s+of\s+this\b",
    r"\blook\s+no\s+further\b",
    r"\byou\s+(?:might|may)\s+be\s+wondering\b",
    r"\byou'?re\s+not\s+alone\b",
    r"\bsounds?\s+familiar\b",
    r"\b(?:have\s+you\s+)?ever\s+wondered\b",
    r"\bhave\s+you\s+ever\b",
    r"\bone\s+thing\s+is\s+(?:certain|clear)\b",
    r"\bmake\s+no\s+mistake\b",
    r"\bspoiler\s+alert\b",
    r"\bthe\s+(?:good|bad)\s+news\s+is\b",
    r"\bso,?\s+what\s+does\s+this\s+mean\b",
    r"\bwhat\s+does\s+(?:this|that|it)\s+mean\s+for\s+you\b",
    r"\bready\s+to\s+(?:get\s+started|take|transform|level\s+up)\b",
    r"\bthe\s+(?:most\s+)?(?:important|interesting|powerful)\s+(?:part|thing|bit)\s+is\b",
]

# LLM vocabulary tells: single words and fixed phrases an English LLM overuses.
LLM_VOCAB = [
    r"\bdelv(?:e|es|ed|ing)\b",
    r"\bleverag(?:e|es|ed|ing)\b",
    r"\brobust(?:ly|ness)?\b",
    r"\bcomprehensive(?:ly)?\b",
    r"\btapestr(?:y|ies)\b",
    r"\blandscapes?\b",
    r"\bjourneys?\b",
    r"\brealms?\b",
    r"\bnavigat(?:e|es|ed|ing)\b",
    r"\bunlock(?:s|ed|ing)?\b",
    r"\belevat(?:e|es|ed|ing)\b",
    r"\bseamless(?:ly)?\b",
    r"\bgame[\s-]?changer(?:s)?\b", r"\bgame[\s-]?changing\b",
    r"\btestament\b",
    r"\bpivotal\b",
    r"\bcrucial(?:ly)?\b",
    r"\bvibrant\b",
    r"\bfoster(?:s|ed|ing)?\b",
    r"\bharness(?:es|ed|ing)?\b",
    r"\bembark(?:s|ed|ing)?\b",
    r"\bunderscor(?:e|es|ed|ing)\b",
    r"\bin\s+today'?s\s+fast[\s-]+paced\s+(?:world|environment|era|market)\b",
    r"\bit'?s\s+worth\s+(?:noting|mentioning)\b", r"\bit\s+is\s+worth\s+(?:noting|mentioning)\b",
    r"\bit'?s\s+important\s+to\s+(?:note|remember|understand)\b",
    r"\bit\s+is\s+important\s+to\s+(?:note|remember|understand)\b",
    r"\bat\s+the\s+end\s+of\s+the\s+day\b",
    r"\bthe\s+bottom\s+line\b",
    r"\bwithout\s+further\s+ado\b",
    r"\blet'?s\s+dive\s+(?:in|into|deeper|right\s+in)\b",
    r"\bin\s+conclusion\b",
    r"\bmoreover\b", r"\bfurthermore\b", r"\badditionally\b",
    r"\bultimately\b", r"\bnotably\b",
    r"\bwhether\s+you'?re\b",
    r"\bhere'?s\s+the\s+thing\b",
    r"\b(?:and\s+)?the\s+best\s+part\b",
]

# A) Antithesis. Inline forms are searched over the whole lowercased text.
#    "not X, but Y" / "not X but Y" within ~45 characters.
ANTITHESIS_INLINE = [
    r"(?<![a-z])(?:not|isn't|aren't|wasn't|weren't|doesn't|don't|never)\s+[^,.!?:;]{1,45}?,?\s+but\s+(?!also\b)",
    # same-sentence split form: "It's not (just) about X - it's about Y" / "isn't X, it's Y"
    r"\b(?:it|this|that)(?:'s|\s+is)\s+not\s+(?:just\s+|only\s+|simply\s+)?[^.!?]{1,60}?[,;]?\s+-?\s*(?:it|this|that)(?:'s|\s+is)\s+",
    r"\b(?:it|this|that)\s+isn't\s+(?:just\s+|only\s+|simply\s+)?[^.!?]{1,60}?[,;]?\s+-?\s*(?:it|this|that)(?:'s|\s+is)\s+",
    # trailing inversion: "... is a partner, not a vendor."
    r",\s+not\s+(?:a|an|the|just|your|some|more)\s+[^,.!?]{1,30}[.!?]",
]
# Split form across a sentence boundary: S1 carries a negated copula, S2 opens
# with the same subject again. "It's not X. It's Y." / "It isn't about X. It's about Y."
ANTITHESIS_S1 = [
    r"\b(?:it|this|that|he|she|there)(?:'s|\s+is|\s+isn't|\s+is\s+not|\s+was|\s+wasn't)\s+not\b",
    r"\b(?:it|this|that|he|she|there)\s+(?:isn't|wasn't|is\s+not|was\s+not)\b",
    r"\b(?:it|this|that)\s+(?:isn't|is\s+not|wasn't)\s+about\b",
]
ANTITHESIS_S2 = [
    r"^[\"'\-\s(]*(?:and\s+|but\s+)?(?:it|this|that|he|she|there)(?:'s|\s+is|\s+was)\b",
]
# Sentence-initial inversion: a whole short sentence of the form "X, not Y."
ANTITHESIS_INVERSION = [
    r"^[\"'\-\s(]*[a-z][^,.;:!?]{0,40},\s+not\s+[^,.;:!?]{1,40}[.!?]*$",
]
# Semantic variants, reported in a separate sub-bucket.
ANTITHESIS_SEMANTIC = [
    r"\brather\s+than\b",
    r"\bless\s+about\s+.{1,60}?\bmore\s+about\b",
    r"\bit'?s\s+less\s+about\b",
]

# ---------------------------------------------------------------------------
# read-aloud-check.py
# ---------------------------------------------------------------------------

VOWELS = "aeiouy"

# Crude passive voice: be-verb (+ optional adverb) + past participle.
_IRREGULAR_PP = (
    "built|made|done|seen|known|given|taken|found|held|kept|left|lost|paid|put|"
    "read|sent|set|shown|sold|told|thought|understood|won|written|brought|bought|"
    "caught|taught|felt|dealt|meant|led|fed|said|heard|met|cut|hit|hurt|spent|"
    "lent|bent|spread|shut|let|run|begun|sung|driven|ridden|risen|chosen|frozen|"
    "spoken|broken|stolen|woken|forgotten|gotten|hidden|bitten|beaten|eaten|"
    "fallen|drawn|grown|thrown|flown|blown|worn|torn|sworn|born|born|sought|"
    "fought|struck|stuck|swung|hung|laid|slid|split|cast|quit|shed|bound|wound|"
    "ground|overcome|undertaken|withdrawn"
)
PASSIVE_RE = (
    r"\b(?:is|are|was|were|be|been|being|am)\s+(?:(?:not|never|also|often|"
    r"usually|always|still|then|now|[a-z]+ly)\s+)?(?:[a-z]{2,}ed|" + _IRREGULAR_PP + r")\b"
)
# Words that end in -ed but are not participles; skip when they follow a be-verb.
PASSIVE_EXCLUDE = {
    "indeed", "need", "speed", "feed", "seed", "exceed", "proceed", "succeed",
    "hundred", "naked", "wicked", "sacred", "wretched", "red", "bed", "shed",
    "greed", "agreed", "freed", "breed", "bleed", "deed", "weed", "reed",
    "used",  # "is used to" (habit) is idiomatic; the passive "is used for" is fine to keep
    "supposed", "allowed",  # "is supposed to", "is allowed to": modal idioms
}

# Nominalisations: -tion/-sion/-ment/-ness/-ity/-ance/-ence, 7+ letters.
NOMINAL_RE = r"\b[a-z]{3,}(?:tion|sion|ment|ness|ity|ance|ence)s?\b"
NOMINAL_EXCLUDE = {
    "question", "questions", "mention", "position", "positions", "station", "stations",
    "moment", "moments", "comment", "comments", "document", "documents", "payment",
    "payments", "apartment", "apartments", "city", "cities", "business", "businesses",
    "witness", "distance", "distances", "chance", "chances", "science", "audience",
    "experience", "experiences", "sentence", "sentences", "fitness", "illness",
    "section", "sections", "option", "options", "condition", "conditions",
    "location", "locations", "equipment", "government", "quality", "security",
    "community", "communities", "attention", "election", "elections", "appointment",
    "appointments", "insurance", "entrance", "silence", "sentence", "ambulance",
}

# Stacked prepositional phrases: count these in one sentence.
STACK_PREPS = {"of", "in", "for", "with", "to"}

# Bare numbers. A number is "bare" when neither of the next two tokens is a
# unit or a content word, and it carries no currency / percent mark itself.
NUMBER_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for",
    "with", "by", "from", "is", "are", "was", "were", "be", "that", "this", "it",
    "as", "so", "if", "than", "then", "not", "its", "it's", "them", "there",
}
NUMBER_UNITS = {
    "%", "percent", "per", "pct", "minutes", "minute", "min", "mins", "hours",
    "hour", "hrs", "hr", "days", "day", "weeks", "week", "months", "month",
    "years", "year", "yrs", "seconds", "second", "sec", "secs", "ms", "km",
    "miles", "mile", "mm", "cm", "m", "kg", "g", "lb", "lbs", "oz", "mph",
    "kph", "kmh", "zl", "pln", "usd", "eur", "gbp", "dollars", "dollar",
    "euros", "euro", "cents", "cent", "bucks", "x", "times", "gb", "mb", "kb",
    "tb", "px", "pages", "page", "words", "word", "people", "customers",
    "clients", "cars", "items", "steps", "step", "points", "point", "pcs",
    "units", "unit", "degrees", "deg", "liters", "litres", "l", "ml", "psi",
    "hp", "kw", "rpm", "mpg", "sq", "sqm", "sqft", "ft", "in", "inches", "inch",
    "am", "pm", "a.m.", "p.m.", "k", "m", "bn", "mn",
}
# A number right after one of these is an identifier, not a quantity.
NUMBER_PREFIX_WORDS = {
    "step", "page", "chapter", "part", "no", "no.", "number", "#", "tip", "rule",
    "section", "figure", "fig", "fig.", "table", "item", "day", "week", "phase",
    "version", "v", "route", "highway", "room", "floor", "level", "grade",
    "since", "in", "from", "until", "till", "by",  # dates: "since 2019"
}
CURRENCY_MARKS = ("$", "zl", "pln", "usd", "eur", "gbp", "\u00a3", "\u20ac")

# English has no digraphs that should count as one consonant; the run counter
# looks at letters. Thresholds are the tool defaults.
CONSONANT_DIGRAPHS = ()
NOMINAL_EXCLUDE_RE = r"(?!x)x"
NOMINAL_LABEL = "-tion/-ment/-ness/-ity"
STACK_PREPS_LABEL = "of/in/for/with/to"
THRESHOLD_DEFAULTS = {}

# Hard-to-say words: 5+ consonants in a row, except these common ones.
HARD_TO_SAY_ALLOW = {
    "strengths", "strength", "lengths", "length", "twelfth", "twelfths",
    "nightclub", "nightclubs", "thoughtful", "thoughtfully", "brightness",
    "lightbulb", "birthplace", "watchstrap", "worthwhile", "northstar",
    "eighths", "hundredths", "thousandths", "months", "widths", "depths",
    "catchphrase", "matchstick", "matchsticks", "toothbrush", "toothbrushes",
    "birthstone", "sixths", "fifths", "warmths", "kirschwasser",
}
