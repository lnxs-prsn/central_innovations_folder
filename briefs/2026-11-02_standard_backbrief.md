# Standard, context record and check — backbrief, 2026-11-02

## Position and situation

[evidence: `briefs/2026-11-02_standard.md`, parts 2 and 5] I am subordinate to Central's executive. My responsibility is the standard, its context record and its presence check under `capability/`. I decide their implementation and tests within the brief; the executive holds the sibling interface and admission decisions. No subordinates are assigned. GO for this subordinate's build is not issued.

[interp] The brief is valid. Reading the existing contract exposes compatibility details to settle in the superior's backbrief check, rather than a change to the CEO's purpose. This run supplies only this backbrief and ends. I have read the full assigned brief, the designated edition's ENTRY and START_TEXT, the local delivery and experience records, the CEO intent, the current executive re-brief, and the context investigation report. Method guidance comes from fixed edition `2026-11-01c`; project direction comes from Central's records.

## Understanding and main effort

One level up — executive's accepted understanding, `BRIEF.md`, third re-brief:

> whatever any project learns is there for any other project to draw on, with the situation it came from, whenever that project's work calls for it: new or long unused, on whatever machine it is cloned to. Each project takes only what fits; you can withhold what misleads; it costs less than it saves. The capability stands alone: anyone who clones it has it working with an agent and Python. It reaches projects by being pointed to, never by placing anything in them.

Two levels up — CEO, `intent.md`, Intent and Main effort:

> Make all my projects learn from each other, so that what any project learns becomes a foundation every project builds on, instead of being reinvented.

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

[interp] I will make the circumstances needed to judge reuse explicit and portable, and give contributing agents a mechanical way to find omissions while they still know those circumstances. I reject treating a complete form, a section heading, or a copied evidence account as proof that advice works. The check establishes recorded presence and structure, with unresolved human judgments visible.

[interp] My main effort is the context record and its single authoritative definition. Both the readable instructions and the checker must depend on that definition, because an independently maintained checklist would allow the very context loss this assignment addresses.

## Proposed record interface

[proposal] Keep `PATTERN.md` as the explanation and embed one fenced JSON context object in an additional final section. Do not add a metadata sidecar: the existing directory contract permits the pattern and its kit. JSON uses only Python's standard library and keeps machine-readable context with its explanation. Existing six explanatory sections remain the narrative contract; the context object supplies structured distinctions, rather than attempting to infer them from prose.

[proposal] Full record, version 1; all fields below are required unless marked conditional. Required lists may be explicitly empty only where stated. Missing knowledge is `null` with an accompanying reason, never invented content; the checker distinguishes recorded unknowns from supplied substantive context.

| Field | Content and requirement |
|---|---|
| `schema_version`, `standard_version` | Supported record and governing standard identifiers. |
| `id`, `title`, `summary` | Contribution's kebab identifier, readable title and concise purpose; identity is not a claim of semantic equivalence. |
| `problem`, `mechanism` | Situation addressed and what the technique changes. |
| `origin` | `project`, `situation`, `environment`, `developed_on`, `development_kind`, `development_account`; distinguishes invention or material refinement from imported advice. Unknown date is recorded as unknown, not replaced by a check date. |
| `applicability` | `fits` (nonempty), `does_not_fit`, `prerequisites`, `adaptations`; the last three can be empty only with an explicit account of what was considered. Exclusions here describe technical fit, not CEO withholding rules. |
| `use` | Ordered instructions and expected outcome. |
| `evidence` | Nonempty list: each item has `claim`, `outcome` (success/failure/mixed), `project`, `situation`, `occurred_on`, `locators`, and `verification`. At least one dated, locatable account of successful real use is required for a fully supplied pattern claim. Failures belong here too. |
| `evidence[].verification` | `status` (unchecked/checked/unavailable), `checked_on`, `checked_by`, `scope`, `result`, `reason`; check details required when status is checked, unavailability reason when unavailable. These are contributor reports, never a truth judgment by this checker. |
| `limits` | Known failure conditions, uncertainty and residual limits; an explicitly considered empty list is distinct from an omitted field. |
| `evolution` | `origin_state` (aligned/diverged/unknown), `assessed_on`, `locators`, `deltas`, `reason`; divergence details required when diverged, an explanation when unknown. Does not imply automatic synchronization. |
| `assets` | List of `path`, `kind`, `purpose`, `adaptations`, `dependencies`, `context_ref`. Paths are contribution-relative under `kit/`; context references resolve to the containing explanation and relevant context fields. At least one deployable asset for full compatibility. |
| `relationships` | Optional list of related contributions with relationship, locator and rationale; no inferred equivalence or merge decision. |

[proposal] A JSON check result adds an envelope, separate from contributor claims: `standard_version`, `record`, `discovery`, `checks`, `presence_complete`, `review_required`, `limitations`. Each check has `rule_id`, `field`, `state` (present/missing/invalid/unknown), and an actionable message. Malformed records still return diagnostics; no invented replacement record is produced. Unknown essential origin or evidence data keeps `presence_complete` false even though the unknown is honestly recorded. Reported evidence verification never makes the checker certify truth.

[proposal] Compact `discovery` is derived, never separately authored: identifiers and versions, title, summary, problem, `applicability.fits`, `applicability.does_not_fit`, a limits/unknowns indicator, reported evidence outcomes and verification statuses, asset kinds, and `presence_complete`. It includes a locator to the full context in `PATTERN.md`. It supports screening only; the sibling must retain the full record and resolve it before selection. The sibling owns supplying-location lists, content hashes/revisions, admission status, comparisons and decisions; these are not origin facts and do not enter my authoring schema. Multiple copies do not create independent evidence.

## Definition, generated standard and check

[proposal] One declarative Python definition records field names, types, requiredness, allowed values, conditional rules, explanatory section identifiers, diagnostic wording, and human-review obligations. A generic interpreter evaluates those rules; a renderer produces `STANDARD.md` and a contribution skeleton from the same objects. There is no separately coded inventory of required context. A generation comparison check detects edited or stale generated documentation. Human-review rules are rendered and reported as such, rather than disguised as executable proof.

[proposal] The public callable interface will be `check_contribution(path)` returning the result envelope and `discovery_record(record)` deriving the compact view. A direct Python command accepts an explicit contribution path, with readable or JSON output. Proposed exit codes: 0 for mechanically complete, 1 for missing/invalid/unknown required material, 2 for usage or read failure. Every successful output still states that presence is not truth and admission remains a separate decision. No execution of contributed assets, network access, shell invocation, symlink traversal or changes to inspected contributions.

## Compatibility and points for the superior's check

[evidence: `/home/mr/Desktop/python/github_clones_working_on/dev_trainer_tool_full_project/innovations/CONTRIBUTING.md`, sections 1–4] I read one current copy in full. The context report establishes byte equality across its ten discovered copies; I have not independently repeated that discovery. Its requirements include successful real-project invention/refinement, dated citable evidence, six named ordered sections, at least one deployable kit file, generic kits, a matching parent index row, contribution procedure, and recording divergence and counter-evidence.

[proposal] I will establish compatibility with a requirement-by-requirement matrix in the report: mechanical enforcement where possible, contributor declarations and explicit human review for semantic and procedural requirements. Synthetic examples will exercise the matrix. A contribution-only command can inspect a supplied kit and its parent index but cannot establish that evidence is true, that a kit contains no unidentified project detail, that synchronization happened in the same sitting, or that a prescribed commit procedure was followed. Such obligations remain part of the standard and are reported for review; a mechanical pass must not claim overall compliance or admission. Parent index/procedure obligations need coordination with the store sibling and executive, not silently disappear from the standard.

[interp; proposed resolution] The brief's optional `kit/` describes accepted input to the check, not an exemption from the inherited contract. The check will accept a folder without a kit and report that deployable material is missing; it cannot label it fully complete. Untested ideas may be diagnosed without becoming admitted patterns or gaining directory rights.

[point requiring superior resolution before build] Literal heading compatibility needs a narrow interpretation of the prohibition on copied text. I propose retaining the six required section names as structural identifiers in the definition and generated skeleton while writing all normative prose afresh and copying no contributions or contract prose. If the prohibition includes those literal identifiers, it conflicts with exact legacy section compatibility. Please settle that interpretation in the recorded GO; I will not resolve it by silently loosening the legacy contract. This concerns subordinate implementation boundaries, not a proposed change to CEO intent.

## Implied tasks, files and resources

[proposal] After GO I will: finalize the approved record and rule definition; implement its generic reader, renderer and checker; generate the standard and skeleton; expose the compact/full result interface to the sibling through the superior; test omissions and conditional rules using invented contributions; establish the compatibility matrix; and write the assigned outcome report. Record-shape changes after GO return to the executive before implementation because the sibling depends on them.

[proposal] My files under `capability/`: `standard/definition.py`, `standard/render.py`, `standard/check.py`, `standard/__init__.py`, generated `standard/STANDARD.md` and `standard/PATTERN.template.md`, standalone `check_contribution.py`, and `tests/test_standard.py`. No `USE.md`, store/access code or personal examples. The sibling may import my package without me changing its files. No further division is needed: schema, rendering and checking are one tightly coupled responsibility of manageable size.

[proposal] Meaningful tests will cover loss of required context, unknown versus substantive values, unverified versus reportedly checked evidence, failures alongside successes, drift reporting, missing kits, asset/context resolution, parent index diagnostics, malformed JSON, generated-document consistency, and invocation from another working directory. Use temporary synthetic fixtures and standard-library unittest. Test portable path rules and reject symlinks without following them; do not claim native Windows execution from Linux tests. The sibling sets the shared Python minimum; avoid unnecessarily recent language features and refer version conflicts to the executive.

[evidence: this run's operations] Resources used for this backbrief were this subordinate instance and local read-only file access, including the fixed delivered edition. Only this backbrief is written. No network, builds, subordinate runs, commits, pushes or other-project writes occurred. [limit] I have no native Windows test evidence or independent verification of source incidents. My eventual check can prove structural presence and local resolvability, not semantic truth or fit. The executive receives this backbrief when this tracked run ends; build and the report remain for the resumed run after its recorded GO.
