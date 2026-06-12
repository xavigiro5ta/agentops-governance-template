---
document_id: LAB-FIX-001
title: Fixtures de Datos Demo
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

# Fixtures de Datos Demo

> Datos **exclusivamente ficticios** para alimentar pruebas de gobierno.
> Prohibido sustituir por datos reales. Fuente de reglas: `LAB-SRC-000`.

## 1. Entidades demo

| Entidad | Valor demo | Identificador |
| --- | --- | --- |
| Empresa | Empresa Demo | `EMP-DEMO-001` |
| Unidad | Unidad Operativa Demo | `UNI-DEMO-001` |
| Usuario | Usuario Demo | `USR-DEMO-001` |
| Proveedor | Proveedor Demo | `PRV-DEMO-001` |
| Documento | Documento Demo | `DOC-DEMO-001` |

## 2. Contactos placeholder (no reales)

| Campo | Valor demo |
| --- | --- |
| Correo | `usuario.demo@example.com` |
| Teléfono | `+00 000 000 000` (placeholder no asignable) |
| Dominio | `demo.local` |

## 3. Ejemplo de documento demo de entrada (intake)

```
título: Documento Demo de Procedimiento
entidad: Empresa Demo
unidad: Unidad Operativa Demo
autor: Usuario Demo
contenido: Texto de relleno ficticio para probar el flujo de ingesta.
```

## 4. Reglas de uso

- Estos valores son los **únicos** admitidos en ejemplos y pruebas.
- Cualquier valor que parezca real (correo, teléfono, nombre propio) debe ser
  rechazado por `scripts/check_forbidden_real_data.py`.
- No derivar de estos fixtures ninguna base de datos, migración ni integración.
