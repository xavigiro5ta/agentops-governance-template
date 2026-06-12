---
document_id: LAB-DOD-000
title: Definition of Done — Laboratorio AgentOps
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

# Definition of Done (DoD)

> Criterios de "terminado" por tipo de artefacto. Un artefacto **no está hecho**
> hasta cumplir su checklist completo. Fuente de reglas: `LAB-SRC-000`.

## 1. Documento controlado
- [ ] Front matter con los 15 campos y tokens canónicos (`LAB-VOCAB-000`).
- [ ] `document_id` único (`check_duplicate_ids.py`).
- [ ] `canon_status: NOT_CANON` y todas las autorizaciones en `false`.
- [ ] Solo datos demo (`check_forbidden_real_data.py`).
- [ ] Registrado en `LAB-IDX-000` y con entrada en `LAB-LOG-001`.

## 2. Skill (`.agents/skills/<nombre>/SKILL.md`)
- [ ] Propósito **estrecho** y un solo objetivo claro.
- [ ] Trigger explícito.
- [ ] Lista de **acciones prohibidas**.
- [ ] **Salida esperada** definida.
- [ ] No autoriza integración ni toca el proyecto principal.

## 3. Script (`scripts/*.py`)
- [ ] Hace una sola comprobación determinista (o orquesta las demás).
- [ ] Solo lectura sobre el repo (no modifica documentos).
- [ ] Código de retorno 0 = PASS, 1 = FAIL.
- [ ] Sin dependencias externas obligatorias.
- [ ] Probado con un caso PASS y un caso FAIL.

## 4. Test (caso de comportamiento)
- [ ] `ID` único (BC-xx).
- [ ] Prompt y **comportamiento esperado** explícitos.
- [ ] El esperado describe una **negativa** cuando la acción está prohibida.
- [ ] Resultado registrable (PENDIENTE → PASS/FAIL) con evidencia.

## 5. Reporte (`docs/02_REPORTES/`)
- [ ] Basado en `LAB-REP-000` (plantilla).
- [ ] Hallazgos con severidad y evidencia (ruta).
- [ ] Conclusión sin autorizar implementación.
- [ ] Nota de límite: `integration_authorized: false`.

## 6. Resultado de validación (`docs/03_RESULTADOS_VALIDACION/`)
- [ ] Basado en `LAB-VAL-000` (plantilla).
- [ ] PASS/FAIL por check y veredicto global.
- [ ] Comando y fecha de ejecución.
- [ ] Nota: validación verde **no** autoriza integración.

## 7. Pull Request
- [ ] Solo artefactos LAB-ONLY; sin tocar Next.js ni `package.json`.
- [ ] `run_all_checks.py` en PASS.
- [ ] Índice y bitácora actualizados.
- [ ] Descripción con alcance, validaciones y límites.
- [ ] **No** mergeado automáticamente; espera revisión humana (G3).
- [ ] Incluye la frase: "Integración al proyecto principal: NO autorizada".

## 8. Regla transversal
> Si cualquier casilla no se cumple, el artefacto está **EN PROGRESO**, no "hecho".
> La trazabilidad prevalece sobre la rapidez.
