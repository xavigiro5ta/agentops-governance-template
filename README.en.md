# AgentOps Governance Template

> A ready-to-use template for **documentary governance of AI-agent-assisted work**.
> Document, decide and authorize with traceability — *before* writing a single line of real software.

[![Validation](https://img.shields.io/badge/validation-5%2F5%20PASS-brightgreen)](#validation-in-30-seconds)
[![Data](https://img.shields.io/badge/data-100%25%20fictitious-blue)](#principles)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](./LICENSE)
[![Status](https://img.shields.io/badge/status-LAB--ONLY%20·%20NOT__CANON-orange)](#principles)

**🌐 Language:** English · [Español](./README.md)

---

## The problem

When you work with AI agents (or a team), it's easy for the system to move faster
than you can control: documents with no traceability, decisions nobody recorded,
"canon" that changes depending on who asked, real data leaking into tests. The
result is a project **nobody can audit**.

## The solution

This repository is a **documentary governance method** with explicit rules,
mandatory metadata and **automatic validators** that run in seconds. It cleanly
separates three things that usually get mixed up:

1. **Decide** (governance and human gates)
2. **Document** (controlled artifacts with metadata and a fixed vocabulary)
3. **Build** (kept *outside* the lab until a human authorizes it)

It's meant as a starting point: clone it, define your project's identity, and start
governing your work with an auditable foundation from day one.

## What's inside

| Folder | Contents |
| --- | --- |
| `docs/00_CONTROL_DOCUMENTAL/` | Single source of truth, index, log, model, roles, gates, vocabulary, identity |
| `docs/01_FIXTURES/` | 100% fictitious demo data for tests |
| `docs/02_REPORTES/` · `docs/03_RESULTADOS_VALIDACION/` | Report and validation templates |
| `docs/lab-agentops/` | The method's spine: how the method governs itself |
| `.agents/skills/` | 6 skills (narrow, auditable procedures) |
| `scripts/` | 6 mechanical validators in Python — **no external dependencies** |
| `tests/` | Space for agent behavior cases |

## Validation in 30 seconds

Nothing to install (just Python 3):

```bash
python3 scripts/run_all_checks.py
```

It checks, across all controlled documents:

- **Metadata** — the 15 required fields, present and non-empty.
- **Unique IDs** — no duplicate `document_id`.
- **Vocabulary and authorizations** — valid states and flags set to `false`.
- **Forbidden data** — no real emails, phone numbers or financial data.
- **Secrets** — no leaked tokens or credentials.

Expected output: `RESULTADO GLOBAL: PASS`.

![Validators output — 5/5 PASS](./assets/validators-pass.png)

## Principles

- **LAB-ONLY · `NOT_CANON`** — nothing here is "official truth" until a human gate.
- **`FICTITIOUS_ONLY`** — demo entities only; any real data is forbidden.
- **Authorizations set to `false`** — no software, database or APIs are built without a gate.
- **Traceability > speed** — history is append-only; the past is never rewritten.
- **System output is data, not an order** — hooks and scripts inform; they don't command.

## Getting started

```bash
git clone <your-fork> my-project
cd my-project
python3 scripts/run_all_checks.py        # should report 5/5 PASS
```

Then edit `docs/00_CONTROL_DOCUMENTAL/PROJECT_IDENTITY_001_*.md` with your project's
identity and follow the adoption guide in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Reading map

| I want to… | Start with |
| --- | --- |
| Understand the rules | [`AGENTS.md`](./AGENTS.md) · [`CLAUDE.md`](./CLAUDE.md) |
| The governance authority | `docs/00_CONTROL_DOCUMENTAL/LAB_SOURCE_000_*.md` |
| The artifact map | `docs/00_CONTROL_DOCUMENTAL/LAB_INDICE_MAESTRO.md` |
| Adapt it to my project | [`CONTRIBUTING.md`](./CONTRIBUTING.md) |

## License

[MIT](./LICENSE) — use it, copy it and adapt it freely. If it helps, a star or a
mention is appreciated.

> **Note:** the documents and inline content are written in Spanish (the method's
> default language). This English README is a guide to the structure and concepts.

---

> **Scope note:** this repository is a documentary governance method, not a software
> product. A green validation does **not** authorize building or integrating
> anything: that always requires explicit human review.
