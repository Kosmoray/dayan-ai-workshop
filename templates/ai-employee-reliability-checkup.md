# Template: AI Employee Reliability Checkup

Use this checkup before giving an AI agent a recurring role inside a team workflow.

## Goal

Decide whether an AI agent is safe and useful enough to perform a defined job with clear boundaries.

## Five Dimensions

| Dimension | Question | Score |
|---|---|---|
| Task clarity | Does the agent know exactly what job it owns? | 1-5 |
| Data boundary | Does it know what it may read and what it must not read? | 1-5 |
| Action boundary | Are risky actions blocked or approval-gated? | 1-5 |
| Verification | Is there a verifier for the output? | 1-5 |
| Handoff | Can another person or agent continue the work later? | 1-5 |

## Intake Questions

1. What job should this AI employee perform?
2. What inputs does it need?
3. What outputs should it produce?
4. Which actions are safe and reversible?
5. Which actions require approval?
6. What would count as a failed result?
7. How will the result be verified?
8. Where will the work record be stored?

## Report Skeleton

```md
# AI Employee Reliability Checkup

## Role

## Current Score

| Dimension | Score | Evidence |
|---|---:|---|

## Main Risks

## Required Guardrails

## Verifier

## Pilot Plan

## Decision
Ready / Ready with limits / Not ready
```

## Decision Rules

- **Ready**: all dimensions score 4 or 5, and high-risk actions are gated.
- **Ready with limits**: one or two dimensions score 3, with a clear pilot plan.
- **Not ready**: any dimension scores 1 or 2, or the agent can affect production, customers, payments, or secrets without approval.
