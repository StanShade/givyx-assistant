# Final independent review cascade before publishing

A separate last editorial stage for **new** articles. The main author remains your working model. This stage does not rewrite the article and does not replace research, fact-checking, the legal check, the render check or the delivery check.

**Why separate.** An author in a long session does not see its own patterns: it wrote the text and then "checks" it itself. The final cascade moves the last edit to **a different model or a fresh agent without the author's history**, followed by an independent reviewer who sees the source and the final but does not see the editor's justifications.

## Order

1. Finish the content and legal edits, links, auto-linking and all normalizations.
2. Save the current `work/<slug>/brief.md` and `claims.md`.
3. Run the final cascade (the implementation is up to your stack, the contract is below; an example binding is `qa.final_review` in `config.yaml`).
4. Check that the final version compiles; after any edits repeat the cascade.
5. Publish the exact accepted file. A version changed by the server (including markup normalization on import) does not pass verification: reconcile the local source, accept again and import again. Do not present an old hash as a new acceptance.

If auto-linking or normalization changed even one byte after acceptance - stop: run the cascade on the new version and repeat delivery. A manual `acceptance.md`, an old checklist or a zero AI score does not open publishing.

## Real fresh contexts

Each role is **a new process and a separate request to the model**: no author history, no resume, no tools. The editor is, where possible, **a model from a different family** than the author's (`qa.final_review.editor_model` in `config.yaml`); the reviewer is a separate fresh context of the same or another model. The reviewer receives the source, the result, the brief, the claims and the mechanical diagnostics, and **does not receive the editor's explanations**. The next correcting iteration receives the specific blockers of the previous reviewer.

A maximum of **three full pairs** editor -> reviewer. After the third reject the source file is not replaced, there is no acceptance, the candidates and reports stay in `work/<slug>/`. An unavailable model, an unexpected model id, an error or a truncated response means a stop with no fallback and no manual "accepted". The cascade cannot be simulated inside the main context ("imagine you are a different editor") - that is not independence.

The editor checks, in order:

- living speech: LLM vocabulary tells, bureaucratese, heavy word combinations, artificial familiarity;
- filler: removing it must not take away an action, a fact, a condition, a warning or an explanation;
- the owner's view: is the subject clear to a newcomer, has the meaning been substituted, has the promise been widened;
- rhythm and a line-by-line read after the edits.

Facts, numbers, units, negations, conditions, sequences, code, commands, URLs, other people's exact quotes and the meaning of commercial wording are preserved. Do not invent the owner's experience, numbers or examples. The reviewer separately checks the theses of the source, lost caveats and additions; answers what to do when the advice does not apply and how to verify the result.

The voice sample for the editor is a safe style reference (a short file with examples of delivery, without private details or financial cases). The speech sample is not a source of facts about the product.

Typography: no zero-width/BOM/control markers in the visible text; em dashes are replaced with a hyphen per the local style. **Do not run global replacements across the file**: code, URLs, names and exact quotes are protected. The mechanical diagnostics (`tools/ai-cadence-check.py`) run before the edits and on every candidate; their output is saved and passed to the reviewer. The diagnostics change nothing themselves. CV, the share of short sentence endings and the AI score are reference information, not proof of quality and not a goal. Explain false positives on quotes and caveats left in place. Do not cut meaning for a number. Do not promise detector evasion, ranking growth or indexing.

## Artifacts and version lock

Default directory: `work/<slug>/final-review/` (private).

- `acceptance.json` - the only active acceptance index; deleted at the start of a new run, appears only after accept.
- `runs/<uuid>/original.*`, diagnostics before the edits.
- `runs/<uuid>/iteration-N/`: source, candidate, the editor's prompt and response, `editor.md`, diagnostics after, the reviewer's prompt and response, its verdict.
- Only for the accepted iteration: `final.*`, `final.sha256`, the import payload; the index contains the hash of the source, of the exact bytes of the final and of the canonical payload as a whole, the path of the source file, and both model receipts.

Receipts contain the provider, the requested and the actual model, the status, distinct context ids, call start/end, and the SHA-256 of the prompts and responses. The acceptance check re-reads the evidence from disk: source, candidate, final, payload, both responses and prompts, their hashes. The candidate must match the text from the editor's response, the final file must match the reviewer's actual input, and the saved reviewer response must contain accept and empty blockers. A manual acceptance without receipts, a different model, or a negative verdict does not pass.

## Remote content verification and honest limits

- Before publishing - two reads of the remote state with a comparison of the snapshot and a repeat check of **the same** local acceptance. Even a new valid acceptance of a different local version does not silently replace the already verified remote version.
- Verify all available editorial fields (body, slug, title, meta, categories). Fields that the read API does not return are listed explicitly as `unverifiableFields` with a warning, not assumed to match. A required field missing from the response does not count as a match.
- If the server has no CAS/If-Match for publishing, a narrow "last read -> write" window remains. The local gate is not a server transaction. Do not bypass moderation or server-side blockers.
- SHA-256 is an integrity check, not an external cryptographic signature. A direct API call outside the standard flow is beyond the boundary of this gate.

## Local check without writing to the site

For a smoke test of the mechanism use **a copy** of the file and a separate directory, not the standard acceptance index. A short positive fixture tests the mechanism, not the readiness of a full article. Store the actual results and limitations of a specific smoke test next to its artifacts; do not write "success" on a reject. A mechanism check must produce no writes to the site and no platform changes.
