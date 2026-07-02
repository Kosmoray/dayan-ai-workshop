# Dayan Workshop Map

Dayan AI Workshop organizes reliable AI work into five surfaces.

```text
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Context    │ -> │    Action    │ -> │   Control    │
│ skills/docs  │    │ tools/APIs   │    │ redlines     │
└──────────────┘    └──────────────┘    └──────────────┘
                                             |
                                             v
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Handoff    │ <- │ Verification │ <- │   Evidence   │
│ status notes │    │ verifiers    │    │ tests/sources │
└──────────────┘    └──────────────┘    └──────────────┘
```

## The Five Surfaces

| Surface | Question | Artifact |
|---|---|---|
| Context | What should the AI know? | Skills, source lists, project notes. |
| Action | What can the AI do? | Tool policy, command scope, API scope. |
| Control | What must be blocked or approved? | Permission redlines, hooks, review gates. |
| Verification | How do we prove done? | Verifiers, tests, checklists. |
| Handoff | How does work continue later? | Status notes, decision logs, next actions. |

## Design Principle

Do not make the model remember your operating system. Put the operating system into files, rules, and checks.
