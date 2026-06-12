---
document_id: LAB-STAGE-000
title: Control de Etapas y Madurez — Laboratorio AgentOps
project: AgentOps LAB
version: 0.1.0
status: DRAFT
canon_status: NOT_CANON
classification: LAB_INTERNAL
method_classification: METHOD_GOVERNANCE
created_by: Claude Code
requested_by: Usuario Demo
date: 2026-06-08
data_policy: FICTITIOUS_ONLY
scope: Experimental methodological governance layer (LAB-ONLY)
implementation_authorized: false
code_authorized: false
database_authorized: false
automation_authorized: false
integration_authorized: false
---

# Control de Etapas y Madurez (LAB-STAGE-000)

> Define los **estados de madurez** de una pieza y las transiciones permitidas y
> prohibidas, con gates. Fuente de reglas: `LAB-SRC-000`.

## 1. Dos planos de estado

Para evitar confusión (alerta `ROLE_CONFUSION`/`BROKEN_TRACEABILITY`) se distinguen:

- **Estado documental (front matter `status`)** — vocabulario validado por
  `scripts/`: `DRAFT`, `IN_REVIEW`, `APPROVED_LAB`, `DEPRECATED`, `ARCHIVED`
  (`LAB-VOCAB-000`).
- **Estado de madurez (este documento)** — modelo conceptual del ciclo de vida de
  una pieza del laboratorio (abajo). No se escribe en el campo `status`.

## 2. Estados de madurez (mínimos obligatorios)

| Estado | Significado | `status` documental sugerido |
| --- | --- | --- |
| `IDEA` | Intención sin definir | `DRAFT` |
| `DISCOVERY` | Exploración/recopilación demo | `DRAFT` |
| `LAB_DRAFT` | Borrador de laboratorio | `DRAFT` |
| `LAB_REVIEW` | En revisión de laboratorio | `IN_REVIEW` |
| `LAB_ACCEPTED` | Aceptado solo para laboratorio | `APPROVED_LAB` |
| `CANON_CANDIDATE` | Propuesto a canon (no aprobado) | `IN_REVIEW` |
| `CANON_APPROVED` | Canon aprobado (fuera de este PR) | (fuera de alcance) |
| `DEPRECATED` | Reemplazado | `DEPRECATED` |
| `BLOCKED` | Bloqueado por una restricción | `DRAFT`/`IN_REVIEW` |

## 3. Transiciones permitidas

```
IDEA → DISCOVERY → LAB_DRAFT → LAB_REVIEW → LAB_ACCEPTED → CANON_CANDIDATE → [GATE HUMANO] → CANON_APPROVED
                                   │              │              │
                                   └────► BLOCKED ◄┘──────────────┘   (desde cualquier estado activo)
LAB_ACCEPTED → DEPRECATED      (al ser reemplazado)
CANON_CANDIDATE → LAB_ACCEPTED (si se devuelve sin canonizar)
BLOCKED → (estado previo)      (al resolverse la causa)
```

## 4. Transiciones prohibidas

- Cualquier salto a `CANON_APPROVED` **sin** gate humano explícito posterior.
- `IDEA`/`DISCOVERY` → construcción de software (no existe esa transición aquí).
- `LAB_*` → integración al proyecto principal (G4 cerrado).
- Saltarse `LAB_REVIEW` para llegar a `LAB_ACCEPTED`.

## 5. Gates entre etapas

| Transición | Gate |
| --- | --- |
| `LAB_DRAFT → LAB_REVIEW` | GM-3 (validadores PASS) |
| `LAB_REVIEW → LAB_ACCEPTED` | GM-5 (revisión humana) |
| `LAB_ACCEPTED → CANON_CANDIDATE` | GM-5 + decisión de proponer |
| `CANON_CANDIDATE → CANON_APPROVED` | **Gate humano explícito separado** (fuera de este PR) |

## 6. Criterios para avanzar

- Metadata y vocabulario canónicos correctos.
- `run_all_checks.py` en PASS.
- Sin BLOCKERs activos (`LAB-ALERTS-000`).
- Registro de la transición en la bitácora (`LAB-LOG-001`).

## 7. Criterios para volver atrás

- Aparece un riesgo no resuelto, un supuesto inválido o trazabilidad rota.
- La revisión humana solicita correcciones.

## 8. Criterios para congelar una pieza

- Depende de una decisión externa pendiente o de un gate humano aún no disponible.
- Se marca informalmente como "congelada" manteniendo su `status` actual y se
  documenta el motivo; no avanza ni se descarta.

## 9. Criterios para descartar una pieza

- Queda obsoleta o reemplazada → `DEPRECATED` (y `ARCHIVED` si se conserva como histórico).
- Viola de raíz las restricciones LAB-ONLY y no es corregible → `BLOCKED` y baja.

## 10. Regla obligatoria

> Ningún documento LAB puede pasar a `CANON_APPROVED` sin un **gate explícito
> posterior**. Este PR **solo define el sistema**; **no aprueba canon**.

## 11. Estado documental

`LAB-ONLY / NOT_CANON`. Autorizaciones en `false`.

> **Integración al proyecto principal: NO autorizada; requiere validación de
> laboratorio y revisión humana.**
