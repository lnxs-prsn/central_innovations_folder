# capability-002 report — 2026-11-05

## Outcome and handoff

Built within the assigned brief and the four adjustments in its recorded GO. Staged, not published:

- Stage: `capability/.staging/capability-002/`
- Manifest: `capability/.staging/capability-002/EDITION.json`
- External manifest SHA-256: `f66f1577cdd34b086183467147a2ec28ff1ef2dbed84268043e91a7439a2bdfb`
- Inventory: 20 payload files plus the manifest. Verified the external hash, every listed size/hash, exact file inventory and byte equality with the corresponding source files after validation.

The executive can independently verify and install this complete fixed stage, then identify it and its external hash in the mutable published index. OWNER.md now states the index's entry duties. This run changed no published files, made no commits or pushes, used no network and made no real admission or other curator decisions. No finding requires changing what the CEO wants.

## Outcome against the brief and adjusted GO

**Main effort — existing know-how.** Added the optional `capability/EXISTING.md`, linked before the numbered procedure in USE.md. It starts with the executive's per-piece choice, including keeping material local or deferring without conversion or offering. It applies regardless of the holding's folder or format. The separate file keeps its reading optional for agents doing other work.

The guide explicitly handles a received prose copy without a context record. The developer is best placed to describe development, and actual using projects their uses; a holder may complete only facts it can truly state. `origin.project` names development and `evidence[].project` names the reported use, rather than either defaulting to the supplier. Unknown developer or required evidence leaves the piece unoffered. Adding context changes content identity, so two holders completing one copied technique can produce separate identities without independent successes. The guide preserves their relationship and says only that the curator can relate offers. It does not assign merge work to the holder.

A holder's observed real use adds evidence about that use, with its own situation and scope. It does not establish unknown origin, invention or material refinement. Copying, renaming, possession and inspection are distinguished from development and actual use. Nulls, explicit unknown states, empty lists, adverse evidence, generic assets and review obligations remain governed by standard 1.0; no requirement was weakened to make old prose publishable.

Manual reading against invented decision cases gave these routes (guidance review, not evidence of actual project effort):

| Invented holding | Guide's route |
|---|---|
| Own invention with evidence and kit | Record actual origin and successful use; verify, check and deliberately offer if chosen. |
| Complete unchanged received bundle | Preserve the developer and evidence; multiple suppliers do not add successes. |
| Copied prose without a record, development and use facts known | Complete only supported facts; completion produces a new identity, with the received basis visible. |
| Two holders independently complete one copy | Separate identities remain possible; no independent use is inferred; the curator can relate the offers. |
| Copy with holder's own successful real use but unknown developer | Own use can be recorded, but it cannot fill origin; leave unoffered. |
| Material refinement in actual work | Identify the actual development/change and received basis, with supporting use. |
| Missing required context or deployable kit | Leave unoffered rather than inventing facts or treating prose as complete. |
| Executive chooses to defer | Keep local; no conversion or offer is required. |

**Reaching and using the capability.** USE.md's first line is one generic copyable sentence covering both uses and when to enter:

> Before drawing on shared know-how or offering yours, read INDEX.md at the listed location, or USE.md in a clone.

The listing supplies the location. The publisher's mutable index names the current fixed capability, external manifest hash, USE.md and current catalogue; relative paths resolve there. OWNER.md specifies those duties and distinguishing historical entries. No fixed edition claims to identify a future edition or catalogue.

A bare clone runs directly wherever examples say EDITION, with no pack or empty-catalogue prerequisite and no edition number in the entry. Initialization, checking and offering need no catalogue. Without the curator's index there is nothing yet to ask/select. One sentence directs self-curation to OWNER.md. Verified direct use with an invented project: init, self-check, check and offer succeeded without a catalogue; the code copy's files remained identical. Packing for a clone was not needed.

**Readable missing-catalogue failure.** `Catalogue.__init__` now detects an index with no catalogue reference and raises an actionable diagnostic naming the curator's published INDEX.md, `--catalogue` and OWNER.md for self-curation. The CLI returns status 2; there is no fallback. Prose-only indexes receive the same guidance. Existing malformed blocks still use the strict index parser. The new test first accesses a valid catalogue, removes the current reference, and verifies both ask and select fail instead of using remembered policy; it also covers prose-only indexes for both commands.

**Validation from an edition.** Separated source packing determinism/inventory assertions into a source-only test. The detached runtime test packs from a temporary developing source when run in source, but directly copies the fixed edition when run from an edition. It never removes an edition marker to disguise source. Both routes exercise synthetic self-check, ask/select, standalone checking, writable-project rejection, packing rejection and unchanged read-only edition bytes. OWNER.md documents the exact commands and the sole intentional edition-only skip. Source packing remains tested.

**Compatibility, size and update.** The runtime change is limited to missing-catalogue diagnostics. The pack allowlist adds EXISTING.md. No commands, dependencies, schema, publication formats, authority changes, migrations or background behavior were added. `standard/` and PUBLICATION.md have no diff. Existing offers and records require no migration. UPDATE.md records `Significant change: no` with the reason and taking impact; the small diagnostic change did not warrant changing that accepted classification. All existing tests still pass alongside the three added tests.

## Validation evidence

Environment: Linux 6.18.50+rpt-rpi-2712, aarch64, glibc 2.41; Python 3.13.5 (`python3`) and Python 3.11.15 (the supplied uv-managed interpreter, invoked only as an interpreter).

| Check | Python 3.13.5 | Python 3.11.15 |
|---|---|---|
| Source: `python -B -m unittest discover -s tests -v` | 36 passed | 36 passed |
| Disposable copy of final staged edition: same unit command | 35 passed, 1 intentional source-packing skip | 35 passed, 1 intentional source-packing skip |
| Source: `python -B -m standard.render --check` | Passed | Passed |
| Disposable edition: same render check | Passed | Passed |
| Disposable edition files after unit suite and render check | Byte-identical | Byte-identical |

Source tests include direct generic-copy use without a catalogue, missing-reference guidance/no fallback, deterministic source packing, manifest/file verification, detached read-only operation and existing empty-catalogue behavior. Tests and self-checks use invented temporary projects only. In addition, every source Python file parsed with Python 3.9 grammar using `ast.parse(feature_version=(3, 9))`; this is syntax evidence only.

`git diff --check` passed. Checked tracked source and the new guide, then every staged payload, for forbidden personal paths; none found. Final staged payload matches source exactly. Stage verification used the publication module's manifest and file verifiers plus an exact inventory comparison. No project holdings, old reports or unpublished contributions were used as guide examples or payload.

## Friction, resources and limits

The first test-edit command used a repository-relative filename while already in the capability directory, so the edit failed before writing; the following suite ran the prior 33 tests. Corrected the working-directory mismatch and subsequently validated the intended 36-test suite. An initial guessed Python 3.11 x86_64 interpreter path was absent; located the supplied aarch64 interpreter and used it successfully. Neither event is counted as successful final validation.

The new prose-only-index test initially exposed that `read_index` requires an explicit optional flag to accept an index with no knowhow block. Adjusted only the catalogue caller to use that existing option; incomplete or malformed blocks still fail strict parsing. Both full source suites and both final edition suites then passed. This did not change scope or require referral.

Used one writer, local file tools, existing standard-library code/tests and the two provided interpreters. Keeping the guide, entry contract, diagnostic and validation changes together avoided divided ownership. No additional agent or external service was needed. The stage and its packing cost journal are under the capability's ignored `.staging/`; all exercises use temporary invented projects, not this project's root.

Windows and Python 3.9 execution remain untested and are not claimed. Read-only mode checks and byte snapshots passed here; they do not establish Windows filesystem behavior. Actual effort for a real project to reconstruct context remains unknown; the guide says so. Runtime tests cannot establish that a future agent will make correct provenance judgments; the guide and the unchanged human review obligations support that judgment.

Publication and index updates remain the executive's next work. This report is the completion receipt for the resumed run; the run now ends.
