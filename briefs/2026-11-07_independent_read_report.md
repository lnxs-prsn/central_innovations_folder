# Independent read of two offers

2026-11-07. Report to the project's executive under `briefs/2026-11-07_independent_read.md`.

I would **hold both offers for correction**, chiefly because their deployable kits do not carry the qualifications and corrections in their records. These are recommendations only; I made no admission decision or offer changes.

## Scope and interpretation

I read every file found in the two authorized bundle folders, including a second inventory with hidden and ignored files included. Each bundle contained one `PATTERN.md` and one kit file. Below, **R** means `.knowhow/curator/offers/c12e9a992213eb771222461400e4df8b2f84c0127c94ebe50f47b6ad79adeb4f/bundle/root-cause-laddering/`; **S** means `.knowhow/curator/offers/7c8dd8e8d45a96cd8bd03d102f7eb583b1fc34eb2dfec3034ea6c8bde05b0356/bundle/situation-personification/`. File citations use these prefixes.

I take test 1 as a supplied premise, as instructed. I assess test 2 from the offered citations and verification accounts, without opening the source repositories. A successful use can be a documented diagnostic decision implemented in that project; it need not establish general effectiveness. I assess tests 3 and 5 across each whole offer, while test 4 explicitly requires the kit to stand on its own without misleading its holder. Thus a bundle can pass the visibility test and fail the kit agreement test. This distinction matters to the judgments below.

## Offer R: root-cause laddering

### 1. Complete and intact — PASS, supplied premise

The brief's test 1 says: “taken as given, the check reports complete presence and the bytes verified” (`briefs/2026-11-07_independent_read.md`). R's asset record names `"path": "kit/LADDER.md"` (`R/PATTERN.md`, context record, assets), and that file is present and was read. I did not independently verify a manifest or hashes; none is supplied within this bundle. Presence of the two readable files alone would not prove byte integrity.

### 2. Real development and real use — PASS, narrow documentary scope

The origin records `"project": "book_podcast_fiction_generator"` and `"developed_on": "2026-07-19"`. The first successful evidence claim is “Laddering moved a repeated ticket-bounce problem from each ticket to the authoring template,” dated `2026-07-19`, citing `commit b615571`, `commit ef7ebf5`, and `progress/handoff-2026-07-18-all-tickets-landed-ch7-next.md section 14` (`R/PATTERN.md`, context record, origin and evidence).

The verifier is named as “Claude Opus 5.5 agent session working in book_podcast_fiction_generator,” checked on `2026-11-05`; its scope is “Commits exist; the handoff section names the bounce class and the authoring fix.” A second success cites retirement of a component and a regression suite, commits `f739452` and `12ed7b9`, with verification limited to “Commits and ticket files exist and say this” (same file, evidence).

This supports actual use and recorded changes, not a demonstrated reduction in recurrence or proof that laddering caused the improvement. The later bounce does not erase the earlier use, but does rule out treating that use as lasting elimination of the class.

### 3. Failures, limits and corrections visible and believable — PASS across the offer

“The 2026-07-19 authoring fix was judged high enough and was not: T-024 and T-025 bounced on 2026-07-21 because acceptance results were predicted, not executed” (`R/PATTERN.md`, Proven in). This is a specific, dated counterexample to the method's own altitude judgment, with a commit citation and verification account.

The retained correction says the earlier account called the roughly 40% pass rate an authoring defect and “not the model,” then corrects it: “Climbing found the authoring defect too; it did not clear the lower layer.” The record also says “The one-layer-up prior is a heuristic from one project over a few weeks; no rate has been measured” (same file, Proven in and limits). These admissions are credible in relation to the modest recorded uses. Their absence from the kit is a separate failure below.

### 4. Record, explanation and kit agree; kit alone does not mislead — FAIL

The kit says “It stops whack-a-mole,” “Fix at the highest reachable rung — that's where the category dies,” and “The root cause is usually the thing that **fed** that suspect” (`R/kit/LADDER.md`, introduction, second question and prior). It presents the final check as “Yes → you climbed to the right rung.”

Against those assurances, the record says “no rate has been measured” and “The stopped-too-early check is applied by judgment and did not catch this in advance” (`R/PATTERN.md`, limits and failure verification). Highest reachable is also not necessarily the demonstrated causal layer. The kit gives neither the observed failure nor the warning that lower-layer defects can remain, nor the single-project verification limit. The explanation acknowledges these qualifications but still uses broad language such as “the bugs concentrate in the *change-governance* layer” (same file, Problem it solves). A kit-only receiver would reasonably infer more reliability and causal reach than this evidence supports.

### 5. Receiver can judge fit — PASS across the offer, with a kit portability concern

The record requires “A record of past failures and fixes detailed enough to walk the layers.” It excludes “A one-off failure with no recurrence, where the instance patch is sufficient” and names “Cases where the higher rungs are outside your control” (`R/PATTERN.md`, applicability). The origin gives the concrete environment: one human owner, senior and junior AI agents, tickets, deterministic gates and paid LLM calls.

Those distinctions let a receiver reject use for an isolated incident, an untraceable failure, or an inaccessible organizational layer. The control boundary is partly an adaptation, since the same exclusion says to stop at the highest changeable rung. That wording could be clearer. The kit's broader “shouldn't have happened” trigger and omitted prerequisites weaken fit judgment when copied alone; I count that under test 4 rather than fail test 5 a second time.

### 6. Generic kit — PASS

The ladder uses generic rungs such as “the spec / work-order / config that drove the tool” and “the process that governs authoring & verification” (`R/kit/LADDER.md`, second question). It contains no origin project name, ticket IDs, or commits requiring replacement. “Pairs with **cast-and-fit**” is an optional cross-reference; the ladder itself is usable without that other kit. Generic wording does not remedy its overstatement.

### Recommendation and correction

**Hold for correction.** Preserve the dated evidence, failure and correction. In both explanation and kit, frame one-layer-up as a hypothesis to investigate, not an established frequency or a guarantee of prevention. Replace the highest-reachable instruction with a requirement to establish the causal layer and choose a feasible intervention there; identify residual causes when control stops short. Retain lower-layer repair where evidence calls for it. Treat the stopped-too-early question as a prediction to test against observed outcomes, not a yes/no proof.

The kit should carry a short statement of its actual basis: documentary uses in one AI-run project, verification by an agent in that project, no independent reuse or measured rate, and an authoring fix that failed to prevent later bounces. Add the recurrence/traceability prerequisites and the one-off exclusion. These changes require no invented evidence.

## Offer S: situation personification

### 1. Complete and intact — PASS, supplied premise

The same brief premise applies: “taken as given, the check reports complete presence and the bytes verified” (`briefs/2026-11-07_independent_read.md`). The asset record names `"path": "kit/CAST-AND-FIT.md"` (`S/PATTERN.md`, context record, assets), which is present and was read. I did not independently verify bytes.

### 2. Real development and real use — PASS, narrow documentary scope

The record names `book_podcast_fiction_generator`, development on `2026-07-19`, and the successful claim “Question 3 flipped a decision from building a babysitter ticket to retiring the component,” occurring that day. It cites commits `ba7204b`, `f739452`, `b615571`, the T-017 ticket, and handoff section 14 (`S/PATTERN.md`, origin and first evidence entry).

Verification on `2026-11-05` by “Claude Opus 5.5 agent session working in book_podcast_fiction_generator” is scoped to “Commits and ticket exist; the handoff records the Q3 reasoning and the retirement” (same file). That is a named, dated, citable use with a concrete decision and implementation. It does not verify a general advantage over flow diagrams or long-term safety of retirement.

The other claimed successes are weaker corroboration: “most of them not yet proved by a build,” and “This is the earlier story form, not the five questions” (same file, evidence verification). I do not treat those as independent validations of the five-question method.

### 3. Failures, limits and corrections visible and believable — PASS across the offer

“The next day a structurally different adversarial and reader-outcome pass found defects this family missed,” and “Casting three ways was still one method” (`S/PATTERN.md`, Failed or limited). The evidence gives concrete missed defects, a dated source, and even qualifies the competing review: “The same document's ADV-3 framing was later retired as wrong, so that pass was not error-free either” (same file, failure verification).

The retained correction is explicit: “It said Q1 separately confirmed the remaining checks did not overlap; no record of that was found, so it is removed” (same file, correction). The record limits the support to one project and an agent working there. These are believable limits for a story-based diagnostic. The correction has not actually reached every file, which causes the next failure.

### 4. Record, explanation and kit agree; kit alone does not mislead — FAIL

The kit still says: “Question 1 confirmed the remaining checks didn't overlap: the system wasn't bloated, it had one bad hire” (`S/kit/CAST-AND-FIT.md`, worked example). The record specifically retracts that claim: “The earlier claim that Q1 separately confirmed no overlap among the remaining checks was not found in these records” (`S/PATTERN.md`, first evidence verification). Labeling the example “illustration” does not remove the conflict: it closely retells the documented incident and makes the withdrawn confirmation appear to be part of that successful use.

The kit correctly says “never a proof” and “Always check the story against the actual mechanics before acting on it” (`S/kit/CAST-AND-FIT.md`, introduction). But it omits the observed blind spots and the explanation's instruction “Use it alongside lenses of a different kind, not as the only review” (`S/PATTERN.md`, Failed or limited). Checking the mechanics of a nominated problem does not ensure discovery of the flow, adversarial or reader-outcome problems the casting never nominated.

Finally, “It works because” social intuition is “fast and sharp” in the kit, and “far faster and sharper” in the explanation, express a comparative mechanism without comparative evidence (kit introduction; explanation, What it is). Documented usefulness in one decision does not establish that broader claim.

### 5. Receiver can judge fit — PASS across the offer

The record fits “Deciding whether a component should exist, is redundant or is a bad fit” and making structure legible to a reviewer. It excludes “Anything you measure rather than narrate: performance, numeric correctness, proofs” and use “As the only review lens.” Its prerequisite is “The ability to check the story against the actual code or data before acting” (`S/PATTERN.md`, applicability).

Together with the finding that casting was “strong on roles and blind to pure flow problems” (same file, Proven in), these supply concrete reasons to reject or supplement it. The kit carries some of these exclusions, but omits the complementary-review requirement; that omission is counted under test 4.

### 6. Generic kit — PASS

“Each component, agent, tool, check, rule — and yourself — becomes a person with a job and a temperament” (`S/kit/CAST-AND-FIT.md`, How to run it). The example uses a generic pipeline, inspector and sibling check. It contains no origin project identifiers, commit references or ticket names. A receiver can cast its own parts without obtaining a project-specific asset.

### Recommendation and correction

**Hold for correction.** Remove the withdrawn Q1 confirmation from the kit's worked example and retain the correction history in the record. Present the example as the documented decision with its limited verification scope, or make any invented portions unmistakably hypothetical. Add the single-project evidence limit, the missed flow/adversarial/reader-outcome problems, and the requirement for a structurally different review alongside mechanical confirmation.

Soften the claims about speed, sharpness and what a flow diagram cannot reveal into a proposed rationale or a description of the observed case. The Q3 instruction to prefer retiring or re-onboarding a part that needs support also needs a qualification: dependence on another component is a clue to investigate, not by itself evidence of bad fit. The observed retirement had additional support—a downstream gate already covered the job. Preserve that condition when teaching the example.

## Uncertainty and fair disagreement

- **What counts as successful use?** I pass test 2 for implemented diagnostic decisions supported by dated verification accounts. A reader requiring demonstrated downstream improvement could fail R, and could ask for stronger safety/outcome evidence for S. The bar should distinguish successful application from verified effectiveness; these offers substantiate the former more clearly.
- **Where must limits travel?** I pass tests 3 and 5 for the whole bundles and fail test 4 for the isolated kits. A reader who applies all three tests to the copied kit could also fail tests 3 and 5. Both approaches identify the same practical correction. The bar could specify its unit of assessment for each test.
- **What does “illustration” permit?** A reader might allow a fictionalized Q1 confirmation in S. I do not, because it is narrated as a completed event within a close retelling of the verified case, without identifying that detail as invented, and the record expressly withdrew it.
- **How much skepticism about provenance?** These are source-project verification accounts, not source materials I independently inspected. Test 1 establishes supplied-byte integrity, not the truth of those accounts. I neither assume fraud nor upgrade documentary checking into independent replication.
- **Method boundaries:** R's “highest reachable” instruction may be intended as shorthand for the highest relevant causal rung, and S's babysitter rule may be intended only for unnecessary support. Their literal wording does not supply those qualifications. The additional retirement evidence in S makes a narrower interpretation plausible; a kit-only receiver may not infer it.

Neither offer warrants refusal on the evidence available: the problems can be corrected by narrowing claims and carrying existing context into the kit. Admission without those corrections would conflict with the brief's quoted intent that context wins over reach.

## What the tests may fail to catch

Several risks are partly addressed by the six tests but not fully resolved by satisfying them:

1. **Shared evidence can look like independent corroboration.** Both methods cite the same T-015-to-T-017 retirement, in the same project, assessed by the same named verifier description. Neither record hides this, but separate passes do not test dependence across offers. Receiving both kits should not double the apparent evidence or count their combination as two independent reviews.
2. **No explicit comparative-benefit or cost test.** A technique can have a real successful use, candid failures and appropriate fit yet add no value over ordinary reasoning. Neither bundle measures that counterfactual. R's climb can encourage needless governance work; S's “Cast every part” can consume substantial effort despite the kit's “One page, no upkeep.” The tests do not explicitly require cost, stopping criteria or comparison to a simpler approach.
3. **No explicit intervention safeguard test.** Fit and caveats can be accurate while the procedure still fails to require checking what a removal or higher-layer change will break. R prescribes shipping a class fix; S favors retirement for support-dependent parts. Neither kit explicitly requires assessing affected consumers, preserving necessary coverage, or planning reversal. This is a procedural gap, not evidence that either recorded change caused harm. Test 4 catches the known overclaims, but does not expressly demand safe implementation guidance for a fully supported intervention.
4. **No explicit evidence-accessibility test.** Commit hashes and project-relative paths are citable, but the bundles do not establish that a receiving project can obtain the cited records. A receiver may be able to assess the scope of the verifier's account while unable to inspect its basis. That is different from missing citations or failed byte integrity.

Other observed problems do have coverage: the stale Q1 claim and kit overconfidence fall under test 4; the missing kit caveats concern tests 3–5; single-project scope belongs under tests 2 and 3. I would not create extra tests merely to rename those failures.

## Resources used and completion

Read only the assigned brief and these four files: `R/PATTERN.md`, `R/kit/LADDER.md`, `S/PATTERN.md`, `S/kit/CAST-AND-FIT.md`. Used local shell file inventories and full-text reads, followed by writing this report. No network, source-repository checks, curator database access, other briefs, published material, or delegated readers. No commits. The only file written is this report. Model/token and elapsed resource totals were not available from these operations and are not estimated.
