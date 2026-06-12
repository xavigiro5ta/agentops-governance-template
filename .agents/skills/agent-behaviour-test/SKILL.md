---
name: agent-behaviour-test
description: Ejecuta los casos de comportamiento de agentes definidos en tests/agent-behaviour-cases.md y registra si el agente respeta las reglas del laboratorio.
---

# Skill: agent-behaviour-test

## Propósito (estrecho)
Comprobar que un agente, al recibir solicitudes, **respeta** los límites del
laboratorio (modo LAB-ONLY, datos ficticios, sin integración) definidos en
`LAB-SRC-000` y reflejados en `AGENTS.md` / `CLAUDE.md`.

## Trigger
- El usuario pide "probar el comportamiento del agente" o "correr los casos".
- Tras cambiar `AGENTS.md`, `CLAUDE.md` o cualquier skill.

## Acciones permitidas
1. Leer `tests/agent-behaviour-cases.md`.
2. Para cada caso, comparar el comportamiento esperado vs. el observado.
3. Registrar PASS/FAIL por caso en un resultado de `docs/03_RESULTADOS_VALIDACION/`.

## Acciones prohibidas
- Ejecutar acciones reales que el caso describe como prohibidas (p. ej. crear DB).
- Usar datos reales en los casos.
- Marcar un caso PASS sin evidencia.

## Salida esperada
- Tabla de resultados (caso, esperado, observado, PASS/FAIL).
- Veredicto global y, si hay FAIL, qué regla del laboratorio se violó.
