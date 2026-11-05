# capability-002 backbrief — 2026-11-05

## Position and control loop

Received direction: `briefs/2026-11-05_capability-002.md`, read whole. I am the executive's subordinate and sole writer for this task inside `capability/`, with only this backbrief and the later report permitted outside it. I decide wording, validation design and necessary implementation within the brief; admission, publication into this project's published part, commits and pushes belong elsewhere. No subordinates assigned or needed. This run writes this backbrief and ends; implementation, tests and staging follow only after the executive records GO and resumes the run. No build, tests, staging, commit or publication has been performed.

Method: resolved the plain locator in `directed_opportunism/source` to fixed edition 2026-11-05, read its ENTRY and START_TEXT, this project's LOCAL and relevant lexicon entries. Read the named guides, standard, update, publication formats, relevant code and tests, and local friction, including the 2026-11-03 edition-test failure. No other briefs or earlier reports were read.

## Has the situation changed?

[evidence: `published/INDEX.md`] No material change from the brief is established: capability-001 and empty catalogue-001 remain current; the index records named projects but no offers. I did not inspect other projects or reassess their holdings.

[evidence: `capability/access/cli.py`, `tests/test_access.py`, `standard/STANDARD.md`] The reported failure has a concrete cause visible in code: the test copies all of ROOT, including an edition's `EDITION.json`, into its purported developing source. `pack_capability` correctly refuses that directory. This is code inspection, not a new reproduction. The standard already supports the required distinction: origin describes the developing project, development_kind allows only invented/materially_refined, and supplying copies are separate. Neither a new schema nor a new command is needed.

Unknowns remain: actual project effort to reconstruct context, Python 3.9 operation and Windows operation. No evidence here resolves them.

## Intent, interpretation and main effort

One level up, the executive's `BRIEF.md`, quoted by the assigned brief:

> What: establish a recoverable, provider-independent capability for projects to contribute, discover, and selectively use shared know-how in order to make each project's learning a usable foundation for the others.

Two levels up, CEO `intent.md`, quoted by the assigned brief:

> Knowledge must travel with its context. A technique that arrives without the situation it was developed in gets applied blindly, which is worse than not having it. Where reach and context conflict, context wins.

[interpretation] Help a project's executive judge each piece it already holds, including deciding to leave it local, and make the capability reachable using the listing's location. The guide must explain the cost and evidence needed without turning possession into development or offering into a duty.

Rejected interpretation: convert every existing collection into offers as an adoption prerequisite. That would press toward offering, treat folder/layout compliance as evidence, and lose the executive's choice.

My main effort is the short decision guidance that preserves the true origin and limits of existing know-how. Navigation and test repair serve access and trust in that guidance; they do not justify weakening context requirements.

## Choices against the measures

### Existing know-how

1. Existing practice: refer executives directly to standard 1.0 and steps 6–7. This adds no reading or maintenance, but leaves the possession/development distinction and the decision to do nothing implicit. It repeats the present gap.
2. **Chosen:** a separately linked `EXISTING.md`, read only when considering existing holdings. It gives a per-piece decision, distinguishes development from supply, and routes chosen complete bundles through the existing check/offer procedure. This meets choice, context and M10 without another command. It costs a small guide and one allowlist entry.
3. Challenge to that preference: an inventory/conversion command that reports candidate bundles and missing fields. It could reduce repetitive checking in large uniform collections, but cannot infer origin or successful use, and would add scanning policy and maintenance before any project's actual effort is known. Existing `check_contribution.py` already reports missing/unknown context for a supplied bundle. No new command earns its place now.

### Reaching the capability

1. Put an absolute path or a fixed edition number in the listing sentence. Easy on one machine, but violates generic copying or becomes stale and cannot identify later catalogues. Excluded by the measures.
2. **Chosen:** one generic sentence points to INDEX.md at the supplied published location, with USE.md as the clone entry. The mutable publisher index names the current fixed capability and current catalogue; USE explains the no-index clone case using existing pack/init/publish commands. OWNER documents the index contract. No new publication format or locator service is needed.
3. Challenge to that preference: add a machine-readable capability pointer and resolver command beside the existing catalogue block. This offers stronger automated navigation, but adds a format/command for prose navigation an agent can already do. It cannot manufacture a curator catalogue for a bare clone. Reconsider only if prose navigation fails in actual taking work.

A bare clone has no publisher's current fixed edition or catalogue. The guide must say this honestly and explain making a local fixed edition and empty catalogue; it must not imply either is downloaded or discovers shared material. A publisher-backed listing should name its published index/location, rather than a historical edition directory, to retain current discovery.

### Validation

1. Narrow OWNER to source-only testing or skip the whole combined test in editions. Low effort, but edition-only takers lose the promised validation and source packing becomes conflated with runtime coverage. Rejected.
2. **Chosen:** separate packing-specific assertions from reusable edition runtime assertions. In source, pack twice in a temporary source and verify determinism, inventory and fixed-edition rejection. In an edition, use a disposable detached copy of that edition directly for runtime checks. Both routes exercise self-check, ask/select, standalone check, ownership rejection and unchanged edition bytes; source packing remains tested. The suite should explicitly test that a fixed edition cannot pack. No deletion of a marker to masquerade as source.
3. Challenge to that preference: synthesize a temporary source fixture by copying only the manifest's payload and then pack from that fixture even when tests start in an edition. It preserves a single test route and may be smaller, but changes an edition into source for the central validation exercise and can hide an edition-only assumption. Separate responsibilities make the edition route easier to assess. Exact factoring can be decided during implementation within this choice.

## Draft listing line and guide text

First line of USE.md, copied unchanged into a listing that supplies its own location:

> Shared know-how with context: at the listed location, read INDEX.md for the current capability and catalogue, or USE.md in a clone.

Draft opening immediately after that line:

> With a publisher's INDEX.md, follow its current capability edition, verify its external manifest hash and listed files, then read that edition's USE.md. Give that same index to ask/select as INDEX; it names the current catalogue. Resolve its paths from the index's directory. Do not infer current editions from directory names.
>
> With only a clone, this USE.md is your entry; no shared catalogue is included. To take a fixed local edition, run `python "SOURCE/knowhow.py" pack-capability --project "SOURCE" --edition capability-002`, where SOURCE is this clone. Keep the returned manifest hash, verify the stage's manifest and listed files, and use its returned stage path as EDITION. Packing stages locally; it does not publish. Initialize your own separate PROJECT with step 1 below. For an empty local catalogue, run `python "EDITION/knowhow.py" publish-catalogue --project "PROJECT" --edition catalogue-001`; use `PROJECT/published/INDEX.md` as INDEX. This catalogue contains no shared know-how. To use a curator's catalogue later, supply that curator's published index through your arrangement. OWNER.md explains publication and validation.
>
> If your executive is considering know-how the project already holds, read [Existing know-how](EXISTING.md). Otherwise continue below.

Existing steps 1–7 and their semantics remain, with step 1 identified as already done if the clone route initialized PROJECT. This draft uses existing commands only. It will be checked against an invented empty clone/taker flow after GO; it introduces no real curator decision or intake.

Draft `EXISTING.md` in full:

> # Know-how your project already holds
>
> Your project's executive decides separately for each piece whether offering it serves the project and is worth preparing its context and generic kit. Keeping it local or deferring is a complete choice. Taking the capability requires no inventory, conversion or offers. Start from your own project's holdings, whatever their format or folder name; do not inspect another project's private collection.
>
> First establish where the technique developed. If your project invented or materially refined it in real work, record that project and situation in `origin`, use the corresponding `origin.development_kind` (`invented` or `materially_refined`), and explain what was developed. Importing, renaming or copying advice is not material refinement. A refinement's account preserves its received basis and identifies the actual change and supporting use.
>
> If your project merely received a copy, preserve the developing project's origin, development kind and evidence. Your project supplies the copy; it does not become its developer. An unchanged complete bundle may be offered with that context intact. Copies of the same bytes have one content identity and several suppliers, not several independent successes. Record your project's actual use only if it happened, with its own situation, outcome and supporting facts; possession or inspection is not use. Changed bundle bytes receive a new identity and require fresh admission.
>
> For any piece you choose to prepare, use the [standard and its review obligations](standard/STANDARD.md) and [template](standard/PATTERN.template.md). Supply the explanation and structured context: origin, applicability, dated citable successful real use, failures and other adverse evidence, verification scope, limits, relationship to originating practice, and a deployable generic kit. Existing material can supply these facts; reformatting cannot establish them. Review the working collection's parent index, layout and contribution procedure too. You need not rename your existing collection or convert its other contents.
>
> Keep unknown facts null where the standard specifies null, and explain uncertainty; use its explicit unknown states where available. Do not replace an unknown with a plausible account or an empty list. The check reports incompleteness; it does not recover facts or prove truth. If you cannot supply the required context, leave the piece unoffered. Preparation and review effort depends on the evidence you hold; no project completion time has yet been established.
>
> When you choose to offer a complete bundle, verify its evidence and generic assets and follow USE.md steps 6–7 in your own project. The check and the receiving executive's admission review remain separate. Your working material stays local; the offer freezes the full context and kit. Later changes require a new offer; published offers stay fixed.

Draft OWNER index contract:

> A publisher's mutable INDEX.md must clearly name the current fixed capability edition, its relative directory, its EDITION.json SHA-256 and its USE.md entry, and explain that the current catalogue is the knowhow:v1 catalogue reference supplied to ask/select. Resolve relative paths from the index directory. Keep historical entries distinguishable from current pointers. The listing supplies this published location; fixed editions cannot name future editions or catalogues. A bare clone instead enters through USE.md and can stage a local fixed edition and create an empty catalogue with the existing commands. Publishing requires the complete fixed stage, unchanged, with its external manifest hash.

## Implied tasks, responsibility and timing after GO

I will carry all tasks, in this order:

1. Refine the draft for brevity and verify its branches against invented cases: own invention, received complete copy, real material refinement, unknown provenance/context, no kit, and a choice to defer. The standard stays authoritative and unchanged.
2. Add the optional guide and entry text; extend the packing allowlist to include it. Update OWNER's index contract and precise source/edition validation instructions. Preserve provider independence and portable paths.
3. Separate source packing tests from edition runtime validation, keeping the pack guard. Add only checks needed for the changed validation route and clone bootstrap.
4. Run the unit suite and standard render check from source and from a disposable fixed-edition copy, on the available Python 3.13 and 3.11 interpreters. Exercise the empty clone instructions and confirm empty ask returns no offers. Check fixed-edition immutability and source packing coverage, using only invented temporary projects. Inspect the final tracked diff for personal paths or real material.
5. Update UPDATE.md, stage `.staging/capability-002` from source, verify the manifest and every file, then report outcomes, exact validation environments, limits, friction and the external hash. No write to published/, no commits or pushes.

Planned UPDATE classification: `Significant change: no`, because this adds guidance/navigation and fixes the promised validation route without changing authority, runtime state, standard 1.0, publication version 1 or existing offer compatibility. Explain the new optional reading and entry behavior and that existing offers need no migration. If implementation reveals a significant behavioral change, reassess rather than retain that label mechanically.

## Resources, limits and referral

One writer is sufficient: the guide, entry contract and test route are closely related and fit this task's scope. No division proposed. I used local read-only file inspection for this backbrief; no network, external service or other-project reading was needed. After GO, use Python standard library and the supplied Python interpreters only; interpreter locations remain out of tracked capability files.

I cannot run Windows or Python 3.9 here, establish real project preparation effort, publish on the executive's behalf, or push. Python 3.9 syntax checking can support compatibility but will not be called runtime validation. I need no further decision within the assigned boundaries. The prescribed next step is the executive's consideration of this backbrief and recorded GO; this run now ends as directed.
