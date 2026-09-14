# Email 1 — the "we built a version for you" offer · template (PL + EN)

Reconstructed 2026-09-14 from the rules Stan set on 09-10/09-11 (the sent bodies were composed
inline and not saved). **Stan re-approves this once; then every batch reuses it verbatim** with
only `{{…}}` filled. Rules baked in: warm, not official · lead with a verified fact about what they
do WELL, never a fault list · describe the experience, invite the click · 149/249/750 shown the
same way every time · one send per curl · goes to Stan first.

Send call: `POST /emails` with `layout:"givyx"`, `locationId:"l_givyx"` (footer = Givyx address,
phone, email — never in the body), `replyTo: info@givyx.com`, unique `utm_content`.

## PL

**Subject:** `Zbudowaliśmy wersję strony dla {{NAZWA}}`
**Eyebrow:** `Oferta` · **Title:** `Strona dla {{NAZWA}}`

> Dzień dobry,
>
> Z tej strony Stan z Givyx, z Krakowa. Zanim napisałem, sprawdziłem Was: {{FAKT}}.
>
> Zbudowaliśmy wersję Waszej strony — z Waszą nazwą, telefonem, usługami i oceną z Google:
>
> **[Zobacz stronę →]({{URL}})**
>
> Strona zaczyna się od wjazdu do hali i zjazdu pod maskę silnika, potem usługi na pierścieniu,
> rezerwacja wizyty i kontakt — wszystko działa na telefonie. Zobaczcie sami, to 30 sekund.
>
> Jeśli się podoba, uruchamiamy ją na Waszej domenie w 2 dni. Abonament:
> **149 zł/mies.** — ta strona, jak w podglądzie · **249 zł/mies.** — rozbudowana, nowoczesna,
> z rezerwacją online · **750 zł/mies.** — płatności online, bez brandingu Givyx.
> Utrzymanie, zmiany i poprawki są w cenie — my dbamy o stronę, Wy o auta.
>
> Odpiszcie na tego maila albo zadzwońcie — chętnie dopasuję stronę pod Was.
>
> Pozdrawiam,
> Stan

`{{URL}}` = `https://{{slug}}.givyx.com/?utm_source=email&utm_medium=oferta&utm_campaign={{slug}}&utm_content={{code}}`

## EN (US)

**Subject:** `We built a version of your site — {{NAME}}`
**Eyebrow:** `Offer` · **Title:** `A site for {{NAME}}`

> Hi,
>
> Stan here, from Givyx. Before writing I looked you up: {{FACT}}.
>
> We built a version of your site — your name, phone, services and reviews:
>
> **[See the site →]({{URL}})**
>
> It opens with a drive into the shop and a dive under the hood, then your services, online
> booking and contact — all on the phone. Takes 30 seconds to look.
>
> If you like it, it goes live on your own domain in 2 days. **$60/month**, maintenance and changes
> included — we keep the site current, you keep fixing cars.
>
> Reply to this email or call — happy to adjust anything.
>
> Stan
>
> This is an advertisement. Reply "unsubscribe" and you won't hear from me again.

`{{URL}}` = `https://{{slug}}.givyx.com/?utm_source=email&utm_medium=offer&utm_campaign={{slug}}&utm_content={{code}}`

## Once the risk-reversal decision is made
Add one line before the sign-off, both languages:
PL `Bez umowy, rezygnacja w każdej chwili{{, pierwszy miesiąc gratis}}.` ·
EN `No contract, cancel any time{{, first month free}}.`
