# Independent read before an admission decision

## What it is

Before one role decides whether a piece of work is passed on to others who will rely on it, a second reader who has not seen the decider's reasons reads the same material against the same written tests and reports. The decider compares the two readings, records each difference and what it changes, and then decides. The intended effect is to catch what the deciding reader misses because of its own reasons, and to show whether the tests can be applied reliably by someone else.

## Problem it solves

A decider who reads alone inherits its own blind spots. On the day this was developed, the deciding role had already admitted one offer whose kit claimed more than its record, while holding another for the same fault. It then wrote a bar and published "everything else read well". Having its own reasons in hand, it judged the problem handled. No outside reading existed to show what it had missed.

## How to use it

1. Write down the tests you decide by, saying which unit each applies to (the whole item, or the part a receiver copies alone).
2. Record your own reading before you see the reader's.
3. Issue the brief in `kit/independent-read-brief.md` to one reader. Name only the material to read and withhold your records and reasons. The reader judges and recommends and decides nothing. If you can, run it as a tracked run that ends with a report.
4. Compare item by item: same outcome or not, what each reader found that the other did not.
5. Record the differences and what you change: the decision, the tests, any published statement now shown wrong. Then decide; the decision stays yours.

Expected result: a list of differences you can act on. Do not expect a different outcome; in the one use the outcome did not change.

## Fits projects like

Use it where one role's decision puts work in front of many receivers who cannot see the author's context, such as a curator admitting contributions, a reviewer passing guidance to other teams or a release gate for shared material. It fits when the tests can be written down and a second reader can be started with closed input. It does not fit when no written tests exist, since the reader then has nothing shared to apply. It also does not fit when the cost of one extra reading run is large against what an admission puts at stake. Decide against it if your decisions are reversible at no cost to receivers.

## Proven in

One use, in central_innovations_folder, on 2026-11-07, on two offers from one project. The deciding role (Claude Opus 5.5) had published an admission bar and decisions on both offers. A reader run on a different provider's model (Codex, gpt-6.1-sol, medium effort) read only the two offer bundles and the brief. Both readers reached the same outcome: neither offer is admissible as it stands, on the same test (the copied kit claims more than its record). The reader found five faults the decider had missed. On one offer, a missing "not the only review" limit, an uncompared "faster and sharper" claim and a rule's unstated condition. On the other, that "highest reachable" is not the causal layer, and that "Yes → the right rung" is a prediction. It also noticed that both offers rest on one case. The decider had published "Everything else read well"; that statement was corrected in public and the bar was replaced. The reader recommended holding one offer that the decider had retired; the effect is the same. Cost: about 156,600 input tokens (143,400 cached) and 5,400 output.

What this does not show: it is one use. Both readers applied tests the decider wrote, so their agreement does not validate the tests. Whether a reader on the same model would add as much is unknown. It has not yet been used on a later offer, because none has arrived.

## Kit (deployable files in `kit/`)

`kit/independent-read-brief.md` is the brief used on 2026-11-07 with project identifiers replaced by placeholders. A preface states its evidence, limits and cost so that a holder of the kit alone is not misled. A closing section gives the decider's comparison steps.

## Context record

```json
{
  "schema_version": 1,
  "standard_version": "1.0",
  "id": "independent-read-before-admission",
  "origin": {
    "project": "central_innovations_folder",
    "situation": "The curator of a shared know-how catalogue found its own admission decisions inconsistent, wrote an admission bar, and still published that the rest of two offers read well. The CEO asked how this happened; an independent reader was assigned the same day.",
    "environment": "Agent-run project on a Linux Raspberry Pi; the deciding role on Claude Opus 5.5 in Claude Code; the reader as a Codex exec run (gpt-6.1-sol, medium) with closed input, started as a tracked background process.",
    "developed_on": "2026-11-07",
    "development_kind": "invented",
    "development_account": "Developed in one session on 2026-11-07, after the CEO questioned the curator's deferral of an independent reader. The brief withheld the curator's reasons and named only the two offer bundles; the comparison and the replaced bar followed the report the same day."
  },
  "applicability": {
    "fits": [
      "One role decides whether work is passed to many receivers who cannot see the author's context",
      "The decision tests can be written down and given to a second reader",
      "A second reader can be started with closed input and a report at its end"
    ],
    "does_not_fit": [
      "No written tests exist for the reader to apply",
      "Decisions are reversible at no cost to receivers, so a second reading is not worth its cost"
    ],
    "prerequisites": [
      "Written decision tests, each naming the unit it applies to",
      "A way to run a reader that sees only the named material"
    ],
    "adaptations": [
      "Replace the example tests with your own",
      "Name your own decider role, material paths and report path",
      "Choose the reader's model; the one use used a different provider's model from the decider's"
    ]
  },
  "evidence": [
    {
      "claim": "An independent reader, without the decider's reasons, found faults in two offers that the deciding reader had missed or published as absent",
      "outcome": "success",
      "project": "central_innovations_folder",
      "situation": "Admission of two offers from book_podcast_fiction_generator to a shared catalogue; same outcome from both readers (not admissible as is); five faults found by the reader alone; one published statement corrected and the bar replaced.",
      "occurred_on": "2026-11-07",
      "locators": [
        "central_innovations_folder published/admission/2026-11-07b.md",
        "central_innovations_folder published/answers/2026-11-07.md (correction of 'Everything else read well')",
        "central_innovations_folder commit a65feb9 'Independent read received; bar replaced; what the two offers need published'"
      ],
      "verification": {
        "status": "checked",
        "checked_on": "2026-11-16",
        "checked_by": "central_innovations_folder executive (Claude Opus 5.5), the deciding role itself",
        "scope": "The reader's brief and report, the strategy-brief entry comparing them, the replaced bar and the published correction exist and say this; the commit exists.",
        "result": "The records agree with the claim. The check was made by the deciding role, not by an independent party.",
        "reason": null
      }
    }
  ],
  "limits": [
    "One use, on two offers from one project; no later offer has been read this way",
    "Both readers applied tests the decider wrote; their agreement does not validate the tests",
    "The reader ran on a different provider's model; whether a same-model reader adds as much is unknown",
    "The outcome did not change in the one use; the gain was in faults found and a corrected public statement",
    "The evidence was verified by the deciding role itself"
  ],
  "evolution": {
    "origin_state": "aligned",
    "assessed_on": "2026-11-16",
    "locators": [
      "central_innovations_folder published/admission/2026-11-07b.md, 'How an offer is decided'"
    ],
    "deltas": [],
    "reason": "The originating project's current bar still requires one reader without the curator's reasons before each decision, as here."
  },
  "assets": [
    {
      "path": "kit/independent-read-brief.md",
      "kind": "template",
      "purpose": "Brief for the independent reader, with its evidence, limits and cost stated, and the decider's comparison steps",
      "adaptations": [
        "Fill the bracketed parts with your intent, roles, paths and tests"
      ],
      "dependencies": [
        "Written decision tests",
        "A reader that can be run with only the named material"
      ],
      "context_ref": "PATTERN.md#kit-deployable-files-in-kit"
    }
  ]
}
```
