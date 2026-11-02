# Publication backbrief — subordinate 3 — 2026-11-02

## Position and received direction

[evidence: `briefs/2026-11-02_publication.md`, parts 2, 4–5] I am subordinate 3 to this project's executive, the one writer for `capability/`, including the standard. My decision rights cover formats, interface, layout, identities, matching and tests. Admission, merge, retirement and exclusion decisions remain with their assigned authorities. I have no subordinates. My only present deliverable is this backbrief; building follows the executive's recorded GO and resumed run. I neither publish into this project's `published/` nor commit or push.

One level up, quoted from the task brief, part 2, attributed there to `BRIEF.md`, “Publication re-brief (replacing)”:

> Every project's learning becomes a foundation for the others, carried with its context. Under this brief, know-how moves only by publication: a project that takes the capability offers what it learns in its own published part, complete and fixed, with its context; the capability reads only published parts, offers back a published catalogue, and is itself published, with how to use it and how to offer. Who commands the organization, and its shared state and pause or stop, sit above every project; the capability holds none of it.

Two levels up, `intent.md`, Intent and Main effort:

> Make all my projects learn from each other, so that what any project learns becomes a foundation every project builds on, instead of being reinvented.

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

## Understanding and main effort

[interp] The task brief is valid. I will make publication the boundary for both incoming knowledge and outgoing access: an offering project deliberately publishes a complete checked bundle; the curator retains verified publications and publishes its own fixed catalogue; a taker reads that catalogue and keeps its decisions and costs at home. Taking the capability does not grant it command over projects.

[interp] Rejected interpretation: replace `innovations/` scanning with scanning every project for a `published/` folder, while retaining shared clone-side records. That still invents discovery outside the given published-part list and still lets takers write into another project's folder.

[interp] My main effort is the complete, fixed offer and its verified ingestion. Identity, admission, preservation and the catalogue depend on getting that boundary right. A manifest is an integrity check, not evidence that the content is true or that a named actor is authorized.

## Offer form, identity and placement

[interp: proposed design] Each participating project initializes a random UUID once in its own `.knowhow/project.json`. Its public index declares that same ID. Moving or reassigning the project preserves this file, its records and its published part; no path or organization name becomes its identity. A deliberate fork initializes a new UUID. Conflicting claims to one UUID are diagnosed rather than silently combined. Labels and current locations are descriptive.

An offer lives at `published/knowhow/offers/<offer-manifest-sha256>/`. It contains `OFFER.json` and `bundle/<contribution-slug>/PATTERN.md` with `bundle/<contribution-slug>/kit/`. Context stays in PATTERN's existing structured record; there is no separately authored duplicate. The manifest records format and standard versions, content ID, contribution slug and a sorted inventory of relative paths, sizes and SHA-256 hashes. Its own hash is recorded in the index, avoiding a self-hash.

The content ID hashes a deterministic, length-framed sequence of sorted bundle-relative paths and exact bytes. Supplier UUID, source path, timestamps and display labels stay outside that content hash, so exact copies deduplicate across suppliers. The standard's originating-project and evidence accounts remain intact inside PATTERN; supplying copies do not become independent successes. Each supplier's index links its UUID, offer manifest hash and relative manifest path. Similar content stays separate until an explicit curator decision. Changed bundle bytes produce a new content ID and need new admission; changed publication metadata produces a new offer manifest. Existing offers are never overwritten.

`offer` reads only a specified contribution in the running project's own folder, performs the standard check before publication, stages the complete copy, checks the staged bytes again, then installs the fixed offer and updates only a delimited know-how block of that project's `published/INDEX.md`. Existing index prose and method declarations survive. An identical repeat is idempotent; a hash conflict or incomplete check fails without publishing a partial offer. The contribution remains exactly PATTERN plus kit; manifests are outside it, preserving standard 1.0's layout.

## Curator input, retention and catalogue

[interp: proposed design] `ingest --published-parts LIST.json` receives an explicit versioned JSON list of published roots, with locators relative to the list file where possible. It is an adapter input, supplied by whatever organization arrangement exists. It has no projects-folder setting and never constructs or searches a parent projects tree. Missing input produces a clear missing-resource result before creating state or reading publications. An explicitly empty list is valid empty input.

For each supplied root the reader opens only `INDEX.md`, then the offer manifests named by its know-how block and their enumerated files. All publication paths must stay beneath that published root. No evidence locator is fetched. Reject absolute or traversing manifest paths, links/reparse points, prohibited names, special files, ambiguous portable names, duplicate paths and hash/size mismatches. Validate the complete manifest before reading bundle data; check and retain the verified staged copy, not a later reread of a changing source. A bad offer is diagnosed without admission; other independent valid offers can proceed with an explicit partial-failure summary.

Curator state lives in the curator project's `.knowhow/curator/`: SQLite decisions and ingestion/cost history, and immutable retained offers by content ID, with all supplying origins. It is separate from executable code and never inside a fixed capability edition. Missing, moved or withdrawn source locations are historical observations, not deletions of retained content. Repointing the input list to a new published root with the same project UUID updates location history without losing decisions. Unadmitted offers are inspectable by the curator, not returned to takers as reusable knowledge.

`publish-catalogue` produces a fixed edition under the running curator project's `published/knowhow/catalogues/<edition>/`. It includes a bounded discovery index, complete retained bundles needed for admitted content, supplying-origin records, check results, decision reasons and effective admission/merge/retirement/exclusion policy. Historical decision records and restricted or retired material remain retained; eligibility controls the capability's offer and selection. The catalogue is self-contained: full context and kits resolve inside it after every supplier has disappeared. Its manifest inventories and hashes every included file; the curator's index identifies the current edition and manifest hash. No pointers into private curator state occur in the publication.

The publisher writes a complete staged edition before changing the current-index block. Readers verify the named manifest and used files; partial or altered editions fail closed. Exact retained copies remain one content with multiple supplying origins. A merged source and its adverse evidence remain available for review, with restrictions propagated to its surviving target as in the current engine.

## Takers, policy and records

[interp: proposed design] A taker supplies its own explicit project root and the curator's published index. `ask` reads bounded discovery and policy; `select` loads full context and kit files only for selected IDs. Neither command ingests suppliers. Both resolve the current catalogue from that index and verify policy before applying eligibility, including global and project-UUID exclusions, retirement, merges and that taker's local declines. An earlier candidate ID grants no later access by itself. Preserve the existing default five / maximum twenty candidates and 12000-byte candidate-list bound, deterministic matching and visible negative-condition matches.

Taker records live only in its `.knowhow/`: stable project ID, append-only declines and reversals, inspection/use accounts and command costs, plus catalogue identity/locator history. `select` records inspection, not successful reuse; `log-use` records caller-reported outcomes and savings estimates separately from measured elapsed time/output bytes. Bytes are not tokens. The curator records its own command costs only; there is no organization capacity aggregate. A standalone `check_contribution.py` remains read-only; the project-scoped `knowhow.py check` can record its cost locally.

Catalogue identity is the manifest hash; a path is a replaceable locator. A move requires an explicit replacement locator and verification of the retained identity, not a search for a matching name. Where the index names a new current catalogue, takers verify and record that new identity before using it. Keep old edition identities for interpreting past use.

[interp: practical limit] A new curator decision affects takers after the curator publishes it. Each ask and select rechecks the supplied current index; if that index or its current policy is unavailable or invalid, access fails rather than falling back silently. A disconnected copy cannot know about a later exclusion, and these mechanisms do not prevent direct filesystem reading of already published bytes. I will state that boundary in both guides; no polling, authentication service or command-level stop mechanism is implied.

## Proposed command interface

[interp] Every stateful invocation requires `--project PROJECT_ROOT`, explicitly identifying the folder of the agent running it; the tool cannot authenticate that assertion. Writable paths are derived beneath that root, checked for containment and links, and refused inside the loaded capability edition. No arbitrary external state/output override. All examples retain `--json` support.

| Command | Purpose and additional inputs |
|---|---|
| `init` | Initialize this project's stable identity and empty local records. |
| `check CONTRIBUTION` | Check an addition inside this project; compact diagnostics and local cost record. |
| `offer CONTRIBUTION` | Check, freeze and index an offer in this project's published part. |
| `ingest --published-parts LIST.json` | Curator imports only explicitly listed publications. |
| `review [ID]` | Curator inspects pending/full retained offers and diagnostics before deciding. |
| `admit ID`, `merge ID --into ID`, `retire ID` | Curator appends attributed, reasoned decisions. |
| `exclude ID --all` or `--project-id UUID` | Curator records the CEO's scoped exclusion. |
| `decisions [ID]` | Inspect curator decision history. |
| `publish-catalogue --edition NAME` | Freeze catalogue and update this project's published index. |
| `ask --catalogue INDEX --task TEXT [--limit N]` | Taker receives compact candidates. |
| `select ID... --catalogue INDEX` | Recheck policy and return selected full context and kit locator. |
| `decline ID --reason TEXT --actor ACTOR [--undo]` | Append this project's decline or reversal. |
| `log-use ID --outcome TEXT [--saving-note TEXT]` | Record this project's actual-use account. |
| `self-check` | Exercise invented publication, ingestion, decision, catalogue and taker flow in temporary directories. |
| `pack-capability --edition NAME` | Stage a generic fixed capability edition inside this project's local staging area. |

Curator decisions retain required actor/reason and reasoned `--undo`; actor text is attribution, not authority verification. `exclude --project-id` separates the target's stable identity from the running curator's `--project` root. A fresh empty clone can initialize, check, self-check and publish an empty catalogue without real projects or offers. Ask against an empty valid catalogue returns no offers.

## Existing work: keep, change, remove

[evidence: code and guides read] The current `access/engine.py` hashes and snapshots bundles, stores SQLite events and use records, matches lexically, bounds candidates and propagates restrictions through merges. `access/cli.py` configures a projects root, refreshes by gathering on ask/select and writes beside the clone. `check_contribution.py` imports before disabling bytecode writes; the main `knowhow.py` already disables them.

[interp] Keep the standard's schema, generated template/document agreement, presence-versus-truth distinction, conditional validation and compact check projection. Keep the matching and decision semantics where they fit publication, including rollback and non-destructive reversal. Rework snapshot handling into verified manifest ingestion, separating curator storage from a read-only catalogue reader and project-local journals. Remove `configure`, `load_root`, `gather`, ancestor project-marker discovery, path-based project IDs, root-hash namespaces, automatic supplier refresh during ask/select and every clone-relative `.local/` write. Replace the guides' gathering, ownership and recovery claims. Prevent bytecode writes in all executable entry points before local imports.

The standard's parent-index and contribution-procedure review duties still apply to an offering project's working collection; the publication envelope does not waive them or copy that private collection index into public offers. Document that distinction in the use guide. No standard weakening or new automatic admission.

## Implied tasks, checks and fixed capability edition

[interp] After GO I will implement the identity and manifest contracts first; then offer publication and ingestion/retention; then curator decisions and catalogue publication; then taker access and local records; then guides, edition packaging and integrated checks. Closely coupled paths stay with one writer. No division or additional agents are needed for this coherent task.

Tests will use only invented projects and offers in temporary directories. Retain meaningful standard and decision tests; replace tests tied to project-tree scanning and clone-local storage. Verify missing-list zero activity, index preservation, tamper rejection, path/link/reparse/prohibited-file rejection before content reads, complete-context retention after source disappearance, duplicate origins, changed-content readmission, UUID continuity after moves, decline/exclusion at both stages including merge predecessors, interrupted publication, empty recovery and bounded discovery with tenfold growth. Check command write sets, including execution from a read-only fixed capability edition and independent takers whose records never mix. Run the suite, generated-document check and Python 3.9 syntax check after implementation. Report the actual interpreter/OS exercised; a Linux run does not establish Windows execution.

`pack-capability` will use an explicit allowlist: entry scripts, required `access/` and `standard/` sources, generated standard/template, `USE.md`, `OWNER.md`, tests and edition/update instructions. Include all runtime dependencies, a versioned `EDITION.json` file inventory with SHA-256 hashes, and an external manifest hash for the executive to index. Exclude `.git`, caches, private state, curator catalogues, project publications, personal paths and real innovations. Repacking identical content must give the same content identity; changed content needs a new edition. Stage only beneath the running project's `.knowhow/`; in this project's build run keep that stage inside `capability/` to respect my write boundary. The executive checks the report and publishes the final edition into this project's `published/`; I supply the means and staged artifact, not that publication.

## Resources, limits and handoff

[evidence] I read the full assigned brief, taken edition's ENTRY/START_TEXT and adoption note, local locator, relevant project records, guides, standard and implementation/tests. The locator resolved without movement; the recorded edition `2026-11-02b`, manifest SHA-256 `01eafeda2451e2bfed572aaf31c938c3914037a56480c877b91a299d90087cd0` and every listed file hash verified. Resources used: this one subordinate instance and local reads plus this backbrief write; no network, other-project investigation, build, test run, commit or push.

[interp] The organization's published-part list remains unavailable. That blocks real intake, not implementation or synthetic verification. No real offers have been inspected or admitted in this run. M1–M6 reach only what projects choose to publish and take; retained published evidence can still be unavailable for independent verification, which stays explicit. M10 instrumentation enables comparison, but actual savings remain unproven until real use accounts arrive. No change to the CEO's desired outcome is proposed and no decision from the CEO is needed for this design.

Control-loop handoff: this backbrief is complete. I end this run now, with building untouched, for the executive to receive and check it. After recorded GO and resumption, I will build, test, write `briefs/2026-11-02_publication_report.md` with outcome, friction and resources, and end that run. If a discovery would change what the CEO wants, I will record it in that report and end instead of continuing.
