---
document_id: LAB-VAL-000
title: Plantilla de Resultado de Validación
version: 0.1.0
status: DRAFT
canon_status: NOT_CANON
classification: LAB_INTERNAL
created_by: Agente AgentOps
requested_by: Usuario Demo
date: 2026-06-08
data_policy: FICTITIOUS_ONLY
implementation_authorized: false
code_authorized: false
database_authorized: false
automation_authorized: false
integration_authorized: false
---

# Plantilla de Resultado de Validación

> `scripts/run_all_checks.py` puede generar resultados con prefijo `LAB-VAL-<NNN>`.
> Fuente de reglas: `LAB-SRC-000`.

## 1. Ejecución
- Fecha/hora:
- Comando: `python3 scripts/run_all_checks.py`
- Entorno: laboratorio (LAB-ONLY)

## 2. Resumen por check
| Check | Resultado (PASS/FAIL) | Hallazgos |
| --- | --- | --- |
| `check_metadata.py` | | |
| `check_duplicate_ids.py` | | |
| `check_status_values.py` | | |
| `check_forbidden_real_data.py` | | |

## 3. Estado global
- Resultado global: PASS / FAIL
- Detalle:

## 4. Límites
- Validación verde **no** autoriza integración. `integration_authorized: false`.
