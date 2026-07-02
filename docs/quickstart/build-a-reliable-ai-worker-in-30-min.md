# Quickstart: Build A Reliable AI Worker In 30 Minutes

This quickstart turns a vague AI assistant into a bounded workflow.

## Step 1: Name The Job

Bad:

```text
Help with marketing.
```

Better:

```text
Draft a weekly competitor update from approved public sources, then produce a review-ready brief.
```

## Step 2: Write The Mission Card

Use `examples/ai-worker-mission-card.md`.

Fill in:

- role;
- allowed inputs;
- forbidden inputs;
- allowed actions;
- approval-required actions;
- expected output;
- verifier.

## Step 3: Add Redlines

Use `templates/permission-redline-library.md`.

Start with three categories:

| Action | Level |
|---|---|
| Read public sources | Allow |
| Install tools or change local config | Warn |
| Publish externally or touch credentials | Block |

## Step 4: Define Done

Write a verifier before the agent starts.

Example:

```md
## Must Pass
- Sources are linked.
- Claims are separated from assumptions.
- No customer-identifying information appears.
- The final brief has next actions.
```

## Step 5: Keep The Handoff

At the end of every run, save:

- what changed;
- what evidence was checked;
- what remains risky;
- what the next agent or human should do.

## Result

You now have a small AI worker that can be improved over time without relying on chat memory or heroic prompting.
