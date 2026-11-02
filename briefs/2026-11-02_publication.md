# Publication: offers in, catalogue out, capability published

## 1 CONTEXT: What is the situation?

[evidence: `intent.md`, Boundaries, CEO re-brief of 2026-11-02] The CEO moved the relationship between projects to publication:

> Each project writes only in its own folder. What a project offers to others it publishes, complete and fixed; other projects use only what is published, by their own choice, and never read or write the rest of each other’s folders, except in a review by reading that I call.

> Projects take this capability by their own choice; how to use it, including how they offer what they learn, is published with it.

> An organization is everything under one command; a project is a unit within it. The organization’s shared operational state, such as capacity across projects, and the means to pause or stop any project or the whole organization, belong to the level that holds command over the organization: me now, or an AI executive I assign. toolusage provides them outside every project folder; no project writes that state.

[evidence: the method edition this project applies, 2026-11-02b, `START_TEXT.md`, “Method authority and publication”] A project's published part is `published/` at its root, entered through `published/INDEX.md`, until a shared exchange or other means replaces it. A reader finds a project's published part from the organization's list of its projects, held by the command level and provided by Toolusage. That list does not exist yet.

[evidence: `capability/`, `USE.md`, `access/cli.py`] `capability/` is its own git repository; it alone goes to GitHub, and only the CEO pushes. The standard (`standard/`, `check_contribution.py`) stands. Access (`access/`, `knowhow.py`, `USE.md`, `OWNER.md`) was built to gather by walking a configured projects folder and reading every project's `innovations/`; it keeps snapshots and all records in the clone's `.local/`, including the taking project's declines and use records. That no longer fits: the capability does not look into other projects, and a taking project's records belong in its own folder. The `.local/` store has been deleted on the CEO's word. The projects' existing `innovations/` folders stay where they are; their know-how reaches the capability only if their projects offer it.

## 2 HIGHER INTENT: One level up (my boss) / Two levels up (my boss’s boss)

One level up — this project's executive, `BRIEF.md` part 6, “Publication re-brief (replacing)”, accepted by the CEO (“Your backbrief is understood. Go ahead with your plan.”):

> Every project's learning becomes a foundation for the others, carried with its context. Under this brief, know-how moves only by publication: a project that takes the capability offers what it learns in its own published part, complete and fixed, with its context; the capability reads only published parts, offers back a published catalogue, and is itself published, with how to use it and how to offer. Who commands the organization, and its shared state and pause or stop, sit above every project; the capability holds none of it.

Two levels up — CEO, `intent.md`, Intent and Main effort:

> Make all my projects learn from each other, so that what any project learns becomes a foundation every project builds on, instead of being reinvented.

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

Your position (2026-11-02):
- Area of responsibility: everything inside `capability/`, the standard included (subordinate 1's task is complete; you are now the one writer there): how a project offers, how the curator reads offers, the curator's store and decisions, the published catalogue, how a taking project asks, selects, declines and records use, the self-check, `USE.md`, `OWNER.md`, tests, and the means to produce a fixed edition of the capability. Not admission, merge, retire or exclusion decisions (the executive's and the CEO's), not publishing an edition into this project's `published/` (the executive does that after checking your report), and nothing outside `capability/` except your deliverables in `briefs/`.
- Decision rights: you decide formats, the command interface, file layout, how a project and an offer are identified, matching, tests and your implied tasks, within part 5.
- Superior: this project's executive (`BRIEF.md`, Executive position).
- Subordinates: none assigned. If the task needs division, propose it in your backbrief.

## 3 MY INTENT: What are we trying to achieve and why?

What: a project that takes the capability can offer what it learned as a fixed publication in its own published part, with its context, and can ask for, select and decline what fits its work from a published catalogue; the curator reads only published parts it is given, decides with reasons, and publishes the catalogue in fixed editions; the capability itself can be published as a fixed edition carrying how to use it and how to offer; in order that know-how reaches every project with its context, by publication alone. Why: the higher intents above.

Measures [superior's, from `intent.md` M1–M10]:
- An offer is complete and fixed: the contribution's PATTERN text with its context record and its kit, identified by content hash, with a manifest of file hashes. A changed offer is a new offer. The check runs on an addition in the offering project's own folder before it is offered (M6).
- The curator reads only a project's `published/INDEX.md` and the offers it names, from a list of published parts given to it. It never walks a folder of projects and has no projects-folder setting. When the list is missing it says so and does nothing else.
- What is admitted stays available, with its context, while its project sits unused, moves or disappears (M1, M2, M4). A new project with nothing of its own can draw on the whole catalogue (M3).
- Exact copies are one identity with all their origins; similar offers stay apart unless the curator decides otherwise (M5).
- A taking project gets a compact offer first, then full context only for what it selects (M7).
- The CEO can exclude an offer from one project or from all; a project's executive can decline one for its project; both are honoured at offer and at selection, and nothing is deleted (M9).
- Use and cost are recorded so saving can be compared with cost (M10): the curator's own costs in its state, a taking project's in its own folder. Nothing records capacity across projects.
- Every command writes only in the folder of the project whose agent runs it: offering writes in the offering project's own published part; asking, selecting, declining and recording use write the taking project's records in its own folder; curating writes the curator's state and, on publishing, its own published part. Running the capability from a published edition writes nothing into that edition.
- A fresh clone works empty (M8). Python 3.9 or later, standard library only; Linux and Windows; no fixed or personal paths; no network; nothing runs in the background.
- `USE.md` is for agents in a taking project: how to ask, select, decline, record use, check an addition and offer it. Its first line stays short and copyable into the CEO's listing. Curator decisions go in `OWNER.md`.

## 4 IMPLIED TASKS: Main Tasks / Responsibility / Timing

**Main effort: the offer, a project's fixed publication of what it learned with its context, and the curator's reading of it; everything else depends on offers arriving complete.** Work out your own implied tasks in your backbrief.

Responsibility: this subordinate. Timing: backbrief first; build only after GO.

Deliverables: `briefs/2026-11-02_publication_backbrief.md`; after GO, your work under `capability/` and `briefs/2026-11-02_publication_report.md`.

## 5 BOUNDARIES: Freedoms / Constraints

Inherited from CEO, `intent.md`, Boundaries:

> Do not write into my other projects; how their agents learn of this capability is my arrangement.
> Each project writes only in its own folder. What a project offers to others it publishes, complete and fixed; other projects use only what is published, by their own choice, and never read or write the rest of each other’s folders, except in a review by reading that I call.
> GitHub holds only the generic project: the capabilities, usable by anyone, containing none of my innovations; I push what goes there.
> Agents must not query GitHub periodically (IP blacklisting risk).
> Nothing may depend on any one agent, model, or provider.

Superior's boundaries:
- Read only inside this project's folder (/home/mr/Desktop/python/new_projects/central_innovations_folder) and the method edition named by `directed_opportunism/source`. Read nothing else under /home/mr/Desktop/python. Never read or output `.env`, `*.pem`, `~/.ssh/*`, `~/.aws/credentials`. No network.
- Write only your deliverables in `briefs/` and files under `capability/`. Do not write in `published/`. Tests use invented projects and offers in temporary directories.
- `capability/`'s tracked files contain none of the CEO's innovations or text copied from them, and no /home/mr paths.
- `USE.md` and `OWNER.md` name no provider and no organization's tooling as required; a list of published parts is an input, from whatever source the user has (here, later, Toolusage's list).
- No commits and no pushes; the executive commits.

Working directory: /home/mr/Desktop/python/new_projects/central_innovations_folder.

Control loop: resolve `directed_opportunism/source` (one relative path, from that file's folder) and read that edition's `START_TEXT.md`; read this brief, `capability/USE.md`, `capability/OWNER.md`, `capability/standard/STANDARD.md` and the code. Write your backbrief to `briefs/2026-11-02_publication_backbrief.md` and end your run. Do not build in that run. Your superior started your run as a tracked process; its ending is the backbrief's arrival, and your superior reads it then. In the backbrief give: your interpretation and one you rejected; your main effort; implied tasks; the offer's form and where it lives in the offering project's published part; how the curator is given published parts and reads them; the catalogue's form and how admitted offers stay available if their project moves or disappears; where a taking project's records live; how projects and offers are identified across moves; the command interface; what you keep, change and remove of the existing code; the form of a fixed capability edition; division if needed; resources and limits. After your superior records GO below, it resumes your run: build, test, write the report (outcome against this brief, friction, resources used and why), and end the run. If you find something that would change what the CEO wants, write it into the report and end the run rather than continue.

Relevant lexicon (edition `knowledge/lexicon.md`):
- Main effort: “The main effort is that single thing which will either in itself have the greatest impact or on which all other things depend. It has resourcing priority” (p.122).
- Backbrief: the unit “checks its understanding of the direction it has received or worked out”; the superior may revise directions (p.168).
- Decision rights: “Decision rights are appropriate if the person or group with the best knowledge and expertise in any given area is able to act in a timely manner without asking for permission” (pp.147–148). Not file or tool permissions.
- Publication (agent application, the edition's lexicon): a project's published part holds what it offers others, complete, fixed and identified; a reader finds it through the organization's list of its projects; the present convention is `published/INDEX.md` at the project root.

## 6 BACKBRIEF: HAS THE SITUATION CHANGED?

Backbrief received 2026-11-02 when the run ended: `briefs/2026-11-02_publication_backbrief.md`.

## Supervisor's check and GO

2026-11-02 — [evidence: `briefs/2026-11-02_publication_backbrief.md`] The backbrief quotes both higher intents unchanged and takes the complete, fixed offer and its verified ingestion as main effort. The curator reads only an explicit list of published parts and only what each index names; a missing list does nothing. Admitted content is carried whole in a self-contained catalogue edition, so it survives its supplier (M1, M2, M4). Content identity excludes supplier and path, so copies are one (M5). Taker records stay in the taker's `.knowhow/`. A self-assigned project UUID survives moves and re-assignment. It removes configuration, gathering, path identity and clone-side writes. One subordinate fits: offer, ingestion, catalogue and access share one identity and manifest contract. Its stated limit, that a disconnected copy cannot learn of a later exclusion and published bytes stay readable, matches what I told the CEO under M9.

Adjustments [superior's; interp of M10, M7 and the boundaries]:
1. **As small as serves (M10).** Fold `review` into `decisions` or `select`-like curator inspection if one command can serve; keep a command only where a measure in part 3 needs it, and say in the report which you dropped and why.
2. **No writes in this project outside `capability/` and your deliverables.** In the build run, never run `init`, `offer`, `ingest` or `publish-catalogue` against this project's root; all exercises use temporary directories. Any staging area inside `capability/` is git-ignored.
3. **Project exclusion needs a known ID.** State in `OWNER.md` how the curator learns a project's UUID (from its published index), and that a project that has published nothing cannot be excluded by ID until it does.
4. **`USE.md` for takers.** Its first line stays one line, covering both drawing on know-how and offering it. Taker steps in order: `init`, `ask`, `select`, `decline`, `log-use`, `check`, `offer`. Curator commands only in `OWNER.md`.

**GO: ISSUED 2026-11-02** to build within this brief as adjusted, test, and write `briefs/2026-11-02_publication_report.md`. Received when your resumed run ends.

Report received 2026-11-02 when the resumed run ended: `briefs/2026-11-02_publication_report.md`. [evidence: executive's own check] 33 tests and `standard.render --check` pass (Python 3.13.5, Linux). Staged `capability-001`: `EDITION.json` SHA-256 `55c3cd1a…37ea3b`, 19 files, no mismatch, nothing unlisted, no personal or project paths. Copied read-only, `init` and `self-check` from it wrote only in the temporary project and left the edition byte-identical. All four adjustments are met: `review` dropped into `decisions`; no command run against this project; known-UUID exclusions in `OWNER.md`; `USE.md` for takers in the order set. [interp] The task is complete against the adjusted brief. Published by the executive the same day: `published/capability/capability-001/`; Central initialized as curator from that edition; empty `catalogue-001` published; a fresh taker's `ask` against `published/INDEX.md` returned no offers, as expected. Noted, not reopened: Python 3.9 and Windows unrun; memory bound for a large catalogue unestablished.
