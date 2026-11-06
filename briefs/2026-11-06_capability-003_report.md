# Capability edition 3 report

All nine items completed. No item required a format change or a new command. Stage only; no publication, commit or push performed.

## Outcomes

1. `capability/EXISTING.md`: the unoffered-copy restriction explicitly concerns a copy the holder did not develop. Material refinements of a described but unnamed base may be offered, with the refining project's origin, `materially_refined`, the received basis in the records' words, the unnamed developer, the actual changes and the project's own successful uses. Unchanged use remains a copy.
2. `EXISTING.md`: development without a received copy is `invented` despite resemblance to common practice; this claims development rather than novelty. Unknown influence belongs in the development account.
3. `EXISTING.md`: two sentences require correcting the kit alongside corrected or withdrawn claims before offering, and limiting its claims to what the record supports.
4. `capability/USE.md`: preservation guidance covers local commits, the edition-specific `.gitignore`, restoring identity, retaining declines and use records, catalogue hashes/local paths, every-command cost writes, the cost-reading tradeoff and the executive's remote-push decision.
5. `USE.md`: verify the manifest and listed files, then run without `-I`; explains script-folder imports and the remaining `PYTHONPATH` consideration.
6. `USE.md`: check the curator's index first, publish unresolved questions under “Questions for the capability” in the project's own published index with attempt/result/need, and continue unblocked work. Reading requires the curator's next run and access to that published part; its index locates answers.
7. `capability/OWNER.md`: index duties now include reading listed parts' indexes for questions because intake only reports counts, publishing answers and locating them in the curator's index.
8. `capability/standard/definition.py`: asset-path description includes the `kit/` prefix and `kit/guide.md`; the checker already uses that description for invalid-path messages, so its acceptance logic needed no change. Added a definition-owned example and minimal renderer support to populate the template path. Regenerated `STANDARD.md` and `PATTERN.template.md` using `standard.render`; neither generated file was edited by hand. Extended the path test to check invalid state and the prefix/example in messages, including a prefix-free path. Standard 1.0 and publication formats remain unchanged.
9. `capability/UPDATE.md`: edition 3, `Significant change: no`, with the reason, changes and taking impact. Updated the packing example in `OWNER.md` to `capability-003`. Staged using `pack-capability`.

## Stage and integrity

Stage: `capability/.staging/capability-003/`

External SHA-256 of `EDITION.json`:

`229794fbc843b14bfd2f4b01c2c4d5dd1ad37b9a1c4cf932b8ce4392b2fb9df3`

Verified the external manifest hash, all 20 listed file sizes and SHA-256 hashes, exact inventory (listed files plus `EDITION.json`), and equality to current source bytes. Reverified the stage and disposable copy after testing; every file still matches. Scanned packed text for the local home path and the project/technique identifiers from the answers; none were present.

## Commands and results

Working directory for source checks: `capability/`. Python executables were `python3` (3.13.5) and `/home/mr/.local/share/uv/python/cpython-3.11.15-linux-aarch64-gnu/bin/python3.11` (3.11.15).

- `python3 -B -m standard.render`: succeeded; generated the two standard documents.
- For each executable, `-B -m unittest discover -s tests` from source: 36 tests, all passed, no skips (3.13: 6.257 s; 3.11: 5.978 s).
- For each executable, `-B -m standard.render --check` from source: passed, exit 0.
- `python3 -B knowhow.py pack-capability --project . --edition capability-003`: succeeded, 20 files, hash above.
- Copied the complete stage to `/tmp/capability-003-validation-6o03u5pd/edition`; retained its edition marker.
- For each executable, `-B -m unittest discover -s tests` from that disposable copy: 36 tests, passed with exactly one intended skip, `test_source_packing_is_deterministic` (“Packing requires developing source”); detached operation and edition packing rejection ran (3.13: 10.086 s; 3.11: 9.307 s).
- For each executable, `-B -m standard.render --check` from that copy: passed, exit 0.
- Independent Python standard-library integrity checks before and after copy validation: passed.

Tests used invented projects in temporary directories. No `init`, `offer`, `ingest` or `publish-catalogue` command targeted this project's root.

## Friction and resources

No blocker. `capability/` is ignored by the enclosing repository, so its changes do not appear in the enclosing `git diff`; inspected the edited files directly and verified stage/source equality instead. Existing changes to the root `.gitignore` and `.knowhow/curator/catalog.sqlite` were present at entry and were left alone.

One agent; no subordinates, network, external dependencies, publishing, commits or pushes. Read only the assigned brief under `briefs/`, the named answers and capability source/guides/tests within this project; used the required installed interpreters. Writes were confined to capability source/staging, temporary synthetic validation directories and this report. The pack command wrote its own staging cost journal. Temporary validation copy was removed after final integrity verification; the fixed stage remains for the executive. No claims of real reuse savings, Python 3.9 execution or other-platform validation are made.
