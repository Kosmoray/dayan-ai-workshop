# AI Workflow Governance

AI workflow governance is the set of boundaries, checks, and handoffs that lets a team use AI agents without losing control of data, actions, quality, or accountability.

## Why It Matters

Teams rarely fail because an AI tool cannot draft text or code. They fail when nobody knows:

- what the AI was allowed to read;
- what the AI was allowed to change;
- who approved risky actions;
- how the final answer was verified;
- where the work record lives after the session ends.

## Minimal Model

| Layer | Question | Artifact |
|---|---|---|
| Context | What does the AI know? | Skill, project notes, source list. |
| Action | What can it do? | Tool policy, permission list. |
| Control | What must be blocked or approved? | Hook, redline library. |
| Verification | How is done proven? | Verifier, test, checklist. |
| Handoff | How does the next session continue? | Status note, summary, decision log. |

## When To Use

Use this when AI agents interact with real work:

- code changes;
- customer documents;
- research workflows;
- internal knowledge bases;
- scheduled automation;
- multi-step operational tasks.

## When Not To Use

Do not overbuild governance for a one-off draft, brainstorming note, or reversible personal task. The amount of governance should match the risk.

## Related

- `docs/glossary/verifier.md`
- `docs/patterns/skills-hooks-verifiers.md`
- `templates/permission-redline-library.md`
