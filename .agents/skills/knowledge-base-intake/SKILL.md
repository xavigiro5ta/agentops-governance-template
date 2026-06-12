---
name: knowledge-base-intake
description: Normaliza conocimiento de entrada (solo datos demo ficticios) a documentos controlados con metadata mínima. Úsala para incorporar material nuevo al laboratorio.
---

# Skill: knowledge-base-intake

## Propósito (estrecho)
Convertir material de entrada **ficticio** en documentos controlados que cumplan
la metadata mínima y la política de datos de `LAB-SRC-000`.

## Trigger
- El usuario aporta texto/notas demo para incorporar al laboratorio.
- Se necesita un nuevo `LAB-FIX-<NNN>` o documento base demo.

## Acciones permitidas
1. Leer `docs/01_FIXTURES/FIXTURES_DATOS_DEMO.md` para reutilizar entidades demo.
2. Crear el nuevo documento con front matter completo (los 15 campos).
3. Asignar un `document_id` único según la convención `LAB-<TIPO>-<NNN>`.
4. Registrar el alta en `LAB-IDX-000` (índice) y `LAB-LOG-001` (bitácora).

## Acciones prohibidas
- Introducir datos reales (nombres, correos, teléfonos, finanzas). Solo demo.
- Crear base de datos, migraciones o esquemas productivos.
- Conectar APIs o activar automatizaciones.
- Marcar `canon_status` distinto de `NOT_CANON` o autorizaciones en `true`.

## Salida esperada
- Un documento nuevo en `docs/` con metadata válida (pasa `check_metadata.py`).
- Índice y bitácora actualizados.
- Confirmación de que todos los datos son demo.
