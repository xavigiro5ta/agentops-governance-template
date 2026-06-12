---
document_id: LAB-REQ-000
title: Necesidades Funcionales Esperadas — Laboratorio AgentOps
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

# Necesidades Funcionales Esperadas

> Cataloga **qué debe poder hacer** el laboratorio como sistema de gobierno, y
> cómo se verifica cada necesidad. No describe el software real. Fuente de reglas:
> `LAB-SRC-000`.

## 1. Matriz de necesidades

| ID | Necesidad funcional | Cómo se satisface hoy | Verificación | Estado |
| --- | --- | --- | --- | --- |
| REQ-01 | **Fuente única de verdad** | `LAB-SRC-000` concentra reglas y vocabulario | Lectura + `source-consolidation` | CUMPLE |
| REQ-02 | **No duplicidad** de identificadores | `document_id` único por documento | `check_duplicate_ids.py` | CUMPLE |
| REQ-03 | **Datos ficticios** únicamente | Fixtures demo y placeholders | `check_forbidden_real_data.py` | CUMPLE |
| REQ-04 | **Gates** de autorización explícitos | `LAB-GATES-000` define cada gate | Revisión humana + evidencia | CUMPLE |
| REQ-05 | **Bitácora** append-only | `LAB-LOG-001` registra cambios | Auditoría manual | CUMPLE |
| REQ-06 | **Índice** maestro al día | `LAB-IDX-000` mapea artefactos | `documentary-audit` | CUMPLE |
| REQ-07 | **Skills** estrechas y auditables | 6 skills en `.agents/skills/` | Revisión de SKILL.md | CUMPLE |
| REQ-08 | **Validadores** mecánicos | 5 scripts en `scripts/` | `run_all_checks.py` | CUMPLE |
| REQ-09 | **Pruebas de comportamiento** de agentes | `tests/agent-behaviour-cases.md` (BC-001..020) | `agent-behaviour-test` → `LAB-VAL-002` | CUMPLE_TABLETOP / ADVERSARIAL_PENDIENTE |
| REQ-10 | **Protección del proyecto principal** | LAB-ONLY; no se toca Next.js | `git diff` + revisión | CUMPLE |
| REQ-11 | **Preparación de integración futura** | Estrategias en papel + `LAB-GATES-000` G4 | Revisión humana | DISEÑO (no ejecutado) |
| REQ-12 | **Vocabulario normalizado** | `LAB-VOCAB-000` + `check_status_values.py` | Validador | CUMPLE |
| REQ-13 | **Roles de agentes** definidos | `LAB-ROLES-000` | Revisión humana | CUMPLE |
| REQ-14 | **Definition of Done** explícita | `LAB-DOD-000` | Checklist por artefacto | CUMPLE |

## 2. No-objetivos (explícitos)

- No construir software productivo.
- No crear base de datos, migraciones ni esquemas.
- No conectar APIs ni activar automatizaciones.
- No declarar canon ni autorizar integración.

## 3. Trazabilidad

Cada necesidad se enlaza con su mecanismo de verificación. Una necesidad solo se
marca `CUMPLE` cuando existe evidencia (validador en verde, documento o registro).
La integración futura (REQ-11) permanece en **diseño**: su ejecución requiere
gate G4 (ver `LAB-GATES-000`), hoy **no autorizado**.

REQ-09 queda en `CUMPLE_TABLETOP / ADVERSARIAL_PENDIENTE`: los casos BC-001..020
pasaron en modalidad tabletop (cobertura de reglas, `LAB-VAL-002`), pero falta una
prueba adversarial con un agente externo en vivo (ver `LAB-AUDIT-001` y PR #2
recomendado).
