---
document_id: LAB-MODEL-000
title: Modelo Maestro AgentOps — Laboratorio
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

# Modelo Maestro AgentOps

> Describe **cómo se organiza** el sistema de gobierno que el laboratorio prueba.
> No describe el software real. Fuente de reglas: `LAB-SRC-000`.

## 1. Capas del modelo

```
            ┌─────────────────────────────────────────┐
            │  LAB-SRC-000  Fuente Única de Control     │  ← reglas y vocabularios
            └───────────────────┬─────────────────────┘
                                │
            ┌───────────────────▼─────────────────────┐
            │  LAB-MODEL-000  Modelo Maestro (este)    │  ← arquitectura del gobierno
            └───────────────────┬─────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                        ▼
  AGENTS.md / CLAUDE.md     Skills (.agents)        Validadores (scripts)
  (instrucción operativa)   (procedimientos)        (control mecánico)
        │                       │                        │
        └───────────────────────┼───────────────────────┘
                                ▼
                 Fixtures · Reportes · Resultados · Tests
```

## 2. Componentes y responsabilidades

| Componente | Responsabilidad | No hace |
| --- | --- | --- |
| Fuente única (`LAB-SRC-000`) | Reglas, vocabulario, límites de autorización. | No ejecuta nada. |
| Modelo maestro (`LAB-MODEL-000`) | Arquitectura del gobierno. | No define el producto. |
| `AGENTS.md` | Instrucciones para agentes genéricos. | No declara canon. |
| `CLAUDE.md` | Instrucciones específicas para Claude. | No autoriza implementación. |
| Skills | Procedimientos estrechos y auditables. | No tocan producción. |
| Scripts | Validación mecánica (metadata, ids, estados, datos). | No interpretan negocio. |
| Fixtures | Datos demo ficticios de entrada. | No contienen datos reales. |
| Tests | Casos de comportamiento esperado de agentes. | No ejecutan software real. |

## 3. Flujo de trabajo del laboratorio

1. **Intake** — `knowledge-base-intake` normaliza conocimiento **demo** a documentos controlados.
2. **Auditoría** — `documentary-audit` verifica metadata y consistencia.
3. **Consolidación** — `source-consolidation` reconcilia hacia `LAB-SRC-000`.
4. **Estrategia** — `implementation-strategy` diseña planes (sin ejecutarlos).
5. **Pruebas** — `agent-behaviour-test` corre los casos de `tests/`.
6. **Validación** — `validation-report` ejecuta `scripts/run_all_checks.py` y publica
   un resultado en `docs/03_RESULTADOS_VALIDACION/`.

## 4. Estados de un documento (ciclo de vida)

```
DRAFT → IN_REVIEW → APPROVED_LAB
                      │
                      ├──→ DEPRECATED → ARCHIVED
```

`APPROVED_LAB` **nunca** implica apto para el proyecto principal.

## 5. Invariantes del modelo (deben cumplirse siempre)

- `canon_status` = `NOT_CANON` en todo artefacto.
- Todas las banderas de autorización en `false`.
- `data_policy` = `FICTITIOUS_ONLY`.
- Cada documento controlado tiene `document_id` único.
- La trazabilidad prevalece sobre la rapidez.

## 6. Criterio de promoción (fuera de alcance de este laboratorio)

La promoción de cualquier patrón al proyecto principal exige:
1. Validación de laboratorio completa (todos los checks en verde).
2. Revisión humana documentada.
3. Decisión explícita y separada, **fuera** de este laboratorio.

> **Integración al proyecto principal: NO autorizada** en el estado actual.
