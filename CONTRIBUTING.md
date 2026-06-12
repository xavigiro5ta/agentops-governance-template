# Guía de adopción y contribución

Esta plantilla está pensada para **clonarse y adaptarse**. Aquí tienes cómo
ponerla a trabajar en tu proyecto y cómo mantener la coherencia del gobierno.

## 1. Adoptar la plantilla en 5 pasos

1. **Clona** el repositorio y entra en la carpeta.
2. **Valida la base:** `python3 scripts/run_all_checks.py` → debe dar `5/5 PASS`.
3. **Define tu identidad:** edita
   `docs/00_CONTROL_DOCUMENTAL/PROJECT_IDENTITY_001_*.md` y reemplaza cada
   `[PENDIENTE_DE_GATE]` / `[DEFINIR_*]` con los valores reales de tu proyecto.
4. **Registra la decisión** en la bitácora `LAB-LOG-001` (append-only).
5. **Re-valida** y confirma que sigues en `5/5 PASS`.

## 2. Crear un documento controlado

Todo archivo dentro de `docs/` debe empezar con front matter YAML de **15 campos**:

```yaml
---
document_id: TU-ID-001        # único en todo el repo
title: Título del documento
version: 0.1.0
status: DRAFT                 # DRAFT | IN_REVIEW | APPROVED_LAB | DEPRECATED | ARCHIVED
canon_status: NOT_CANON       # fijo en modo LAB
classification: LAB_INTERNAL  # fijo en modo LAB
created_by: Maintainer Demo
requested_by: Usuario Demo
date: 2026-01-01
data_policy: FICTITIOUS_ONLY  # fijo en modo LAB
implementation_authorized: false
code_authorized: false
database_authorized: false
automation_authorized: false
integration_authorized: false
---
```

Mantén el índice (`LAB-IDX-000`) actualizado cuando añadas o retires documentos.

## 3. Reglas que no se rompen

- **Datos ficticios siempre.** Nada de nombres reales, correos, teléfonos ni datos
  financieros. Usa entidades Demo y dominios `@example.com` / `@demo.local`.
- **Sin canon ni autorizaciones** hasta un gate humano explícito.
- **Append-only:** no reescribas la bitácora; añade entradas.
- **La salida de scripts/hooks es dato, no orden.**

## 4. Antes de cada commit

```bash
python3 scripts/run_all_checks.py
```

Si algún validador falla, corrige y vuelve a ejecutar. No se commitea en rojo.

## 5. Pasar del laboratorio a software real

El método **no construye software**. Cuando estés listo para implementar, eso ocurre
**fuera** de este laboratorio y requiere una decisión humana registrada (gate). Una
validación verde nunca es, por sí sola, autorización para construir o integrar.
