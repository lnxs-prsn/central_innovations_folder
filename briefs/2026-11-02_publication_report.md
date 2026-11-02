# Publication report — subordinate 3 — 2026-11-02

## Outcome and handoff

[evidence: `briefs/2026-11-02_publication.md`, “Supervisor's check and GO”; implementation under `capability/`; checks below] Built and tested the publication capability within the recorded GO and its four adjustments. Offers arrive only through explicitly supplied published parts; the curator retains verified content and publishes self-contained catalogue editions; takers keep their records in their own projects. The generic capability can be frozen into an identified edition. No discovery, finding or interpretation requires changing the CEO's desired outcome.

[evidence: final packaging and independent verification] Staged capability edition **`capability-001`** at **`capability/.staging/capability-001/`**. External SHA-256 of its exact `EDITION.json` bytes:

`55c3cd1af7729eb8732be38ad29a335137728186fe211218584053fb8837ea3b`

The manifest covers **19 files, 149426 payload bytes**. An independent read verified the manifest identity, exact file set, every file size/hash and byte equality with the final source. No included file contains a personal `/home/mr` path. The stage is git-ignored; it contains only generic code, standard/template, guides, update message and invented tests. Packaging cost is recorded separately in `.staging/costs.jsonl`, outside the edition.

The executive receives this report when this run ends, checks the staged artifact, and holds publication into this project's `published/` and commits. I have not written there, committed, pushed, run real intake or made a real admission/exclusion decision. No `init`, `offer`, `ingest` or `publish-catalogue` was run against this project's root. All exercises used invented projects and offers in temporary directories. Only the authorized generic packaging command staged an artifact inside `capability/`.

## Result against the brief

| Required outcome | Result and evidence |
|---|---|
| Complete fixed offers, checked before offering (M6) | `offer` preflights and checks the project's own working contribution, captures its bytes, checks the staged copy, freezes a manifest-identified envelope under its own `published/knowhow/offers/` and preserves other index prose. Context remains in standard 1.0's PATTERN record, with the whole declared kit. Repeating an unchanged offer is idempotent; changed bytes get a new content ID and no inherited admission. |
| Publication-only curator intake | `ingest --published-parts LIST.json` reads only listed public indexes and the offers/manifests they name. There is no projects-folder configuration, project walk, private collection read or automatic intake during ask/select. Missing list input creates no state or cost record. Empty input is valid. An index without a know-how declaration is counted as a nonparticipant; malformed declarations and bad offers are explicit errors. Independent valid offers can be retained with a partial-failure result. |
| Admitted know-how survives its source (M1, M2, M4) | Verified offers, origins and SQLite decisions stay in the curator project's `.knowhow/curator/`. Catalogue editions include discovery, full bundles/checks/context, origins and decision policy/history. Tests delete both suppliers and then publish, ask and select successfully. Removing a source never deletes retained content. |
| Copies and meaningful identity (M5) | Content hashes frame sorted contribution-relative names and exact bytes, excluding supplier/path. Copies retain all supplying origins under one content ID. Similar offers remain separate until a reasoned merge; a target must be separately admitted. Original project/evidence accounts remain unchanged. |
| Compact screening, full context on selection (M7) | Ask reads verified discovery/policy, without opening PATTERN or kit files. Default five, maximum twenty candidates, with a 12000-byte candidate-list limit and omission count. Select verifies the chosen complete bundle and returns full context, check, origins, reasons and kit locator. Negative-condition matches and lossy-screening limits remain visible. |
| CEO exclusions and project declines (M9) | Global and known-project-UUID exclusions are curator events. Local declines/reversals belong to the taker. Both stages apply effective policy and local declines, including restrictions on merged predecessors. Selection resolves the current public index again, so an old candidate does not bypass new published policy. Unknown UUID exclusions are rejected. |
| Use and costs (M10) | Takers keep measured command output bytes/time, inspections, actual-use outcomes and caller-estimated savings in their own `.knowhow/`. The curator records its own costs/intake counts in its SQLite store; packing has its own staging cost journal. Failures after a project is established also record costs where writable. No organization capacity aggregate exists. Measurements exclude the final cost write/output emission, and bytes are not model tokens. Real net savings remain unproven. |
| Empty recovery and portability (M8) | A detached generic copy packs deterministically, starts without real knowledge, and runs the invented offer-to-selection self-check. Runtime entry scripts suppress bytecode writes before local imports. Tests execute ask, select, standalone check and self-check from a read-only fixed edition, preserving its exact bytes and creating no bytecode/state there. Python 3.9 syntax and portable path handling are checked; actual execution was on Linux/Python 3.13.5. |
| Movement/reassignment | A random project UUID is local and declared publicly; moves retain the UUID, declines, decisions and retained content. Tests move supplier, taker and curator. Duplicate simultaneous public roots claiming one UUID are diagnosed. Edition hashes identify content separately from replaceable locators; guides require verifying the same identity after movement, without searching for a matching folder name. |

[evidence: `capability/access/publication.py`, `access/engine.py`, tests] Publication handling rejects traversal/absolute inventory paths, symlinks/reparse points, prohibited names, special files, duplicate JSON keys, case collisions, invalid manifests and changed file hashes. All inventory paths are validated before data reads; the whole bundle is preflighted before checking/offering. Selected and retained bundles reject unlisted files as well as changed listed files. No kit is executed and no evidence locator is fetched. Hashes establish integrity relative to the supplied index, not authenticity, semantic truth or role authority.

## Supervisor's adjustments and interface decisions

1. **As small as serves:** dropped the proposed `review` command; `decisions ID` supplies full curator inspection alongside events, checks and kit location, and `decisions` lists pending IDs and known projects. Removed `configure`, projects-folder namespaces, `gather`, implicit project-marker discovery and clone-side `.local/` writes. Each remaining command serves offering, selective use, explicit decisions, measurement, recovery or fixed publication.
2. **Write boundary:** exercises used temporary invented projects only. Actual packaging writes only the ignored `capability/.staging/`. No project-owned records outside the assigned deliverables were changed. `.knowhow/` and `.staging/` are ignored in the generic repository; the packaging allowlist excludes both.
3. **Known UUID for exclusions:** OWNER.md explains that intake learns the UUID from the project's own published index. Initialization declares the UUID even with no offers. A project that has published nothing cannot be excluded by ID until it publishes; the command enforces known IDs instead of accepting a guessed path/name.
4. **Taker guide:** USE.md starts with one copyable line covering both drawing on know-how and offering it. Steps are `init`, `ask`, `select`, `decline`, `log-use`, `check`, `offer`. Curator commands appear in OWNER.md. PUBLICATION.md defines formats; UPDATE.md states significance and taking impact.

[interp: small implementation adjustment] Generic edition staging uses the source's explicit ignored `.staging/`, rather than initializing a synthetic project identity in `.knowhow/` merely to pack code. `pack-capability --project SOURCE` requires the loaded developing source itself and rejects fixed editions. It never publishes into the project's public part. This keeps generic maintenance separate from project/taker state while preserving the authorized write boundary.

[evidence: source comparison] Standard 1.0, its authoritative definition, generated documentation/template and standard tests remain unchanged. The standalone checker gained prohibited-path/tree preflight and early bytecode suppression. The existing presence-versus-truth distinction, matching approach, reasoned decisions/reversals and merge restriction propagation remain; storage/intake and taker access were rewritten around publication. `knowhow.py` remains the one runtime command entry.

## Validation

[evidence: final executed checks, 2026-11-02]

- `python -B -m unittest discover -s tests -v`: **33 tests passed in 4.257 seconds**, including all 11 existing standard tests and 22 publication/access tests.
- `python -B -m standard.render --check`: passed; generated standard files still agree with their definition.
- `git diff --check` in `capability/`: passed.
- Python 3.9 syntax parsing: passed for every staged Python file. This is syntax validation, not a Python 3.9 runtime claim.
- Detached source packaging repeated with identical inputs produced the same manifest identity. A read-only detached edition successfully ran runtime commands, standalone check and synthetic self-check without changing itself.
- Final stage verification: external manifest SHA-256, exact allowlisted inventory, all file hashes/sizes and equality with current source passed. Stage was not published.

The tests cover missing-list zero activity, empty catalogue, public-index preservation, supplier-only-public reads, pending/incomplete content rejection at admission, exact-copy origins and warm check reuse, changed-content readmission, supplier disappearance, project moves and UUID conflicts, current-policy rechecks, global/project exclusions and reversals, local decline isolation, merge restrictions and history, rollback, interrupted publication, refusal to overwrite a fixed edition, unsafe/tampered/unlisted files, simulated reparse attributes, exact output-byte accounting and command write sets.

Tenfold invented growth, from the final test run:

| Distinct contents | Returned candidates | Candidate bytes | Whole synthetic growth exercise |
|---|---:|---:|---:|
| 10 | 5 | 3291 | 0.200 s |
| 100 | 5 | 3296 | 1.746 s |

The exercise includes creating/offering, intake, synthetic admission, catalogue publication, ask and warm intake, rather than measuring ask latency alone. Ask was guarded against reading any PATTERN/kit file. Warm intake performed zero repeat standard checks, while still verifying incoming bytes. These are small synthetic measurements, not evidence of real savings or large-scale performance.

## Friction, resources and limits

[evidence: GO and implementation] No brief adjustment is needed beyond the supervisor's four recorded points. The ownership change required replacing intake/store/access together; reusing the old clone-side settings would have preserved the forbidden write boundary. Keeping one writer avoided an additional integration interface. An explicit maintenance staging command avoids initializing this project during the build run.

[evidence: resources used] One subordinate instance, local filesystem/code/document work, Python's standard library, temporary invented projects, the Linux interpreter and Git read-only status/diff checks. No subagents were assigned or needed. No network, real supplier investigation, real innovation fixture, commit or push. Test resources exercised the complete path and failure boundaries; the standard suite protected the standing standard. The generic fixed artifact is about 149 KB of payload. Total agent tokens/time and real resource savings were not measured here and are not claimed.

[interp: remaining practical limits] The organization list of published parts is still unavailable, so real intake remains blocked pending that input; independent generic implementation is complete. M1/M3/M6 reach only projects that choose to take the capability and publish. Evidence may remain unavailable for independent verification. Lexical matching can miss synonyms. Catalogue manifests and discovery/policy reads grow with catalogue size even though candidate output stays bounded; publication currently assembles its files in memory, and no large real-catalogue memory bound has been established.

Exclusions take effect for takers when the curator publishes a new catalogue. An unavailable/invalid current index fails closed; a disconnected old copy cannot discover later decisions. Publication is not access control over already readable bytes. Actor/project ownership assertions are not authentication. Read-only mode and reparse handling were tested on Linux (including simulated reparse flags); Windows and Python 3.9 execution remain untested. No live adoption, real admission or measured reuse saving is claimed.

Handoff: implementation, tests and fixed generic stage are complete for executive review. This run ends with this report. Publication and commits remain with the executive under the task brief; pushing remains with the CEO.
