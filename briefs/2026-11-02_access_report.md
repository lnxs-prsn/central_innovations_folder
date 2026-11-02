# Store and access — report, 2026-11-02

## Outcome and situation

[evidence: `briefs/2026-11-02_access.md`, Supervisor's check and GO; implementation, tests and real measurements below] Built store/access under `capability/` within the recorded GO and five adjustments. The command gathers into an ignored local store, recognizes exact content copies, offers task matches, returns selected full context and retained bundles, checks additions compactly, and records owner/project decisions and use costs. The standard and its original tests were not changed. No finding requires changing the CEO's intended outcome. This run ends with this report for the executive's receipt.

[evidence: real catalog audit] The real tree yielded **10 collections, 127 contribution locations, 20 distinct contents and 107 additional copies**. All 20 retained contents have invalid/absent final context records under the standard; none is mechanically complete. No admission or other decision was entered. Asking from Central consequently returned no offers. The mechanism is working, but useful cross-project offers still depend on contributing projects completing context and the executive's admission pass. I did not relax that boundary.

## Delivered behavior against the brief

| Brief requirement | Result and evidence |
|---|---|
| M1–M3: refresh when asked, closed/unused/new projects included | `access/engine.py`, `Store.gather`, discovers collections recursively inside the explicitly configured projects folder; ask and select refresh first. Tests use a new receiver without an innovations folder and nested project markers. No opening trigger or background process is required. |
| M4: preserve what is gathered, select only what fits | Immutable snapshot directories retain safely readable bytes, failed checks and historical locations after source edits/removal. Selection returns full PATTERN text, structured context/check results, location currentness, decision history and a resolvable local kit bundle. Tests remove sources after admission and still retrieve the retained context and bundle. Nothing is copied into the receiver. |
| M5: recognize copies, keep similar material apart | SHA-256 over framed sorted relative entry names, kinds and exact file bytes; no timestamps or supplying locations in content identity. One identity has multiple locations. Changed bytes produce another identity with no inherited approval. Synthetic tests and the real-tree counts establish exact-copy recognition, not semantic equivalence or independent success. Similar material remains separate until a recorded owner merge. |
| Admission, merge, retirement and reasons | Explicit commands append actor, reason, scope, target, time and reversal state to SQLite events. Presence and a complete safe snapshot are prerequisites to admission, never sufficient review. Tests cover incomplete admission refusal, merge restrictions, retirement/reinstatement, retained event history and rollback of a multi-ID failure. Real event count remains zero. |
| M7: compact discovery then full context | Deterministic lexical ranking with weighted title/problem/positive suitability; match terms and negative-condition terms aid screening without claiming semantic fit. Offers default to 5, maximum 20 and a 12000-byte candidate-list budget. Own unadmitted matches include diagnostic counts and the first three problems. Full selection does not silently truncate context. The 10/100-content measurements below show bounded output. |
| M9: CEO exclusions and project declines | Scoped/global exclusions and project declines suppress both ask and select, including own material. Explicit reversals preserve history. Restrictions on merged inputs also suppress the surviving target so a merge cannot bypass them. Tests exercise scope, reversal and selection after a stale offer. No real exclusion or decline was entered. |
| M10: use and cost | Automatic SQLite `uses` records store returned IDs, exact UTF-8 response bytes including final newline, elapsed time and gathering counters. `log-use` records actual caller-reported outcome and optional saving estimate separately from inspection. Check/self-check costs go to `.local/command-uses.jsonl` without requiring configuration. These are measurements and attributed estimates, not proof of net savings or token counts. Help/usage failures and failed operations do not create successful use records. |
| M8 and machine-local configuration | A detached standalone copy operates from another working directory with an empty store. Missing configuration asks explicitly; noninteractive invocation gives the configure command and performs no search. `.local/settings.json` and all state are git-ignored. A different absolute projects root selects a new local namespace: no relocation machinery or migration. |
| One portable command and entry | `knowhow.py` is the Python entry, callable by explicit clone path from any directory. Python 3.9 syntax, standard-library dependencies, portable component checks and symlink/reparse rejection; no shell or network use. `USE.md` addresses agents in projects; `OWNER.md` holds owner decisions. Native Windows and actual Python 3.9 execution remain unestablished. |

[interp] Selection is an inspection request followed by full context, not automatic deployment or a statement of fitness. The caller must inspect assets and evidence before applying the technique. Historical locations and contributor-reported verification remain labeled; no evidence is fetched and no kit is executed.

## The five adjustments

[evidence: delivered files]

1. Dropped changed-root relocation, `--offset` and browse. A changed configured root is a new namespace, explicitly documented. `--limit` remains, with matching/omitted counts; a narrower or rephrased task is the way to change the offer.
2. `USE.md` teaches ask, select, check, decline and log-use, plus configuration/self-check needed to operate them. It refers to `OWNER.md` in one line and gives no admission instructions. Owner commands and authority boundaries are in `OWNER.md`.
3. Revised the proposed first line to include adding. It is installed as the first line of `capability/USE.md`, for the executive to settle:

   > Find reusable project know-how with its context; open this file before reusing a technique or adding to your project's innovations.

4. The `check` wrapper filters out every `present` diagnostic. It shows missing/invalid/unknown items with the standard's messages and required review duties. JSON is compact too; the standard's original checker and its richer API remain unchanged. A successful check does not print successful individual fields.
5. After tests passed, configured `/home/mr/Desktop/python` in the clone's ignored state, asked once cold and once warm, measured counts/timings/output, audited zero decisions, and left state in place. Details follow.

## Real-tree evidence and retained state

[evidence: ignored `capability/.local/real-evidence.json`, `real-cold-ask.json`, `real-warm-ask.json`; catalog `uses` entries; `real-state-audit.json`] Both real asks ran the same explicit command, from Central, with `--task "context reusable project knowledge" --project /home/mr/Desktop/python/new_projects/central_innovations_folder --json`. The task is a measurement input, not an admission decision.

| Measurement | Cold | Warm |
|---|---:|---:|
| Collections | 10 | 10 |
| Contribution locations | 127 | 127 |
| Distinct current contents | 20 | 20 |
| Additional copy locations | 107 | 107 |
| Bytes hashed | 912,558 | 912,558 |
| New retained contents | 20 | 0 |
| Presence checks run | 20 | 0 |
| Gathering seconds | 0.930536 | 0.789090 |
| Command seconds logged before logging/output | 0.938712 | 0.798321 |
| Whole subprocess wall seconds, including interpreter startup/exit | 1.014676 | 0.870644 |
| Exact stdout UTF-8 bytes, including final newline | 422 | 419 |
| Offered candidates | 0 | 0 |
| Scan errors / warnings | 0 / 0 | 0 / 0 |

[evidence: audit] All 127 locations are current, 20 contents retained, zero snapshot issues, zero read errors and **zero decision events**. The only non-present check rule across the 20 contents is `json`, field `Context record`, state `invalid`. The standard reports missing final context this way; the report does not call these complete contributions. No source material is included in generic implementation or fixtures. Real responses and personal state stay ignored.

State left for the executive's admission pass:

- Settings: `capability/.local/settings.json`.
- Namespace: `capability/.local/namespaces/fc26e6f7478a7234f967c48c2b02a7c3678be296c70d752713150af37cc07fbd/`.
- Catalog: `catalog.sqlite` inside that namespace; decision events and command-use records are there.
- Bundles: `bundles/<content-id>/<contribution-directory>/` inside that namespace.
- Measurement responses/audit: the four JSON evidence files named above directly under `capability/.local/`.

[evidence: `git -C capability check-ignore` and `status --short --ignored`] Settings and the namespace catalog are ignored; status reports `!! .local/`. Generic code/docs/tests are untracked pending the CEO's commit. I staged nothing, committed nothing and pushed nothing. The parent project's existing BRIEF/MAP/session changes were left alone.

[limit] Warm gathering still traverses the projects tree and hashes source bytes; content hashes avoid recopying immutable bundles and rerunning checks, rather than promising zero I/O. These are two sequential observations on this machine, not a benchmark distribution. The small difference in real output size is due to numerical metrics. No use of real admitted material occurred, so this run does not establish actual savings from reuse.

## Validation and portability limits

[evidence: final validation commands] `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v` passed **22 tests**: 11 access tests plus the 11 unchanged standard tests. `PYTHONDONTWRITEBYTECODE=1 python -m standard.render --check` passed. Runtime was **Python 3.13.5**, Linux aarch64, `Linux-6.18.34+rpt-rpi-2712-aarch64-with-glibc2.41`.

[evidence: `tests/test_access.py`] Access validation includes empty state/configuration prompting; isolated self-check; a new project without innovations; nearest nested git marker and explicit project identity; containment and link rejection; byte-identical copies; stable warm hashes; retained old versions after edits/deletion; no inherited admission; full selected context; own-only incomplete contributions; global/project decisions and reversals; restriction enforcement again on selection; merged-source restrictions; invalid record types; rollback of a partially attempted multi-ID decision; secret entries not read or returned; link/special-file partial snapshots refused admission; compact check without successful field output; exact cost-byte accounting; root namespaces; Python 3.9 syntax parsing and Windows-reserved component names; a standalone clone path containing spaces invoked from a receiver's directory.

[evidence: final synthetic growth test] With invented contributions, growing from **10 to 100** contents kept five offered candidates and increased the measured compact offer from **3940 to 3942 bytes** (excluding command-level gathering metrics). At 10 contents, first gathering took 0.025627 seconds and warm gathering 0.003122 seconds; at 100 contents, the expansion gathering took 0.234034 seconds and warm gathering 0.034016 seconds. Expansion reused the first 10 snapshots. Both warm refreshes ran zero checks. These fixtures establish bounded discovery in the tested case; they do not establish semantic relevance or net savings.

[evidence: root `self-check` invocation] The current machine reported the Python floor met, writable local SQLite storage and successful isolated synthetic gather/check/select behavior. Its synthetic fixture was removed afterward and no real decisions were touched. The detached-clone test separately exercised that same self-check from another directory.

[limits] No native Windows machine or actual Python 3.9 interpreter was available. Syntax and portable-name tests are bounded evidence; the first Windows use should run self-check. Matching is lexical and can miss synonyms or over-rank common words; the agent must judge full context. Files that are unreadable, prohibited, special or linked cannot be fully preserved; safe partial snapshots carry diagnostics and cannot be admitted. Hashing buffers one contribution at a time, so memory depends on the largest bundle. Local state assumes a trusted owner filesystem; actor fields are not access control, and source files should not be concurrently rewritten during an ask. Observable per-file changes during reads are diagnosed, but gathering is not an atomic snapshot of the whole projects tree.

## Files, friction, resources and continuation

[evidence: delivered layout] New generic files are `capability/knowhow.py`, `capability/access/{__init__,engine,cli}.py`, `capability/USE.md`, `capability/OWNER.md`, `capability/.gitignore`, and `capability/tests/test_access.py`. No standard file, standard checker or original standard test was edited. Personal settings, snapshots, events, costs and evidence are only beneath the ignored `.local/`.

[interp: implementation choices] SQLite keeps decision updates transactional; immutable ordinary directories make selected kits directly accessible. Merge chains are deliberately rejected: undo incoming merges before merging a former target onward. This keeps equivalence decisions explicit without inventing combined text. Exclusions and declines bind exact content IDs; newly changed bytes have no inherited admission. Changing the configured root creates a fresh namespace rather than moving decisions. A fresh clone restores the generic capability empty, not the local decision/use histories; those require separately preserving `.local/`, as documented.

[evidence: implementation and test work] During validation, one test-file write used a prefix relative to the wrong working directory and failed before writing; I corrected the path, then ran the full intended tests. Review found that malformed applicability values needed type guarding in matching and that reversed incoming merges must be judged by effective events rather than historical events; both were corrected and covered by tests before the real run. These were implementation adjustments within the brief. No standard change or intent change was needed.

[evidence: operations this run] Resources used: this subordinate instance, local file/command tools, Python's standard library (including SQLite, hashing, JSON, temporary synthetic fixtures and unittest), the delivered method and existing standard. No subordinates, third-party dependencies, network, background process, commits or pushes were used. The real gathering path reads projects and writes only the capability's ignored store; tests compare source bytes before/after gathering and exercise secret-read guards. The executive holds the first real admission pass and the entry-line decision. I end this run with local state retained for that work.
