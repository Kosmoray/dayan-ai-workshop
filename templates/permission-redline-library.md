# Template: Permission Redline Library

Use this template to define what an AI agent can do freely, what requires warning, and what must be blocked until a human approves.

## Permission Levels

| Level | Meaning | Examples |
|---|---|---|
| Allow | Safe and reversible. | Read public docs, summarize provided files, draft local text. |
| Warn | Usually safe, but worth recording. | Install a package, create a scheduled job, change local configuration. |
| Block | High-risk or irreversible. Requires human approval. | Delete data, publish externally, spend money, change credentials. |

## Redline Categories

| Category | Default Level | Rule |
|---|---|---|
| File deletion | Block | Never delete important files without explicit approval and a recoverable path. |
| Credential handling | Block | Never print, store, or transmit secrets. |
| External publishing | Block | Never post, email, or publish on behalf of a human without approval. |
| Payments | Block | Never buy services, subscriptions, or assets without approval. |
| Production deploy | Block | Require approval and rollback plan. |
| Package install | Warn | Record package name, version, source, and reason. |
| Scheduled automation | Warn | Record schedule, command, output path, and disable method. |
| Public web research | Allow | Use public sources; cite links; respect source terms. |

## Agent Permission Matrix

| Agent Role | Can Read | Can Write | Needs Approval |
|---|---|---|---|
| Research assistant | Public sources, provided docs | Draft notes | External messages, private data sources |
| Coding assistant | Project files | Local code changes | Destructive git operations, production deploy |
| Operations assistant | Status files, logs | Local checklists | Cron jobs, credentials, notifications |
| Customer assistant | Redacted materials | Draft reports | Sending to customers, naming real clients |

## Review Questions

- Is the action reversible?
- Could it expose private data?
- Could it cost money?
- Could it affect a customer or production system?
- Is there a clear evidence trail?

## Evidence Log

```md
Date:
Action:
Level:
Reason:
Approver:
Evidence:
```
