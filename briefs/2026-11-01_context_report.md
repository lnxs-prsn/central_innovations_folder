# Context survival investigation — 2026-11-01

## Outcome against the brief

[interp, grounded in observations below] Preserve the contribution's originating situation, applicability and exclusions, evidence with its verification status, known limits, and the relationship between explanatory material and deployable assets. Preserve those distinctions when recognizing equivalent contributions and when presenting material for selection. A name, index description or deployable file alone is insufficient for a sound applicability judgment.

[evidence: task brief, “Supervisor's check and GO — 2026-11-01”] This investigation follows the recorded GO and its adjustment requiring the receiving project's selection-time information as input to the entry sibling. It makes no admission, merge or retirement decisions and selects no implementation. [interp] Nothing found changes the CEO's intent. The expectation of differing admission standards remains unconfirmed by the current files examined; this limits the evidence, rather than changing the purpose.

## Direction and interpretation

One level up — `BRIEF.md`, part 3:

> What: establish a recoverable, provider-independent capability for projects to contribute, discover, and selectively use shared know-how in order to make each project's learning a usable foundation for the others.

Two levels up — CEO, `intent.md`:

> Make all my projects learn from each other, so that what any project learns becomes a foundation every project builds on, instead of being reinvented.

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

[interp] Interpretation taken: determine which distinctions a receiver needs to judge reuse, using actual contributions rather than first inventing a common format. Rejected: treat common wording or a shared topic as sufficient grounds to collapse contributions, or count copied evidence as repeated successful use. Main effort remained the contextual distinctions whose loss changes a reuse judgment.

## Evidence boundary and sample

[evidence: read-only directory discovery during this run] Discovery under `/home/mr/Desktop/python` found ten directories named `innovations`. It did not follow directory symlinks and pruned `.git`, `node_modules`, `.venv`, `venv` and `__pycache__`. This is a bounded discovery result, not proof that every possible knowledge store was found. Filename metadata were examined across those folders; contribution substance was sampled in three only. No historical Git versions or live implementations were examined.

For precise source locators below, these aliases mean absolute paths, not inferred origins:

| Alias | Absolute source directory |
|---|---|
| A | `/home/mr/Desktop/python/github_clones_working_on/dev_trainer_tool_full_project/innovations` |
| B | `/home/mr/Desktop/python/github_clones_working_on/book_podcast_fiction_generator/innovations` |
| C | `/home/mr/Desktop/python/github_clones_working_on/learning_agentic_loops/innovations` |

[evidence: A/B/C directory listings and README indexes] A has eleven indexed pattern directories; B has thirteen; C has fourteen. These three cover distinct current index/admission-status presentations: an empty incubation list, an undated unchecked incubation entry, and dated checked incubation entries. These are observable differences between copies, not a demonstrated copying chronology.

[evidence: reads and SHA-256 comparisons] Six contribution instances were sampled, each including its `PATTERN.md` and every file in its `kit/`: A's `machine-enforced-laws` and `file-state-machine`; B's `machine-enforced-laws` and `situation-personification`; C's `machine-enforced-laws` and `rules-as-gates`. This yields four distinct contribution texts and three copies of one contribution. The repeated contribution tests exact identity; the others test context loss across formats and related-but-distinct advice. No expansion beyond the planned three folders/two contributions each was needed.

[evidence: SHA-256 of current `CONTRIBUTING.md` in all ten discovered folders] All ten admission files are identical: `14a2727b0a8f4039e27762bfdc6a80a5d893eaeb61283c69f0ee60278ec0d890`. The seven other locations are:

- `/home/mr/Desktop/python/learning/curriculums/python_curriculum/innovations`
- `/home/mr/Desktop/python/learning/curriculums/python_curriculum2/innovations`
- `/home/mr/Desktop/python/learning/curriculums/algorith_curriculum_brainstorming/brainstorm/codex/innovations`
- `/home/mr/Desktop/python/github_clones_working_on/innovations`
- `/home/mr/Desktop/python/github_clones_working_on/heurestic_loop_research/innovations`
- `/home/mr/Desktop/python/new_projects/job_getting_projects/project_assessment/projects/dev_trainer_tool_full_project/innovations`
- `/home/mr/Desktop/python/new_projects/job_getting_projects/project_assessment/projects/book_podcast_fiction_generator/innovations`

[interp] I cannot claim to have sampled different formal admission bars. The CEO's account of evolved standards remains historical context; present equality does not establish that the standards were always equal. Investigating history would be additional work, not a finding supplied by these copies.

## Observations

**Admission information and operational status can diverge.** [evidence: A/B/C `CONTRIBUTING.md`, sections 1–4, beginning at lines 7, 21, 37 and 46] The common contract asks for real-project use and citable evidence, a six-section description plus deployable assets, genericized kits, and recorded divergence when originating practice changes. It separately accommodates unproven material. [evidence: A `README.md:53`, B `README.md:57`, C `README.md:61`] Their incubation presentations differ. C additionally records check dates, evidence unavailable from that host, and a condition apparently met while graduation remains undone. These are recorded states, not verification of the underlying claims. No `check.py` exists at the root of A, B or C. No root checker was available to establish automated compliance; checks elsewhere were not examined.

**A copied location is not another origin or independent success.** [evidence: A/B/C `machine-enforced-laws/PATTERN.md` and its two kit files] The entire sampled contribution is byte-identical across all three hosts. The pattern SHA-256 is `a8420040fb643ee06036c2f0fdc62f8821994314c77f92fb77cae83ca6c38d12`; `kit/PREFLIGHT.md` is `da398c42f3fd16564be1f9414bf849a2724959ead6f28aefeb2ab771fa45622d`; `kit/commit-msg` is `6b59222a54c28726d80a4d05f957d3d5371eb1258d27375e65467c9572fcaac2`. [evidence: those patterns, “Proven in”, line 40] They repeat one originating-project account. No separate receiving-host evaluation is supplied there. [interp] Content identity supports recognizing these as exact copies of the sampled bundle, not three independent validations or proof of adoption in three hosts.

**Origin resolution is weaker than the presence of an evidence section suggests.** [evidence: A `machine-enforced-laws/PATTERN.md:40`, A `file-state-machine/PATTERN.md:41`, B `situation-personification/PATTERN.md:50`, C `rules-as-gates/PATTERN.md:67`] These accounts vary from year-level descriptions to month-level incidents and dated sequences, with differing descriptions of the originating environment. The sampled evidence sections do not provide direct local evidence-file links or commit identifiers sufficient to resolve every claim from the contribution alone. [interp] They contain evidence claims with useful circumstances; this report has not established their independent truth. Folder host, described origin, incident date and verification date must remain distinguishable.

**Applicability and limits live in more than one section.** [evidence: A `file-state-machine/PATTERN.md:36`; B `situation-personification/PATTERN.md`, “How to use it” and “Fits projects like”; C `rules-as-gates/PATTERN.md`, end of “Proven in”] Positive fit, cases of limited usefulness, restrictions on what a method establishes, and residual failure conditions appear in different places. [evidence: A/B/C `README.md`, index sections] The discovery indexes do not carry all of these distinctions. [interp] Selecting by an index row alone can discard information that changes the suitability of the contribution.

**A kit is a different view of a contribution, with varying context coverage.** [evidence: A `file-state-machine/kit/STARTER.md` compared with its `PATTERN.md`; B `situation-personification/kit/CAST-AND-FIT.md` compared with its `PATTERN.md`; C `rules-as-gates/kit/GATE-CHECK.md` compared with its `PATTERN.md`] Some kits retain explicit limitations and illustrative context; others emphasize operational starter material without the pattern's fit and originating evidence sections. [evidence: A `machine-enforced-laws/PATTERN.md:47` and `kit/` files] The same bundle contains an executable asset and a prose design asset. [interp] Asset presence does not establish that every asset is executable or complete. A kit-only transfer needs an accompanying route back to the relevant applicability and evidence, not an assumption that all context survived extraction.

## Equivalence and counterexamples

| Evidence relationship | Observation | Inference for recognition |
|---|---|---|
| A/B/C's sampled identical bundle | Pattern and both assets match byte for byte. | Recognize exact content copies while retaining source locations; do not multiply evidence strength by copy count. |
| C `machine-enforced-laws/PATTERN.md` and C `rules-as-gates/PATTERN.md` | Both discuss rules/checks, but their problem, originating situation, timing conditions and limits differ. The latter contains a later, more specific incident sequence. | A shared topic is insufficient for equivalence. Conditions can make apparently opposing advice compatible in different circumstances. Preserve both contexts for the executive's eventual judgment; this is no merge or precedence decision. |
| B `situation-personification/PATTERN.md` and its kit | Different expressions of the same contribution retain a recognizable common purpose and explicit limits, while evidence presentation differs. | Distinguish a contribution's explanation and operational view from independent contributions or independent validation. |

[interp] The second row is the sample's concrete counterexample to collapsing on topical similarity; the third is a within-contribution example of different expression. No independently developed, differently named contributions were established as semantically equivalent by this sample. Nor did it establish a same-name semantic divergence between hosts. An equivalence procedure must be able to leave those questions unresolved rather than invent a demonstration.

## Minimal capability recommendation

[interp, derived from the observations above] The next design work should support the following capabilities without deciding a storage format here:

1. Keep an identifiable contribution revision linked to its explanatory material, deployable assets, supplying locations and described origin. Record which admission standard/revision was applied, the assessed status and the reason, rather than treating current placement as proof of admission quality.
2. Carry applicability conditions, exclusions, adaptation requirements, dependencies and known limits with the contribution. Preserve negative evidence and known divergence; a later summary must not erase a condition that changes use.
3. Distinguish claims of successful use from checked supporting evidence, including evidence locators, originating circumstances, dates, verification scope and unresolved access. Repeated copies of one account remain one account.
4. Support exact-copy recognition separately from semantic equivalence. For semantic comparisons, keep the compared revisions, meaningful condition differences, supporting evidence, uncertainty and eventual decision rationale. The executive retains the decision.
5. Make discovery concise while keeping suitability-affecting context available before selection and maintaining a resolvable link from selected assets to that context. Insufficient information must be visible as insufficient.

[interp] These are the minimum distinctions exposed by this sample, not a complete common admission schema. Uniform headings alone would not resolve the evidence-quality and status differences found here.

## Selection-time input to the entry sibling

[interp: response to the supervisor's GO adjustment] At the moment a receiving project selects knowledge, it needs its current task, intended outcome and relevant operating constraints in hand. For each candidate, it also needs the following information; absent information must be labeled unknown:

| Information available before selection | Purpose grounded in this sample |
|---|---|
| Candidate identity/revision, source location, described origin and related copies/variants | Resolve the actual material and avoid counting copies as corroboration. |
| Problem addressed, applicability conditions and exclusions | Compare with the receiving task; an index title cannot establish fit. |
| Evidence claim, supporting locator, evidence/verification dates and checked versus unverified status | Distinguish a promising description from demonstrated applicability; allow inspection of the basis. |
| Known failures, limits, divergence and unresolved comparisons | Avoid losing the very condition that would change selection. |
| Admission/incubation/retirement status and the governing standard's identity | Avoid presenting unchecked or pending material as already accepted merely because it is discoverable. |
| Available assets, their kind, required adaptations/dependencies and link to explanatory context | Know what is actually supplied and what still must be understood or supplied before use. |

[interp] A concise candidate view may support relevance screening; selecting assets for use requires the suitability-affecting context above or an explicit unresolved judgment. The entry sibling owns how and when this information reaches the receiver, including refresh and loading. This report does not inspect those mechanisms. The executive must reconcile the two reports at this interface.

## Limits, friction and completion

[evidence: scope of this run] Only current local documents, filenames and content comparisons were examined. No kit was executed, historical lineage reconstructed, source incident independently verified, or receiving-project adoption observed. No performance or tenfold-scale claim follows from this sample. The sample is concentrated in a copied family; it cannot establish the full range of admission practices or equivalent ideas throughout the tree. Source paths and structural findings are retained here without copying the personal innovation procedures, kits or incident substance.

[interp] The material friction reaching the executive is the mismatch between expected differing standards and identical current admission files, plus weak resolution of some evidence claims. Treat historical-standard comparison and independent evidence verification as explicit unknowns when choosing further work. They do not require changing the CEO's intent or extending this investigation silently.

[evidence: tools used in this run] Resources used: this Codex instance, local directory traversal, bounded text reads and SHA-256 comparisons. They were sufficient to compare current copies and locate context-bearing sections without network access, source changes or execution of personal assets. No subordinate division was needed. Only this assigned report was written during the investigation; no implementation, external messages, commits or pushes were performed.

[evidence: this report and the recorded GO] The bounded investigation step is complete. The executive receives this report when this run ends, holds comparison with the entry report and decides the next design work; the CEO holds commits. Remaining uncertainties above are reported limitations, not claims of completed verification.
