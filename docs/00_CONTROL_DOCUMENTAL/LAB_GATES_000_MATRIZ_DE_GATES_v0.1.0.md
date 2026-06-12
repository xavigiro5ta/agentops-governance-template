---
document_id: LAB-GATES-000
title: Matriz de Gates — Laboratorio AgentOps
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

# Matriz de Gates

> Un **gate** es un punto de control que decide si un artefacto avanza. Cada gate
> declara qué autoriza, qué **no** autoriza y qué evidencia exige. Ningún gate de
> este laboratorio autoriza tocar el proyecto principal. Fuente de reglas:
> `LAB-SRC-000`.

## 1. Principios de los gates

- Un gate **no se aprueba solo**: requiere evidencia registrada.
- Pasar un gate **no** cambia ninguna bandera de autorización a `true`.
- La trazabilidad de la evidencia prevalece sobre la rapidez.

## 2. Matriz

| Gate | Nombre | Autoriza | NO autoriza | Evidencia exigida | Responsable |
| --- | --- | --- | --- | --- | --- |
| **G0** | Intake | Incorporar material **demo** como documento controlado | Usar datos reales; crear software | Documento con metadata válida + entrada en `LAB-LOG-001` | `knowledge-base-intake` |
| **G1** | Validación documental | Marcar documento `IN_REVIEW` | Marcar `APPROVED_LAB`; declarar canon | `run_all_checks.py` en PASS + reporte `documentary-audit` | `documentary-audit` |
| **G2** | Prueba de comportamiento | Confirmar que el agente respeta límites | Ejecutar acciones prohibidas reales | Resultados `agent-behaviour-test` (BC-xx PASS) | `agent-behaviour-test` |
| **G3** | Revisión humana | Marcar documento `APPROVED_LAB` (solo laboratorio) | Integración a proyecto principal | Aprobación humana registrada en PR + bitácora | Usuario/Dirección |
| **G4** | Integración futura | — (NO autorizado en estado actual) | Todo: no se ejecuta | Decisión humana **separada y explícita**, fuera del laboratorio | Usuario/Dirección |

## 3. Detalle por gate

### G0 — Intake
- **Entrada:** material ficticio (notas demo).
- **Salida:** documento controlado en `docs/` con los 15 campos de metadata.
- **Bloqueo:** si aparece cualquier dato real, el gate falla (ver `check_forbidden_real_data.py`).

### G1 — Validación documental
- **Condición de paso:** los 4 validadores en PASS y sin contradicciones de vocabulario.
- **No autoriza** `APPROVED_LAB` por sí solo: eso ocurre en G3.

### G2 — Prueba de comportamiento
- **Condición de paso:** casos BC-xx relevantes en PASS, demostrando que el agente
  **se niega** ante acciones prohibidas (datos reales, integración, canon, etc.).

### G3 — Revisión humana
- **Condición de paso:** una persona revisa y aprueba explícitamente en el PR.
- **Máximo alcance:** `APPROVED_LAB`. Nunca "apto para producción".

### G4 — Integración futura (cerrado)
- **Estado:** `integration_authorized: false`. **No** se cruza en este laboratorio.
- **Requisito para abrirlo en el futuro:** G1+G2+G3 completos y una decisión humana
  documentada **fuera** de este laboratorio.

## 4. Recordatorio

> **Integración al proyecto principal: NO autorizada.** Ningún gate de esta matriz
> la habilita en el estado actual.
