---
name: source-consolidation
description: Reconcilia reglas dispersas hacia la fuente única (LAB-SRC-000), eliminando contradicciones. Úsala cuando dos documentos parezcan contradecirse.
---

# Skill: source-consolidation

## Propósito (estrecho)
Mantener una **única fuente de verdad** de gobierno en `LAB-SRC-000`,
detectando y resolviendo contradicciones entre documentos del laboratorio.

## Trigger
- Dos documentos dan reglas distintas para lo mismo.
- Tras varias ingestas (`knowledge-base-intake`) que pudieron divergir.
- Antes de una validación global.

## Acciones permitidas
1. Comparar reglas entre `LAB-SRC-000`, `AGENTS.md`, `CLAUDE.md` y skills.
2. Proponer un texto consolidado para `LAB-SRC-000` (con incremento de `version`).
3. Marcar documentos superados como `DEPRECATED` y registrarlo en `LAB-LOG-001`.

## Acciones prohibidas
- Crear una segunda "fuente única" paralela.
- Declarar canon para el proyecto principal.
- Cambiar autorizaciones a `true` o relajar la política de datos.
- Borrar historia: la bitácora es append-only.

## Salida esperada
- `LAB-SRC-000` actualizado y coherente, con `version` incrementada.
- Lista de contradicciones resueltas y documentos marcados `DEPRECATED`.
- Entrada en `LAB-LOG-001` documentando la consolidación.
