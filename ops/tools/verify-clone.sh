#!/usr/bin/env bash
# Independent post-build check of one prospect clone: title, robots meta, robots.txt, template leaks
# across all 8 PL pages, tel: hrefs, rating row. usage: verify-clone.sh <slug> [pl|en]
set -uo pipefail
S="${1:?slug}"; L="${2:-pl}"
if [ "$L" = "pl" ]; then PAGES=("" uslugi umow-wizyte faq o-warsztacie kontakt polityka-prywatnosci regulamin); ABOUT=o-warsztacie
else PAGES=("" services book about contact privacy-policy terms-of-service faq); ABOUT=about; fi
tot=0
for p in "${PAGES[@]}"; do
  h="$(curl -s -m 20 "https://$S.givyx.com/$p")"
  n=$(echo "$h" | grep -o -i -E 'kowalski|autoserwis-kowalski|Warsztatowa|Northgate|Foundry|Avondale|dealership\.givyx\.com|autoservice\.givyx\.com|22 123 45 67|221234567|serwis@autoserwis\.pl|52\.2385|20\.9645' | wc -l | tr -d ' ')
  tot=$((tot+n)); [ "$n" != "0" ] && echo "  LEAK /$p: $n"
done
home="$(curl -s -m 20 "https://$S.givyx.com/")"
echo "$S | $(echo "$home" | grep -o '<title>[^<]*</title>' | sed 's/<[^>]*>//g' | cut -c1-60)"
echo "   robots=$(echo "$home" | grep -o '<meta name="robots" content="[^"]*"' | sed 's/.*content=//') | robots.txt=$(curl -s -m 20 "https://$S.givyx.com/robots.txt" | grep -o 'Disallow: /$' | head -1)"
echo "   leaks=$tot | tel: $(echo "$home" | grep -o 'tel:+[0-9]*' | sort -u | tr '\n' ' ')"
echo "   rating: $(curl -s -m 20 "https://$S.givyx.com/$ABOUT" | grep -o -E '★ ?[0-9][,.][0-9] · [0-9]+' | head -1)"
