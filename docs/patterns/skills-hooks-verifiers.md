# Pattern: Skills, Hooks, Verifiers

This pattern separates AI workflow reliability into three small artifacts:

- **Skill**: how to perform the task.
- **Hook**: what must be blocked, warned, logged, or approved.
- **Verifier**: how to prove the result is acceptable.

## The Problem

Prompt-only systems ask the AI to remember every rule at once. That breaks down when tasks become long, risky, or repetitive.

## The Pattern

| Part | Job | Example |
|---|---|---|
| Skill | Encodes repeatable task knowledge. | “How to write a public comparison page.” |
| Hook | Enforces hard boundaries before or after actions. | “Block credential output.” |
| Verifier | Checks the final result against an acceptance contract. | “Run sanitizer, cite sources, record residual risk.” |

## Minimal Workflow

1. Define the task and expected output.
2. Write the skill in plain language.
3. Add hooks only for actions that can cause real damage.
4. Write the verifier before running the task at scale.
5. Keep the evidence with the result.

## When To Use

- recurring AI-assisted work;
- code or document delivery;
- customer-facing workflows;
- automation that can touch files, data, or messages;
- work that spans multiple sessions.

## When Not To Use

- pure ideation;
- low-risk disposable drafts;
- one-off personal notes;
- tasks where a human will rewrite everything anyway.

## Public Boundary

Public examples should describe the pattern, not expose private tool configs, customer workflows, or internal automation paths.
