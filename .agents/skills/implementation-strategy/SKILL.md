---
name: implementation-strategy
description: Diseña estrategias y planes de implementación (en papel) sin ejecutar código, base de datos ni integraciones. Úsala para planear, nunca para construir.
---

# Skill: implementation-strategy

## Propósito (estrecho)
Producir **planes de implementación** evaluables para el proyecto principal,
manteniéndolos como artefactos de laboratorio. Esta skill **planifica**, no construye.

## Trigger
- El usuario pide "cómo se implementaría X" o "diseña la estrategia para Y".
- Se necesita comparar enfoques antes de cualquier decisión humana.

## Acciones permitidas
1. Redactar un plan paso a paso, con trade-offs y riesgos.
2. Referenciar entidades demo de `LAB-FIX-001` para ejemplos.
3. Guardar el plan como reporte en `docs/02_REPORTES/`.

## Acciones prohibidas
- Escribir o ejecutar código productivo (`code_authorized: false`).
- Crear base de datos, migraciones o esquemas (`database_authorized: false`).
- Conectar APIs o activar automatizaciones (`integration_authorized`/`automation_authorized: false`).
- Declarar que el plan está "aprobado para producción". Solo `APPROVED_LAB` como máximo.

## Salida esperada
- Un documento de estrategia (reporte) con: objetivo, pasos, riesgos, alternativas
  y una nota explícita: la implementación **no** está autorizada y requiere
  revisión humana.
