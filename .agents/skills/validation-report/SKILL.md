---
name: validation-report
description: Ejecuta los validadores mecánicos (scripts/) y publica un resultado de validación en docs/03_RESULTADOS_VALIDACION/. Úsala como paso final antes de revisión humana.
---

# Skill: validation-report

## Propósito (estrecho)
Correr la validación mecánica completa del laboratorio y producir un resultado
trazable, sin emitir juicio de "apto para producción".

## Trigger
- El usuario pide "validar el laboratorio" o "correr todos los checks".
- Antes de solicitar revisión humana o de abrir/actualizar un PR.

## Acciones permitidas
1. Ejecutar `python3 scripts/run_all_checks.py`.
2. Capturar la salida y el código de retorno.
3. Crear un documento `LAB-VAL-<NNN>` en `docs/03_RESULTADOS_VALIDACION/` a partir
   de `PLANTILLA_RESULTADO_VALIDACION.md`.
4. Registrar la ejecución en `LAB-LOG-001`.

## Acciones prohibidas
- Modificar los checks para forzar un PASS.
- Cambiar autorizaciones a `true` ni declarar canon.
- Afirmar que el resultado habilita integración al proyecto principal.

## Salida esperada
- Resultado `LAB-VAL-<NNN>` con PASS/FAIL por check y veredicto global.
- Nota explícita: validación verde **no** autoriza integración; requiere revisión humana.
