# One clear notification to the owner

After an article is published the owner receives **one short message**, not a technical wall of text and not several reports. This document outranks any earlier instructions about notifications in the methodology.

## Single delivery

- On a scheduled run the message is sent only by the scheduler itself, from the agent's final response (the channel is `notify.channel` in `config.yaml`). Do not duplicate the send with scripts, hooks or separate agents. Do not send "published" and then the report as a second message.
- Save intermediate diagnostics, reviewer results, tool errors and retries to the private log (`work/<slug>/`). Do not paste the full report into the final response and do not attach a file automatically.

## Format for a new publication

Final response: usually 450-800, at most 1000 characters including spaces, 5-7 short lines, one message with no tables or attachments. Write in the owner's language; do not artificially translate product names or the search queries themselves.

```
Published: "<clear title>".
Inside: <what the reader will be able to do or understand, one phrase>.
Queries: "<main>", "<related>", "<related>".
Topic strength: <strong / promising / narrow practical> - <one specific reason from the research>.
<direct link to the published page>
```

- In queries, 2-4 natural phrases actually covered by the article; do not present them as measured search volume.
- Topic strength is an editorial assessment with a basis: confirmed demand, an important new change, a frequent question or a useful unsolved task. Do not write "strong" automatically. If there is no confirmation of demand: "Practical topic; search demand not yet confirmed".
- State real impressions/clicks only when useful data exists, with the measurement window and marked as "our site". Views of someone else's video do not equal search demand in your region. No invented success percentages, traffic forecasts or guarantees.
- The brevity of the report does not shorten the research itself and does not cancel a single quality check.

## If not published or attention is needed

Also one message, up to 600 characters.

1. **On the first failure of a slot** (moderation, facts, technical refusal): "The article on <topic> did not go out: <reason>. Taking the next topic: <new topic>, the result will come in the next message". Do not promise deadlines, only state that the agent is already working on the backup.
2. **On the second failure in the same slot**: "Article not published: <reason of the first attempt> and <reason of the second>. Slot skipped. <What is required>". State honestly that the attempts are exhausted; do not present it as "doing it now".
3. **On success at the second attempt**: add one sentence to the success message: "The first topic <X> did not pass the check/moderation, the backup <Y> was taken".

If no confirmed strong topic was found, say exactly that; do not release weak material for the sake of the schedule.

If the article is already published but a problem was found, do not call it a draft: "The article is published, but <consequence for the reader>. <Required action>", with the link in the same message. Do not hide a significant failure under a success message.

Do not copy traces, file paths, exit codes, QA tables, stage numbers, AI score, agent names or CLI commands into the final message. Describe the consequence: "could not save the check results", "could not verify the page", not the raw tool message. Full details are in `work/<slug>/` and the logs, on the owner's request.

## Safe evidence paths

Save new artifacts immediately in `work/<slug>/` inside the project; temporary files before a slug is chosen go in `work/tmp/`. Pass these same paths to the reviewers and record them in the checklist. The checklist must reference real, existing files. On a write refusal, first actually save the file at an allowed path and re-check, instead of declaring the original write successful. Do not disable the system's honesty controls for the sake of a clean report.
