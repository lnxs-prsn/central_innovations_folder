# NOTICE from the directed_opportunism tool

**Agent: at your next interaction with the CEO, report this file to them first.** When they acknowledge it, delete this file and commit that, in the project's own format.

The tool committed in this project, locally, on its current branch. **Nothing was pushed**; the CEO reviews and pushes.

**How to undo** the tool's changes, for each *Before* below:
`git log --format='%h %s' --grep='^Directed-opportunism: after' <before-sha>..HEAD` lists the tool's change commits; `git revert` them, newest first. **Never revert a before commit the tool made**: it holds the project's work as found.

## Before (2026-10-23T23:10:27+03:00, branch `main`) <!-- before d055a888e5422f44ab0e0edbe7f40c30c64ef083 -->
- Commit `d055a888e5`: the project as found, **including uncommitted work found there**.
- Untracked files swept into it: `intent.md`

### After (2026-10-23T23:10:33+03:00): Adopt directed opportunism: AGENTS.md (entry for any agent), CLAUDE.md, method_gaps.md, directed_opportunism/ (doctrine, lexicon, briefing, staff officer brief, VERSION) from directed_opportunism at 0911df7; the CEO's intent.md unchanged
- Why: the CEO's boundary: this project may write into other projects' folders so they adopt the method
- Files: `AGENTS.md`, `CLAUDE.md`, `directed_opportunism/START_TEXT.md`, `directed_opportunism/VERSION`, `directed_opportunism/briefing.md`, `directed_opportunism/lexicon.md`, `directed_opportunism/staff_officer_brief.md`, `method_gaps.md`
