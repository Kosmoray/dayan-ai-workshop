# Sanitization Record

This file records the public-release checks for Dayan AI Workshop.

## Public Layers

| Layer | Can publish? | Examples |
|---|---:|---|
| Public | Yes | General methods, templates, glossary pages, redacted examples. |
| Client-redacted | Only after redaction | Industry scenarios, anonymized before / after workflows. |
| Internal | No | Private operating notes, customer-specific strategy, personal memory. |
| Secret | Never | Credentials, keys, private keys, seed phrases, contracts with sensitive terms. |

## Required Scans

Run these before any public push:

```bash
grep -RInE "API_KEY|SECRET|TOKEN|PRIVATE KEY|BEGIN RSA|BEGIN OPENSSH|seed phrase|private key|keystore|\\.env" . || true
grep -RInE "customer name|real client|internal codename|private memory|unverified revenue|valuation" . || true
grep -RInE "/Users/|/Desktop|\\.cache|\\.config|private workspace" . || true
```

## Current Check

Date: 2026-07-02

Status: public P0 release completed.

Published repository:

- https://github.com/Kosmoray/dayan-ai-workshop
- Branch: `main`
- Published commit: `a83c7cfdf53588fa57db6ed6826e45672f20e73e`

Commands run from repository root:

```bash
grep -RInE --exclude=SANITIZATION.md "API_KEY|SECRET|TOKEN|PRIVATE KEY|BEGIN RSA|BEGIN OPENSSH|助记词|私钥|keystore|\\.env" . || true
grep -RInE "internal codename|private role name|real client|customer-identifying|internal campaign|unverified revenue|valuation" . || true
grep -RInE --exclude=SANITIZATION.md "/Users/|/Desktop|\\.cache|\\.config|private workspace" . || true
```

Results:

- Credentials scan: expected `.gitignore` hits for `.env` and `.env.*`; no credential value found.
- Internal code-name scan: no private code names found.
- Customer-identifying scan: only generic template language such as `real client`; no actual customer identity found.
- Local path scan: only generic scan examples; no machine-specific path found.

Known retained items:

- Product names such as Claude Code and Codex are used only for comparison.
- The repo name uses Dayan as a public project identity.

## Release Rule

If a scan finds credentials, private paths, customer-identifying facts, or unreleased internal strategy, stop the release and remove or rewrite the content before publishing.
