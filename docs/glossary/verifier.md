# Verifier

A verifier is an acceptance contract for AI work. It defines how to prove that a task is complete, safe, and useful before the result is shipped or trusted.

## Why It Matters

AI can produce confident output that looks finished while still missing the real requirement. A verifier turns “looks good” into concrete checks.

## Minimal Verifier Template

```md
# Verifier: <task type>

## Scope
What kind of work this verifier applies to.

## Must Pass
- Check 1
- Check 2
- Check 3

## Must Not Happen
- Failure mode 1
- Failure mode 2

## Evidence
- Command output, screenshot, source link, test report, or review note.

## Stop Conditions
When the task must stop and ask for human review.
```

## Examples

| Task | Verifier |
|---|---|
| Code change | Tests pass, changed files reviewed, no unrelated refactor. |
| Public document | Sanitization scan passes, sources are cited, claims are bounded. |
| Customer plan | Assumptions listed, risks named, next action clear. |
| Data crawl | Source tier recorded, robots and rate limits respected. |

## Failure Modes

- The verifier is written after the result, so it only rubber-stamps the work.
- The verifier checks formatting but not the actual business risk.
- The verifier is too vague: “make sure it is good.”
- Evidence is missing, so another person cannot replay the decision.

## Related

- `SANITIZATION.md`
- `docs/patterns/skills-hooks-verifiers.md`
