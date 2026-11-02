# Store and access — backbrief, 2026-11-02

## Position, situation and intent

[evidence: `briefs/2026-11-02_access.md`, parts 2, 5 and control loop] I am the store/access subordinate to Central's executive. My area is the capability outside the completed standard: gathering, preservation, copies, offers and selection, decision mechanisms, use/cost records, local settings, entry and command. I decide implementation and interfaces within that brief. Admission, merge and retirement decisions belong to the executive; exclusions belong to the CEO and project declines to that project's executive. No subordinates are assigned. I will not modify `standard/`, `check_contribution.py` or `tests/test_standard.py`; a needed standard change goes back to the executive.

[interp] The brief is valid. The available standard separates presence checking, discovery and full context, which supports this assignment without a record-shape change. Existing contributions may produce no cross-project offers until their context is completed and the executive admits them; that is an expected result, not grounds to relax admission. [evidence: `capability/standard/STANDARD.md`; `briefs/2026-11-02_standard_report.md`; `MAP.md`, Leg 10 and current work]

One level up, the accepted executive understanding in `BRIEF.md`, part 6, third re-brief:

> whatever any project learns is there for any other project to draw on, with the situation it came from, whenever that project's work calls for it: new or long unused, on whatever machine it is cloned to. Each project takes only what fits; you can withhold what misleads; it costs less than it saves. The capability stands alone: anyone who clones it has it working with an agent and Python. It reaches projects by being pointed to, never by placing anything in them.

Two levels up, CEO, `intent.md`, Intent and Main effort:

> Make all my projects learn from each other, so that what any project learns becomes a foundation every project builds on, instead of being reinvented.

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

[interp] I take this to mean: make potentially useful learning cheap to find, and make its circumstances and limits unavoidable when the receiving agent chooses to inspect it. Discovery screens; full context supports judgment; neither matching nor a complete presence check admits a contribution or proves fitness. I reject interpreting availability as copying every contribution into every project, automatically selecting lexical matches, or counting supplying copies as independent successes.

## Main effort and implied tasks

[interp] My main effort is the path from a task-specific compact offer to explicitly selected full context and a usable retained bundle. Preservation, identity and decision enforcement support that path. After recorded GO I will:

1. Establish the portable command, local projects-folder setting and unambiguous calling-project identity.
2. Gather every bounded `innovations/` collection on request; preserve versions and locations, hash exact copies, and reuse checks/projections when their content and standard have not changed.
3. Implement retained decision events and their effective state, with reason and actor attribution, before exposing cross-project offers.
4. Implement ranked, bounded discovery and explicit selection with the full explanation, context, check state and bundle locator; enforce exclusions, declines and retirement again at selection.
5. Add check, decision, self-check and use/cost interfaces; document the entry and recovery behavior.
6. Verify with invented contributions, including tenfold growth, nested projects, changed/deleted sources, empty clones and command invocation from another directory. Report results against the brief, remaining limits, friction and actual resources.

## Proposed single command

[interp: implementation choices throughout the remaining design] The entry is `USE.md`, and the executable is `python /path/to/clone/knowhow.py SUBCOMMAND ...`. The path is supplied by the CEO's arrangement; no installation, shell script or working-directory change is required. Human-readable output is compact by default; `--json` supplies structured output. Paths containing spaces are quoted by the caller in the normal platform syntax.

| Interface | Intended behavior |
|---|---|
| `ask --task TEXT [--project PATH] [--limit N] [--offset N]` | Refresh sources first. Return bounded ranked candidates, immutable content IDs, screening context and reasons for matches, plus result counts and pagination. Own-project incomplete material is separately bounded and visibly diagnosed. |
| `select ID [ID ...] [--project PATH]` | Refresh and recheck effective decisions, then return each selected contribution's complete PATTERN text, structured context and check result, admission/provenance information and absolute retained bundle path. Missing/changed evidence remains labeled; kit files stay in the bundle and are not executed. |
| `check PATH [--json]` | Delegate to `standard.check_contribution`; show completeness, counts, actionable missing/invalid fields and the standing review notice. Detailed diagnostics remain accessible in JSON. Does not require projects-folder configuration or gather other projects. |
| `decline ID --reason TEXT [--project PATH] [--actor TEXT]` | Record the project's executive's decline for that project only. An explicit `--undo` with a reason appends a reversal rather than erasing history. |
| `exclude ID (--all \| --project PATH) --reason TEXT --actor TEXT` | Record a CEO exclusion at global or project scope. An explicit reasoned `--undo` appends its reversal. Effective exclusions apply to both offers and selection, including own-project offers. |
| `admit ID --reason TEXT --actor TEXT` | Record the executive's admission of this exact retained version after full review. Refuse mechanical incompleteness; passing is not itself admission. |
| `merge ID [ID ...] --into ID --reason TEXT --actor TEXT` | Record the executive's explicit relationship and the surviving contribution. Retain all inputs and their histories; do not synthesize or edit their text. The target must already be admitted and complete. |
| `retire ID --reason TEXT --actor TEXT` | Record the executive's withdrawal from offers, preserving the bundle, adverse evidence and reason. Reinstatement requires an explicit reasoned decision. |
| `self-check` | Report interpreter/platform, read/write ability in capability-local state, standard integration, configuration state and synthetic end-to-end behavior; never infer a projects folder or alter real decisions. |
| `configure --projects-folder PATH` | Validate an explicitly provided directory and save it locally; also permits a later machine-local change. |
| `log-use ID --outcome TEXT [--saving-note TEXT] [--project PATH]` | Record a caller's actual use/outcome separately from inspection, with optional attributed saving estimate. Merely selecting is logged as inspection, not successful use. |

A read-only `decisions [ID]` view will make reasons and effective state inspectable. Operational/read failures will be distinct from incomplete checks and empty offers. Decision commands require explicit actor/role attribution, but are not an authentication system: local Python cannot establish that the invoking person is the CEO. `USE.md` will state who may use them. I will implement and test mechanisms using isolated synthetic state; I will enter no real admission, exclusion, decline, merge or retirement decisions.

## Calling project, including nested projects

[interp] The caller can always specify `--project PATH`, including a new directory with no repository or innovations. The normalized absolute directory must lie inside the configured projects folder; relative references in the command resolve from the caller's working directory, never from the clone.

Without `--project`, use the nearest ancestor, starting at the working directory, with its own `.git` file/directory or direct `innovations/` directory, stopping at the configured projects folder. The closest marker wins, so a nested project has a separate identity from its containing project. With no marker, require `--project`; guessing an arbitrary ancestor could silently scope a decline to the wrong project. Explicit `--project` also resolves a nested new project without markers or a directory that happens to contain an unrelated innovations collection. Gathering assigns a collection to the directory immediately containing its `innovations/`, not to an enclosing repository.

Project keys are normalized paths relative to the configured projects folder, using portable separators and native case normalization; basenames and contributor-stated `origin.project` are not identity. A path rename is a changed identity and will not silently inherit decisions. Changing the configured root will require explicit confirmation of whether it represents the same relocated project tree; unrelated roots receive distinct local namespaces. No project IDs or files are written into projects. Symlink traversal is rejected, and containment is checked before reading.

## Matching and cost

[interp] Matching is deterministic Python text processing, requiring no model, embedding service or provider. Tokenize and case-normalize the task and retained explanation/context; rank overlap with higher weight for title, problem and positive fit than general prose. Preserve negative fit, prerequisites, adaptations, unknowns and limits in the stored searchable material. Match reasons identify shared terms; negative-condition matches warn rather than asserting semantic incompatibility from keywords alone. Stable content IDs break ties. No lexical match means no claimed relevant candidate; an explicit browse option can inspect the remaining admitted collection in bounded pages.

Admission, retirement, merge redirection, global/project exclusion and project decline filter eligibility before ranking. An unadmitted version is visible only to projects supplying that exact content, with its check result and missing context; a copy does not give another project access to unrelated unadmitted material. Similar contributions remain separate unless the executive records a merge.

Default offers will have a small fixed candidate count and a serialized-output budget, with a cursor/count for omitted candidates and a per-row truncation indicator. Discovery is derived through the existing standard interface; no separate authored summaries are introduced. Selection has no silent context truncation: the caller controls output by selecting fewer IDs. Tests will measure output bytes and scan/check reuse at baseline and tenfold volume, rather than claim a token count from byte counts.

Every command records its operation, project where relevant, IDs, elapsed time, scan/hash/check counts and exact response UTF-8 bytes in local use records. Task text need not be retained. Actual use and caller-estimated savings are separate attributed records. These measurements permit comparison; they do not by themselves prove net savings.

## Store, gathering and recovery

[interp] Use `.local/` beneath the clone, wholly git-ignored: `settings.json`, a standard-library SQLite catalog/event log, and immutable `bundles/<sha256>/` snapshots. SQLite keeps catalog updates transactional; snapshot staging and atomic completion keep interrupted copies out of offers. Snapshots are ordinary directories so selected bundles are directly resolvable on Linux and Windows.

Content identity hashes sorted portable relative paths and exact bytes for the entire permitted contribution bundle, with unambiguous framing. Location, timestamps and admission are outside the hash. Identical bundle content has one identity and multiple current/historical supplying locations; changed prose or kit bytes make a new version requiring its own admission. Names alone never merge contributions. Keep the original bundle even when the check fails, where safely readable; unreadable or prohibited entries remain explicit diagnostics rather than falsely claiming a complete snapshot.

Walk only the configured projects tree, discovering collections even in nested projects. Prune repository metadata, environment/dependency caches and the capability's own `.local/` store, and never follow symlinks. Skip prohibited secret names/paths from the brief without reading or printing their contents. Do not execute kits or fetch evidence. Detect relevant source additions, edits and removals on every ask; retain old snapshots and mark missing locations instead of deleting contributions. Hash ordinary content each refresh rather than treating unchanged timestamps as proof; reuse immutable snapshots, checks and discovery by content hash and standard version. Thus unchanged refreshes still traverse/hash source bytes, but avoid reparsing and recopying. Report that cost honestly.

The catalog stores check results, complete context, discovery, source observations and immutable decision/use events. Derived indexes can be rebuilt from snapshots and events; recovery must retain authoritative decisions and history. Exclusions/declines attach to immutable content identity. Merge filtering also checks restrictions on the merged inputs so redirection cannot bypass a restriction. Newly changed content remains unadmitted, rather than silently inheriting old approval. Nothing is garbage-collected automatically.

With no state, the clone starts with zero contributions and no personal settings. Commands needing gathering ask for the projects folder once if interactive; without interactive input they return a clear instruction to supply it through `configure`. They never search for it. The local store is not backed up by cloning: source projects repopulate it; local admission/decision/use history is absent on a lost machine unless its owner separately preserves that local state. `USE.md` will distinguish empty capability recovery from recovery of personal records.

## Entry, files, division and resources

Proposed first line of `USE.md`:

> Find reusable project know-how with its original context; open this file when your task may benefit from what another project has learned.

[interp] The rest supplies portable command examples, configuration and project selection, ask/select/check/decline instructions, review responsibilities, the standard link, decision roles, local-state recovery and cost interpretation. It addresses any agent and assumes no provider or Central records.

Proposed new layout: root `knowhow.py`, `USE.md`, `.gitignore`; package `access/` containing command handling, project/configuration identity, gathering, store/events, matching and output accounting; `tests/test_access.py` with invented fixtures. Existing standard files remain untouched. Personal data lives only under ignored `.local/`; synthetic temporary fixtures are separate. Verification will inspect tracked/untracked state to ensure real material cannot be accidentally included by ordinary staging.

[interp] No division is needed now: identity, decision eligibility and selection are tightly connected, and the standard interface is already delivered. I propose no subordinates. Resources available: this subordinate instance, local read/file tools, Python standard library and the existing standard. No network, third-party dependency, background process, commits, pushes or writes into other projects are needed. I can implement and validate on available Linux; native Windows and Python 3.9 runtime behavior require those actual runtimes. Syntax/portable path tests and the self-check provide bounded evidence, not a claim of native execution. If a standard change or change to the CEO's intended outcome becomes necessary, I will refer it to the executive and stop dependent work.

[evidence: this run] Read the full assigned brief, fixed edition `ENTRY.md` and `START_TEXT.md`, local delivery/locators, standard, standard report and relevant local direction/experience. No capability build, tests, gathering against the real projects tree or decision writes were performed. This backbrief is the sole deliverable written. GO is not issued in the assigned brief. I end this run for the executive to receive and check it; build resumes only after recorded GO.
