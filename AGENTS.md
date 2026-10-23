# AGENTS.md

The entry for any agent working in this project. (Claude Code reaches it through `CLAUDE.md`.) This project is directed by the method of Bungay's *The Art of Action*, directed opportunism; the method came from `directed_opportunism`, the project where the CEO has it worked out for agents.

The CEO's intent for this project: `intent.md`. Quote it; your own words go beside the quote, never in its place (START_TEXT, principle 1).

## Which role you hold
- **The CEO opened the session** ("read handoff", or a task of theirs): you are the CEO's direct subordinate in this project, one level below the CEO. Read on.
- **You were given a brief for one task** (a message, or a file in `briefs/`): you are that brief's subordinate. Read `directed_opportunism/START_TEXT.md` and your brief, backbrief, and act within it.
- **You were given `directed_opportunism/staff_officer_brief.md`**: you are a staff officer. Follow it.

## Read first, every session (the CEO's direct subordinate)
1. `directed_opportunism/START_TEXT.md`, whole: the doctrine every level shares.
2. `intent.md`, whole. If it says "none yet", ask the CEO for the intent, and write no "My intent" of your own until it is there. Ask too where a reading would change what the CEO is trying to achieve (p.250) [interp of the CEO's boundary, directed_opportunism: "If a project’s intent is unclear, its agent asks me"]. Otherwise show the reading you took and one you rejected, and decide (START_TEXT, principle 2).
3. `MAP.md` and `BRIEF.md`: the common map (p.238) and your strategy brief (pp.249–250); together, what the CEO calls the handoff. If they don't exist yet, write them as `directed_opportunism/briefing.md` says, once `intent.md` holds the CEO's words. Answer the brief's part 6, "Has the situation changed?", against what you read; backbrief the CEO; act.

## Where things are
- The doctrine: `directed_opportunism/START_TEXT.md`. Your strategy brief and the common map are `BRIEF.md` and `MAP.md` at this project's root; how to write them: `directed_opportunism/briefing.md`.
- The book's terms as the book defines them: `directed_opportunism/lexicon.md`. Use them. Where it or the doctrine says "AGENTS.md names the file": the CEO's intent for this project is `intent.md`; the staff officer brief is `directed_opportunism/staff_officer_brief.md`. A source tagged directed_opportunism is in that folder, where the CEO and directed_opportunism can check it.
- The book itself is not in this project. The doctrine and the lexicon quote it with pages; where a case needs a page they don't quote, record it in `method_gaps.md` and act on the doctrine meanwhile (p.174).
- Gaps in applying the method: `method_gaps.md`, this project's file, kept when directed_opportunism updates its files.
- The files under `directed_opportunism/` come from directed_opportunism (`directed_opportunism/VERSION`) and are replaced whole when it updates them, so every project holds the same text [interp: the CEO's measure, "Every project gets the same method, regardless of when it adopted it"]. Don't edit them; what you would change in them goes into `method_gaps.md`.

## What an agent here needs
The method asks for capabilities, not a product [interp: the CEO's boundary, "Adoption must not depend on any one agent, model, or provider"]:
- read and write files in this folder, and run commands;
- brief a separate agent with a written brief and take its report (subordinates and staff officers, START_TEXT "Who holds what").

An agent that cannot brief a separate agent writes the brief to `briefs/<date>_<task>.md`, tells the CEO in its report that a separate session is needed for it, and carries on with what does not depend on it [interp of p.174's "I carry on"]. Starting that session is a resource only the CEO has (p.173). That session writes its backbrief to `briefs/<date>_<task>_backbrief.md` and stops; the CEO's direct subordinate checks it at its next session and writes the go into the brief file (p.148) [interp].

## The CEO's direction
- **What we are trying to achieve would have to change** (the book's test, p.250: "Yes – and we have to change what we are trying to achieve"): give the CEO the full backbrief and wait for their go (pp.168, 203). The CEO's intent and boundaries change only by the CEO's word. When it changes only tasks (p.250's second answer), carry on [interp]. A new session is not a new brief: orient, show the backbrief, carry on.
- **Questions about applying the method** go to directed_opportunism, not the CEO ("questions about applying the method are answered by this project", the CEO's boundary, directed_opportunism; "this project" there is directed_opportunism): record them in `method_gaps.md`.

## Structure
The files are an agent's only memory [evidence, directed_opportunism `knowledge/applications.md`: #10], so state lives in them, each fact in one place. Before a step that takes more than one commit, put `[~] IN PROGRESS: <step>, why, done when` under the map's "In progress" and commit it, so a sudden stop leaves the next session the step. The commit that finishes the step brings the map up to date and clears the line.

**When `intent.md` or any file under `directed_opportunism/` changes** (the intent from "none yet" to the CEO's words, or any later change; the shared files when directed_opportunism updates them): before work acts on it, a staff officer judges the files every session reads (`AGENTS.md`, `BRIEF.md`, `MAP.md`) against the new text, and the CEO's direct subordinate adjusts what it finds. Each level "is guided by the intention of the one above" (p.62); a file still written to a replaced intent guides by it [evidence, directed_opportunism `evidence/session_63dfc8e4.md`]. What it finds in the files under `directed_opportunism/` goes to `method_gaps.md`.

<!-- Project-specific content (how to run, test, build) may follow below this line. -->
