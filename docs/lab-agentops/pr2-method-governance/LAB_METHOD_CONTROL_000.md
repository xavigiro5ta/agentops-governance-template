---
document_id: LAB-METHOD-000
title: Control Metodológico — Laboratorio AgentOps
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

# Control Metodológico (LAB-METHOD-000)

> Reglas marco para controlar **cómo** se admiten, validan y resuelven las tareas
> del laboratorio. No construye software. Fuente de reglas: `LAB-SRC-000`.

## 1. Propósito

Garantizar que toda tarea pase por un control explícito que separe idea,
documentación, prototipo y software real, evitando construcción prematura y
contaminación del proyecto principal.

## 2. Alcance

- Definir entradas aceptadas y salidas permitidas del laboratorio.
- Definir reglas de validación, gates metodológicos y criterios de
  bloqueo/advertencia/aprobación.
- Aplica a documentos, checklists, matrices y estrategias **en papel**.

## 3. No alcance

- No produce código productivo, base de datos, migraciones, APIs ni automatizaciones.
- No declara canon ni autoriza integración.
- No modifica el proyecto principal, Next.js ni `package.json`.

## 4. Entradas aceptadas

| Entrada | Aceptada como |
| --- | --- |
| Idea/intención de trabajo (ficticia) | Documento `IDEA`/`DISCOVERY` |
| Problema operativo (demo) | Documento de análisis LAB |
| Solicitud de documentación LAB | Documento controlado |
| Solicitud de estrategia | Plan en papel (no ejecutable) |
| Solicitud de validación | Ejecución de `scripts/` + reporte |

**No** se aceptan como entrada válida: datos reales, credenciales, pedidos de
código productivo o de integración directa (se derivan o bloquean, ver §8).

## 5. Salidas permitidas

- Documentos Markdown LAB-ONLY con metadata canónica.
- Checklists, tablas de estados, matrices de decisión.
- Contratos conceptuales de entrada/salida.
- Reportes de validación y de comportamiento.

## 6. Reglas de validación

1. Todo documento controlado lleva los 15 campos de metadata (`LAB-SRC-000` §5).
2. `canon_status: NOT_CANON`; todas las autorizaciones en `false`.
3. Vocabulario canónico (`LAB-VOCAB-000`); si un validador rechaza un valor, **gana
   el validador**.
4. `python3 scripts/run_all_checks.py` debe dar PASS antes de proponer un PR.
5. Solo datos ficticios (`FICTITIOUS_ONLY`).

## 7. Gates metodológicos

| Gate | Pregunta de control | Pasa si |
| --- | --- | --- |
| GM-1 Formulación | ¿La tarea está bien definida y es LAB-ONLY? | Objetivo claro, sin datos reales, sin pedir producción |
| GM-2 Clasificación | ¿Se enrutó por `LAB-ROUTER-000`? | Tipo de entrada identificado + ruta asignada |
| GM-3 Validación | ¿Pasa los validadores y el vocabulario? | `run_all_checks.py` PASS |
| GM-4 Madurez | ¿El estado de `LAB-STAGE-000` es coherente? | Transición permitida y registrada |
| GM-5 Revisión humana | ¿Hay aprobación humana para avanzar? | Solo Usuario/Dirección (no agentes) |

Los gates GM-5 y la canonización son **exclusivos humanos** (ver `LAB-ROLES-000`).

## 8. Criterios de bloqueo (BLOCKER)

Se **bloquea** la tarea si pide: datos reales; crear DB/migraciones/APIs;
activar CI o automatizaciones; modificar `package.json`/Next.js/proyecto principal;
declarar canon; poner autorizaciones en `true`; integrar al proyecto principal;
tocar "Proyecto Principal Demo" o "DemoProducto productivo".

## 9. Criterios de advertencia (WARNING)

Se **advierte** (no se bloquea, pero se exige corrección) ante: solicitud ambigua;
sobre-documentación; documentación insuficiente; supuestos no validados; falta de
gate; trazabilidad rota; confusión de roles. Ver catálogo en `LAB-ALERTS-000`.

## 10. Criterios de aprobación (LAB)

Una pieza se aprueba **como laboratorio** (`LAB_ACCEPTED`, nunca canon) si:
cumple metadata y vocabulario; pasó validadores; fue enrutada y tiene estado
coherente; no disparó BLOCKERs sin resolver; y cuenta con revisión humana (GM-5).

## 11. Riesgos controlados

| Riesgo | Control aplicado |
| --- | --- |
| Conversación → software sin control | GM-1/GM-2 + bloqueo de código productivo |
| Sobre/insuficiente documentación | Alertas `OVERDOCUMENTATION_RISK`/`UNDERDOCUMENTATION_RISK` |
| Construcción prematura | Alertas `PRODUCTIVE_CODE_RISK`/`PREMATURE_AUTOMATION` + gates |
| Contaminación del proyecto principal | Bloqueo `MAIN_PROJECT_CONTAMINATION` |
| Canonización accidental | `LAB-STAGE-000`: no hay paso a CANON sin gate humano |

## 12. Respuestas a las preguntas de control

- **¿Cómo se evita que una conversación se vuelva software sin control?**
  Toda intención entra como `IDEA`/`DISCOVERY` y solo avanza por gates; el código
  productivo está bloqueado (`code_authorized: false`).
- **¿Cómo se valida que una tarea está bien formulada?** Gate GM-1: objetivo claro,
  LAB-ONLY, sin datos reales ni pedido de producción.
- **¿Cómo se detecta sobre-documentación?** Alerta `OVERDOCUMENTATION_RISK` cuando
  se duplica contenido o se documenta sin decisión asociada.
- **¿Cómo se detecta construcción prematura?** Alertas `PRODUCTIVE_CODE_RISK` /
  `PREMATURE_AUTOMATION` cuando se pide construir antes de pasar gates.
- **¿Cómo se separa idea, documentación, prototipo y software real?** Estados de
  `LAB-STAGE-000` y rutas de `LAB-ROUTER-000`.
- **¿Cómo se evita contaminación del proyecto principal?** Bloqueo explícito y
  separación estricta (`MAIN_PROJECT_CONTAMINATION`).

## 13. Relación con documentos LAB previos

- `LAB-SRC-000` (fuente única), `LAB-VOCAB-000` (vocabulario), `LAB-GATES-000`
  (gates G0–G4), `LAB-ROLES-000` (roles), `LAB-DOD-000` (Definition of Done).
- Esta capa **complementa** los gates G0–G4 con gates metodológicos GM-1..GM-5;
  no los reemplaza.

## 14. Estado documental

`LAB-ONLY / NOT_CANON`. Autorizaciones en `false`.

> **Integración al proyecto principal: NO autorizada; requiere validación de
> laboratorio y revisión humana.**
