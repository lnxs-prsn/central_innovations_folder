# Project entry investigation — 2026-11-01

## Outcome and situation

[interp] The sample supports three feasible places for knowledge sharing to enter: agent orientation, an explicitly invoked session command, and preparation of a launched turn. It does **not** establish a mechanism that refreshes shared knowledge whenever any project is opened. Written directions, callable code and observed execution must remain separate claims. The next design work needs to establish which opening and creation paths it will cover, then connect refresh and selection to those paths.

[evidence: `briefs/2026-10-25_entry.md`, “Supervisor's check and GO — 2026-11-01”] This investigation follows the recorded GO and its adjustment: each entry below states what information is available to the agent and when. Innovation content, equivalence and selection criteria remain with the context sibling; design remains with the executive.

[interp] No finding changes the quoted CEO intent in `intent.md`. The evidence narrows what can currently be promised about reach, bootstrap and recovery. This assigned investigation step is complete; implementation and runtime verification are not performed.

## Evidence and sampling limits

[evidence] I used one Codex instance, filename discovery with `rg --files --hidden`, bounded text searches, and local source reads. This was sufficient to compare entry arrangements without executing other projects' code. Discovery omitted Git internals, dependency environments and prohibited secret paths. Targeted Python reads resolved paths and checked containment under `/home/mr/Desktop/python`; no external links were followed. Broad discovery was a locator pass, not a census; some result previews were capped. The findings below rest on targeted reads, not absence from those previews.

[interp] I selected these arrangements for differences in entry behavior, rather than representativeness by project count. Duplicate checkouts were not treated as independent confirmations. All source paths below resolve beneath `/home/mr/Desktop/python/`:

| ID | Sample root | Reason for inclusion |
|---|---|---|
| C | `new_projects/central_innovations_folder/` | Current delivered-edition reference and this run's actual assigned-task entry. |
| P | `learning/curriculums/python_curriculum2/` | Provider pointer files and task/persona dispatch. |
| F | `new_projects/job_getting_projects/project_assessment/projects/book_podcast_fiction_generator/` | Different maintainer and pipeline entry routes in one project. |
| D | `new_projects/job_getting_projects/project_assessment/projects/dev_trainer_tool_full_project/` | Nested entry routed to executable session code; copying procedure. |
| T | `new_projects/project_management/toolusage/` | Launch-time prompt/access preparation and a separate confined execution component. |
| L | `github_clones_working_on/learning_agentic_loops/` | An older locally installed entry arrangement, distinct from C's reference. |
| A | `new_projects/project_management/directed_opportunism/deliveries/2026-11-01/adoption/` | Fixed delivered entry templates, examined as installation artifacts. |

Source notation such as `D/autopsy_loop/tools/session.py:600–650` identifies the file under that root and the lines inspected. These are structural findings; no personal innovation substance is reproduced.

## Entry paths and information available

### C — assigned task and delivered reference

[evidence: `C/CLAUDE.md:1–3`, `C/AGENTS.md:1–5`, `C/directed_opportunism/source`, `C/directed_opportunism/LOCAL.md`] Claude's pointer leads to AGENTS; AGENTS directs a reader to resolve a plain relative path and read the edition entry plus local locators. The reference resolves to the sibling method project's `deliveries/2026-11-01/`. LOCAL names intent, executive brief, situation and experience records. No synchronization or executable call appears in these entry files.

[evidence: this run's supplied task and local read results; `C/briefs/2026-10-25_entry.md`, control loop and final GO] In this run the user supplied the working directory, assigned brief and instruction to read the new GO; I read them before investigation. That demonstrates one explicit prompt-to-file entry. It does not demonstrate automatic entry on an editor opening or a fresh harness session.

[interp] **Information and timing:** the assigned task and project identity are available from the initial prompt; method identity becomes available after resolving `source`; project direction and authority after reading the named local records. A generic folder opening alone supplies neither an assigned task nor an inference that a historical assignment is current. Candidate knowledge could be located during orientation, but applicability would need the task and sibling-defined context information. Knowledge refresh must not silently change the fixed method edition or revive stopped work.

### P — task/persona dispatch through provider pointers

[evidence: `P/AGENTS.md:3–21`, `P/CLAUDE.md:1–4`, `P/GEMINI.md:1–4`, `P/README.md:11–33`] Provider files point to a common AGENTS contract. That contract directs reads of reference layers and the relevant persona. A dispatch table maps user requests to roles; one assessment route explicitly instructs invoking `tools/grader.py`. The README describes a human task-copying and assessment ritual.

[interp] **Information and timing:** project reference locations are known after entry; persona and relevant active task become known from the user's request; history is requested for a particular coaching route. The grader is a task-time command, not evidence of an opening hook. This is a feasible task-selection seam after role dispatch, contingent on the agent reading and following the route. Shared loading would have to respect the local staged disclosure and reference-layer boundaries (`P/AGENTS.md:23–50`).

### F — maintainer orientation and separately fenced pipeline kickoff

[evidence: `F/AGENTS.md:1–14`, `F/CLAUDE.md:1–6`, `F/HANDOFF.md:31–55`] A maintainer reads HANDOFF and the dated handoffs it identifies, then current work orders. The handoff distinguishes current state, later process changes and older explanatory records. It is a pointer and trust map, not a refresh program.

[interp] **Information and timing, maintainer:** the project and handoff locations are available at entry; current state, queue and assigned ticket boundaries become available after the directed reads and dispatch. A maintainer orientation seam could expose a compact knowledge-discovery entry before task-specific selection. A dated handoff alone does not establish that knowledge from other projects has been refreshed.

[evidence: `F/fiction_loop/RUN.md:6–10,23–51`, `F/fiction_loop/agents/orchestrator.md:9–34,54–70`] The pipeline instead starts with a manually pasted fresh-session kickoff. Its driver is described as an agent session, not a program. Its permitted world excludes root governance, handoffs and innovations. The prescribed first executable step is a preflight tool; after that it reads selected master-state fields. I inspected these directions, not the private state or runtime effects.

[interp] **Information and timing, pipeline:** role and run request are supplied at kickoff; permitted conduct and preflight result precede selected run-state fields. The driver intentionally lacks maintainer plans and innovation contents. A universal instruction to load shared knowledge into every session would conflict with this arrangement. The feasible seam is preparation by an authorized maintainer or run launcher before the fenced driver begins, with only approved, relevant inputs passed into its permitted world. Whether that interface should change is a design decision; this report grants no change to F.

### D — nested entry invokes a computed session command

[evidence: `D/AGENTS.md:3–19`, `D/autopsy_loop/AGENTS.md:1–14`, `D/autopsy_loop/CLAUDE.md`, `D/autopsy_loop/RUN.md:3–6,23–36`] Root entry gives coordination and ticket boundaries; nested entry adds one command, `python3 tools/session.py` from `autopsy_loop/`. RUN explicitly says the owner starts sessions manually and gives the same kickoff. This is an executable session entry **when invoked**, not code registered to run on folder opening.

[evidence: `D/autopsy_loop/tools/session.py:235–252,259–320,396–472,527–593,600–650`] The command runs checks, resolves profile/progress/workspace state, computes status and eligible actions, writes a run marker, and prints either failure/remedy or status/menu. Some checks call other programs; the tool reads environment configuration and writes output. It was therefore not executed in this read-only investigation. The expected `autopsy_loop/outputs/session_runs.jsonl` was absent at this sampled checkout; no historical execution claim follows from it here. The installed source, rather than the still “ready to implement” label in `D/studio_specs/session_bootstrap.spec.md:3`, establishes that code exists.

[interp] **Information and timing:** before invocation, the agent has the kickoff and project-local directions. Inside the command, profile, exercise, cursor, workspace readiness and queues can be resolved. On successful return the agent gets computed status/menu; the next task is chosen by the user afterward. On checklist failure it gets a remedy instead of a menu. Thus opening-time discovery and task-specific selection may occur at different times. A knowledge integration could use this command boundary for initial discovery and the later choice for selection, subject to local ownership and allowed writes.

[evidence: `D/autopsy_loop/tools/install_hooks.py:23–59`, `D/autopsy_loop/.githooks/commit-msg:1–26`, `D/autopsy_loop/RUN.md:74–85`] The separately installed hook checks commit-message format. It is a commit event, not an opening event; its presence must not be mistaken for refresh coverage.

### T — explicit turn preparation and allocated visibility

[evidence: `T/org/org:108–125,241–301,365–395`] The older organization launcher has explicit staffing/cloning and dispatch code. Turn preparation chooses the work directory, builds a prompt with role/superior and message paths, prepares access grants, then invokes a provider adapter. Dispatch reacts to queued messages or eligible interrupted work. There is no shared-knowledge refresh call in these traced functions. This is a launch seam in source, not proof that these services are active.

[evidence: `T/execution/envelope.py:36–104,164–189,247–278`, `T/execution/README.md:8–14,31–45,66–71`] The separate direct-child component accepts a controller allocation and command; work appears at `/work`, read-only sources at `/sources/NAME`, and tools at `/tools/NAME`. Input defaults closed; explicitly recorded stdin is bounded to 64 KiB. It does not discover a project's knowledge sources or construct its task by itself. The component documentation says production/provider integration remains work, and `T/STATE.md:29–41` records outstanding prerequisites and no activated production roles.

[interp] **Information and timing:** before launch the controller can know the allocation, work directory, supplied task/input and granted source names; the child sees only the prompt/input and mounted files that preparation supplies. A host-readable sibling reference does not guarantee visibility at its original relative path inside `/work`. Launch preparation is a feasible place to refresh and supply a task-relevant discovery result, but production integration and source/path mapping require proof. Provider adapters are replaceable in the source arrangement; provider independence of deployed behavior is not established by that fact alone.

### L and A — installed snapshots and entry templates

[evidence: `L/AGENTS.md:3–9`, `L/CLAUDE.md:2–4`, `L/.directed_opportunism/README.md:3–5,10–34`] L's entry points to a local installed directory that identifies its package/version and directs session reads of local intent, brief and logs. This differs from C's sibling-edition reference. I treated it as sampled project evidence, not a replacement method for this assignment.

[interp] **Information and timing, L:** local installation identity is available after following the entry; local direction and pending work after further reads. These files contain no executable next-open refresh mechanism. Their existence shows an arrangement that can retain a local snapshot through inactivity, not whether that snapshot is current or authorized for this project now.

[evidence: `A/files/AGENTS.md`, `A/files/CLAUDE.md`, `A/files/directed_opportunism/source`, `A/files/directed_opportunism/LOCAL.md`, `A/NOTE.md:11–24,34–36`] A supplies entry and locator templates; its source file is an explicit placeholder. The note describes called installation and preservation of project-owned direction. It expressly distinguishes a locator from synchronization and requires preserving/restoring access to the designated edition.

[interp] **Information and timing, A:** before filling templates there is no real edition location or project-specific task. After a valid installation the reader can locate those records. Copying these templates alone is neither a working new-project bootstrap nor an executable project constructor.

## Creation, inactivity and recovery implications

[evidence: `intent.md`, Context; `D/autopsy_loop/RUN.md:117–130`] The CEO's account identifies copying the last project as the general creation practice. D independently documents owner copying to a new version directory and a manual post-copy checklist, including absolute-path and environment problems. I found no general constructor for the CEO's projects in the bounded searches. The actual UI, command or copying tool the CEO uses was not established. Application commands that generate a book seed or learner profile are not evidence of general workspace creation.

[interp] A feasible bootstrap integration is at the actual copy/create operation, or as an explicit first-session initialization where that operation cannot be intercepted. It would need fresh project direction and knowledge discovery rather than treating the copied project's task/state as current. Which creation mechanism can enforce that remains unknown; locating or agreeing on it is an unresolved design input, not evidence that a new mechanism already exists.

[interp] Weeks of closure cause no special executable event in the inspected files. A refresh performed at a covered next launch could catch up then; a copied or installed snapshot cannot do so on its own. Freshness should be established against available shared state at that launch, with absence or failed access visible. None of this requires periodic GitHub queries. Local availability alone would not cover changes made elsewhere unless their arrival mechanism is also established.

[evidence: `C/directed_opportunism/source`; `A/NOTE.md:34–36`; local file discovery under C] C currently contains direction and delivery-reference records, with no implemented shared-knowledge service found. Its designated edition is outside C. [interp] Cloning C alone would not reproduce the edition at that sibling path, nor establish the CEO's empty, working knowledge-sharing capability. Empty recovery therefore remains unproved. The future generic capability needs its code, dependencies, initialization and empty-state behavior recoverable without personal innovations, plus an explicit way to re-establish authorized external references. Host-specific paths, copied environments and private launcher allocations are recovery dependencies, not evidence of portability.

## Implications for the executive and context sibling

[interp] The executive can now choose the next design investigation around concrete seams:

| Seam | What is feasible | Limit that must remain visible |
|---|---|---|
| Common entry instructions (C, P, F maintainer, L) | Route a reader to compact discovery and later task-specific material. | Requires an agent/harness to reach and follow the file; no universal opening execution is established. |
| Explicit session command (D) | Compute initial discovery alongside local session state, then select after user task choice. | Invocation remains manual or instruction-driven; existing tool checks and writes need local authorization. |
| Turn preparation (T) | Refresh before starting a child and supply permitted inputs/source access. | Covers only launches routed through it; inspected production integration is incomplete. |
| Creation/copy boundary | Initialize discovery and avoid inheriting another project's active direction. | The general initiating mechanism remains unknown; templates require real references and local records. |
| Fenced pipeline preparation (F) | Have an authorized outer role prepare approved run inputs. | Driver cannot independently load root innovation/governance material under its current contract. |

[interp] For the context sibling, the key interface is two-stage: entry may know only project, role, source access and current state; a concrete task may arrive later by dispatch, ticket or menu choice. Discovery must be usable with that limited information, and the later selection result must carry the context needed for applicability. The sibling owns what that context contains. Entry owns when it can be obtained and which role can see it. F's fenced driver is a concrete case where the selecting/preparing role and consuming role may differ.

[evidence] Root checks found none of `.claude/settings.json`, `.claude/settings.local.json`, `.vscode/tasks.json`, `.vscode/settings.json` or `.codex/config.toml` in C, P, F, D and L. [interp] That bounded check does not exclude ignored configurations elsewhere, parent/global hooks, extensions or external launchers. Those outside the authorized tree were not inspected. No claim is made about provider defaults or every project's opening behavior.

[interp] Remaining unknowns are the CEO's actual general opening/creation initiation path, coverage of any host-level hooks, live execution of the sampled commands, confined access in a production deployment, and empty-clone recovery. No network, external messaging, source-project changes, implementations, tests that execute project code, commits or pushes were performed. Only this assigned report was written during the investigation. The executive receives it when this resumed run ends and holds the next design direction and comparison with the context report.
