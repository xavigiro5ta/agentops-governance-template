---
document_id: LAB-METHGOV-000
title: PR2 — Capa de Gobierno Metodológico (README)
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

# PR2 — Capa de Gobierno Metodológico (LAB-ONLY)

> Capa documental **experimental** para controlar **cómo se clasifican, validan,
> bloquean, derivan y aprueban** las tareas dentro del laboratorio AgentOps.
> No construye software. No declara canon. No toca el proyecto principal.

## 1. Qué es PR2

PR2 añade una **capa de gobierno metodológico** sobre el laboratorio creado en
PR #1 (ya mergeado). Define el "cómo se decide", no el "qué se construye". Es
puramente documental y de gobierno: `LAB-ONLY / NOT_CANON`.

## 2. Qué problema controla

Evita que el trabajo con agentes derive en riesgos metodológicos:
- que una conversación se convierta en software sin control;
- sobre-documentación o documentación insuficiente;
- construcción prematura (saltar a código/automatización sin gate);
- mezcla de idea, documentación, prototipo y software real;
- contaminación del proyecto principal;
- pérdida de trazabilidad y confusión de roles.

## 3. Documentos que contiene

| Archivo | document_id | Rol |
| --- | --- | --- |
| `README.md` | `LAB-METHGOV-000` | Índice y guía de esta capa (este documento). |
| `LAB_METHOD_CONTROL_000.md` | `LAB-METHOD-000` | Reglas de control metodológico: entradas, salidas, validación, gates, bloqueo/advertencia/aprobación. |
| `LAB_METHOD_ROUTER_000.md` | `LAB-ROUTER-000` | Clasificación de solicitudes y enrutamiento (bloquear/derivar/aclarar/aprobar LAB). |
| `LAB_STAGE_CONTROL_000.md` | `LAB-STAGE-000` | Estados de madurez y transiciones permitidas/prohibidas con gates. |
| `LAB_ALERTS_000.md` | `LAB-ALERTS-000` | Catálogo de alertas (INFO/WARNING/BLOCKER) con disparadores y acciones. |
| `PR2_AUDIT_CHECKLIST.md` | `LAB-METHGOV-CHK-001` | Checklist de auditoría del PR. |

## 4. Cómo se relacionan

```
        ┌──────────────────────────┐
        │  LAB-METHOD-000 (Control) │  ← reglas marco: qué se valida y cómo
        └────────────┬─────────────┘
                     │ usa
        ┌────────────▼─────────────┐
        │  LAB-ROUTER-000 (Router) │  ← clasifica la entrada y elige ruta + gate
        └────────────┬─────────────┘
                     │ produce piezas con estado
        ┌────────────▼─────────────┐
        │  LAB-STAGE-000 (Stages)  │  ← madurez y transiciones con gates
        └────────────┬─────────────┘
                     │ vigilado por
        ┌────────────▼─────────────┐
        │  LAB-ALERTS-000 (Alerts) │  ← dispara alertas y acciones transversales
        └──────────────────────────┘
```

El Router clasifica → Control valida con sus gates → Stage define en qué estado
queda la pieza → Alerts vigila todo el flujo. La trazabilidad entre los cuatro es
obligatoria (ver `PR2_AUDIT_CHECKLIST.md`).

## 5. Qué está permitido

- Crear/editar documentación Markdown LAB-ONLY.
- Definir checklists, tablas de estados, matrices de decisión, criterios y ejemplos ficticios.
- Definir contratos conceptuales de entrada/salida (en papel).

## 6. Qué está prohibido

- Tocar el proyecto principal, Next.js o `package.json`; modificar dependencias.
- Crear software productivo, base de datos, migraciones, APIs o integraciones externas.
- Activar CI o crear workflows de GitHub Actions; activar automatizaciones reales.
- Usar datos reales, secretos, tokens o credenciales.
- Declarar canon o convertir documentos LAB en productivos.
- Hacer merge o cerrar el PR (eso es decisión humana posterior).
- Mezclar con "Proyecto Principal Demo" ni con "DemoProducto productivo".

## 7. Cómo se audita

1. Revisar `PR2_AUDIT_CHECKLIST.md` punto por punto.
2. Confirmar en "Files changed" que solo hay Markdown bajo `docs/lab-agentops/pr2-method-governance/`.
3. Ejecutar `python3 scripts/run_all_checks.py` (debe dar PASS).
4. Verificar trazabilidad entre los cuatro documentos.

## 8. Estado documental

- `LAB-ONLY / NOT_CANON`. Todas las autorizaciones en `false`.
- Este PR **solo define el sistema**; no aprueba canon ni integra nada.

## 9. Nota de reconciliación de vocabulario

El encargo original sugería `canon_status: NO_CANON`, `status: LAB_DRAFT` y
`classification: LAB_ONLY / METHOD_GOVERNANCE`. Para mantener coherencia con la
fuente única ya mergeada (`LAB-SRC-000`) y pasar los validadores
(`scripts/`), se aplicaron los **tokens canónicos** (`LAB-VOCAB-000`):

| Solicitado | Canónico aplicado | Dónde se preserva la intención |
| --- | --- | --- |
| `canon_status: NO_CANON` | `canon_status: NOT_CANON` | equivalencia en `LAB-VOCAB-000` §2 |
| `status: LAB_DRAFT` | `status: DRAFT` | el estado de madurez `LAB_DRAFT` vive en `LAB-STAGE-000` |
| `classification: LAB_ONLY / METHOD_GOVERNANCE` | `classification: LAB_INTERNAL` + `method_classification: METHOD_GOVERNANCE` | campo extra no validado |
| `requested_by: Usuario Real / Usuario Demo` | `requested_by: Usuario Demo` | política `FICTITIOUS_ONLY` (sin nombres reales) |

## 10. Pendientes de trazabilidad (para auditoría humana)

- Registrar estos documentos en el índice global `LAB-IDX-000` y la bitácora
  `LAB-LOG-001`, y los nuevos tipos (`METHOD`, `ROUTER`, `STAGE`, `ALERTS`,
  `METHGOV`) en `LAB-SRC-000` §6, vía `source-consolidation` en un paso posterior.
  Se omitió aquí para mantener el PR #2 acotado a su carpeta.

> **Integración al proyecto principal: NO autorizada; requiere validación de
> laboratorio y revisión humana.**
