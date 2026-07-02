# Gallery: Redacted Workflow Examples

These are public-safe, anonymized examples. They are not customer case studies.

## Example 1: AI Coding Assistant

| Before | After |
|---|---|
| “Fix this bug.” | Mission card + changed-file scope + test verifier + handoff note. |

Why it matters:

- prevents unrelated refactors;
- makes test evidence visible;
- leaves the next maintainer a clear trail.

Starter artifacts:

- `examples/ai-worker-mission-card.md`
- `docs/glossary/verifier.md`

## Example 2: Weekly Research Brief

| Before | After |
|---|---|
| “Summarize the market.” | Approved sources + claim/assumption split + source tier + review checklist. |

Why it matters:

- separates facts from guesses;
- avoids over-trusting secondary sources;
- gives the reviewer a fast acceptance path.

Starter artifacts:

- `templates/permission-redline-library.md`
- `docs/patterns/skills-hooks-verifiers.md`

## Example 3: Internal AI Employee Pilot

| Before | After |
|---|---|
| “Let the AI handle operations.” | role boundary + allow/warn/block matrix + reliability checkup + pilot decision. |

Why it matters:

- blocks risky actions;
- defines what the AI can read and write;
- makes “ready / ready with limits / not ready” explicit.

Starter artifacts:

- `templates/ai-employee-reliability-checkup.md`
- `templates/permission-redline-library.md`
