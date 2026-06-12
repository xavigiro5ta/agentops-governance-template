---
name: documentary-audit
description: Audita metadata, consistencia y vocabulario de los documentos controlados del laboratorio AgentOps. Úsala antes de aprobar cualquier documento o tras editar docs/.
---

# Skill: documentary-audit

## Propósito (estrecho)
Verificar que los documentos controlados del laboratorio cumplen el contrato de
metadata, el vocabulario controlado y la política de datos definidos en
`docs/00_CONTROL_DOCUMENTAL/LAB_SOURCE_000_FUENTE_UNICA_CONTROL_v0.1.0.md` (`LAB-SRC-000`).

## Trigger
- El usuario pide "auditar documentación" / "revisar metadata".
- Antes de mover un documento a `IN_REVIEW` o `APPROVED_LAB`.
- Después de crear o editar archivos en `docs/`.

## Acciones permitidas
1. Leer documentos en `docs/`.
2. Ejecutar `python3 scripts/check_metadata.py`, `check_duplicate_ids.py`,
   `check_status_values.py`.
3. Listar hallazgos con ruta y campo afectado.
4. Proponer correcciones (sin aplicarlas si tocan canon o autorización).

## Acciones prohibidas
- Declarar canon o cambiar `canon_status` a algo distinto de `NOT_CANON`.
- Cambiar cualquier bandera de autorización a `true`.
- Modificar código Next.js o tocar el proyecto principal.
- Inventar datos reales o sustituir fixtures demo.

## Salida esperada
- Un reporte breve (apto para `docs/02_REPORTES/`) con: lista de hallazgos,
  severidad (info/warn/error) y veredicto PASS/FAIL.
- Si hay error, indicar exactamente qué campo/documento corregir.
