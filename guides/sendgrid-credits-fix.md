# SendGrid — "Maximum credits exceeded": verify the account, move to a paid plan

**Status 2026-08-17: all Givyx email is down.** `POST /emails` returns per-recipient
`sent:false` with `SendGrid send failed with status 401: {"errors":[{"message":"Maximum credits
exceeded"}]}`. The 401 comes from SendGrid, not from our API — our key and payload are fine, SendGrid
is refusing to accept the message. Reproduced twice.

**What is broken while this lasts:** the reply to the inbound Studio lead, every prospect offer and
follow-up, contact-form **lead notifications**, the daily monitoring digest, and any client-facing
transactional mail. Inbound leads are arriving silently — the 15 Aug lead sat unseen for two days and
this is the likeliest reason.

---

## 1. Find out which of the two things it is

`Maximum credits exceeded` means one of:

- **the plan's send allowance is used up** — on the free tier that is a daily allowance that clears on
  its own; or
- **the plan/trial ended, or a payment failed**, and the account has no allowance at all.

They look identical from the API. Tell them apart in the dashboard:

1. Log in at **app.sendgrid.com**.
2. Read the **banner across the top** — an expired trial or a failed payment is announced there.
3. **Settings → Account Details** → current plan, and **Billing** for payment state.
4. **Stats** (left nav) → requests per day. If yesterday sits at a round number like 100 and today
   stopped at the same wall, it's the daily cap. If sends stopped mid-week at an odd number, it's
   billing.

If it is only the daily cap, sending resumes by itself at the reset — but the ceiling will keep
catching us, and it is already costing a live lead, so upgrade regardless.

## 2. Upgrade — 🟡 BLOCKED, under compliance review (2026-08-17)

Card added, plan change attempted, SendGrid responded:

> *"We are currently reviewing your request, and may be reaching out to you in the next 72 hours via
> email, phone, or video conference to confirm the identity of your account and gather more
> information about your intended usage."*

This is a routine anti-spam identity review, not a rejection. Three things decide how fast it clears:

1. **Answer them the same day they make contact.** These reviews stall on silence far more often than
   they fail on merit. Deadline to watch: **~2026-08-20**.
2. **Make sure their email can actually reach you.** It goes to the SendGrid account address. If that
   is `info@givyx.com` forwarded through improvmx, confirm the forward works and check spam — a
   verification email landing somewhere unwatched is the classic way a 72-hour review becomes a
   two-week one.
3. **Have the usage answer ready** — it is the only real question they are asking. Ours is a strong
   one, so give it plainly: transactional mail only (contact-form lead notifications, invoices,
   client site notifications, ops alerts to ourselves); **no marketing lists, no purchased lists, no
   bulk campaigns**; recipients are people who contacted us or are paying customers; own authenticated
   domain (`givyx.com`, DKIM in place); volume in the tens per day, not thousands. Say what Givyx is —
   a website platform for small businesses — and that mail volume tracks customer count.

Once approved: **Settings → Account Details → change plan**, smallest paid email-API tier (our volume
is nowhere near any tier's ceiling). Prices and tier names move — read them off the page rather than
trusting any figure written here.

### Meanwhile: the free allotment is daily, so protect it

Their own advice is to keep sending slowly on the free plan and build domain reputation. That means
the allotment refills — but it is small, and right now it is being consumed by something.

- **Stop all test sends.** Every test burns quota that a real lead notification needs. Retry the real
  send after the daily reset instead of poking it now; a rejected send costs nothing, an accepted one
  costs a credit.
- **Find out what ate it: SendGrid → Activity Feed.** It lists recent messages with recipients and
  subjects, which names the consumer immediately.
- **Suspect a flapping host.** `scripts/uptime-check.sh` is edge-triggered — it mails only on an
  up→down or down→up transition, and `lead-notify-check.sh` alerts once per response id — so neither
  spams under normal conditions. But a host oscillating on the 5-minute cron produces two alerts per
  cycle, up to several hundred a day. Check `logs/uptime-state/` on the VPS and the Activity Feed for
  a run of `[givyx-ops] DOWN` / `RECOVERED` pairs on one host. If that is the cause, flap damping
  (alert only after N consecutive failures) is the fix, and it restores lead capacity today without
  waiting for SendGrid.
- **Priority order for whatever quota exists:** lead notifications first, prospect replies second, ops
  digest last. The daily digest at `0 7 * * *` is the most droppable thing on the list.

## 3. Do NOT let the API key change

🔴 **The single thing that can turn a 20-minute fix into a broken deploy.**

Our sender key lives in `givyx.ops/env/shade.env` as **`SendGridConnection`**. Upgrading a plan does
not touch API keys — but *"while I'm in here let me rotate the key"* does, and the moment the old key
dies, every send 401s again with a different message.

If a key does get regenerated for any reason:

1. Update `SendGridConnection` in `givyx.ops/env/shade.env`.
2. Commit + push, then let the ops apply run — **and check that it actually ran**. A failed
   `apply-ops` cannot be fixed by re-running the workflow: the VPS has already fast-forwarded, so the
   rerun reports success having done nothing. Push a new commit instead.

Also leave **sender authentication alone**. The domain's DKIM (SendGrid `s1`/`s2` CNAMEs) is what
carries DMARC alignment for `info@givyx.com` — SPF lists improvmx only, so DKIM is doing the real
work. Breaking it sends prospect mail to spam without any error to warn us.

## 4. Verify with the real operation, not a status page

A green dashboard is not proof. Send an actual message:

```bash
KEY=$(grep '^EmailApiKey=' /Users/stan/Code/givyx/givyx.ops/env/shade.env | cut -d= -f2-)
curl -s -X POST https://api.givyx.com/emails \
  -H "X-Givyx-Api-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"to":["stan.zak.inf@gmail.com"],"subject":"SendGrid restored","text":"Test after plan change."}' \
  | python3 -m json.tool
```

Expect `"sent": true` for the recipient. Anything else, read the `error` string — it is passed through
from SendGrid verbatim.

*(This is the automatic-tax lesson again: `automaticTaxSafeToEnable` was a status endpoint we wrote
ourselves, we trusted it instead of the operation, and checkout broke. Verify the operation.)*

## 5. Once mail is flowing again

1. **Send the inbound Studio lead's reply** — text in
   `outreach/inbound-2026-08-15-givyx-studio.md`. If it went out manually from Gmail in the meantime,
   don't double-send.
2. **Check for lead notifications that failed while this was down.** Form submissions retry 3× and
   persist delivery status, so failures should be recoverable rather than lost — go through them and
   make sure no other inbound lead is sitting unanswered.
3. **Consider a monitor for this specific failure.** We already alert on lead-delivery failure; a
   sender that refuses everything is the case where the alert itself cannot be delivered. A check that
   notices "0 sent / N failed" and reaches Stan by some other channel — SMS, or the ops dashboard —
   is what would have caught this on 15 August instead of 17 August.
