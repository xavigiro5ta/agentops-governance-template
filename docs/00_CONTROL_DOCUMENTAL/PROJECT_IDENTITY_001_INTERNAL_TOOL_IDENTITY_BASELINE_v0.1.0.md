---
document_id: PROJECT-IDENTITY-001
title: Baseline de Identidad del Proyecto (plantilla)
version: 0.1.0
status: DRAFT
canon_status: NOT_CANON
classification: LAB_INTERNAL
created_by: Maintainer Demo
requested_by: Usuario Demo
date: 2026-06-12
data_policy: FICTITIOUS_ONLY
implementation_authorized: false
code_authorized: false
database_authorized: false
automation_authorized: false
integration_authorized: false
---

# Baseline de Identidad del Proyecto

> Plantilla. Define aquí, mediante **gate humano explícito**, la identidad del
> proyecto que vas a gobernar con este método. Mientras no exista ese gate, todos
> los campos quedan como `[PENDIENTE_DE_GATE]` y `canon_status` permanece
> `NOT_CANON`. Fuente de reglas: `LAB-SRC-000`.

## 1. Para qué sirve este documento

Fija la **identidad mínima** del proyecto (qué es, qué dominio cubre, cómo se
nombra) para que todos los agentes y colaboradores partan de la misma base y no
inventen alcance. Es el primer documento que un adoptante debe completar.

## 2. Campos de identidad (completar por gate)

| Campo | Valor | Quién decide |
| --- | --- | --- |
| Nombre del proyecto | `[PENDIENTE_DE_GATE]` | Dirección humana |
| Acrónimo / código corto | `[PENDIENTE_DE_GATE]` | Dirección humana |
| Naturaleza | Herramienta interna / método de gobierno documental | Dirección humana |
| Dominio de especialización | `[DEFINIR_DOMINIO]` (ej.: operaciones de un sector) | Dirección humana |
| Audiencia | `[DEFINIR_AUDIENCIA]` | Dirección humana |
| Estado de construcción | Solo gobierno documental — **sin software productivo** | `LAB-SRC-000` |

## 3. Lo que este proyecto **no es** (en fase LAB)

- **No** es un producto terminado ni en construcción de código.
- **No** declara canon: `canon_status` siempre `NOT_CANON` hasta gate humano.
- **No** activa implementación, base de datos, APIs ni automatizaciones
  (todas las banderas de autorización en `false`).
- **No** usa datos reales: política `FICTITIOUS_ONLY` (entidades Demo).

## 4. Cómo personalizar

1. Abre un gate humano (registra la decisión en `LAB-LOG-001`).
2. Reemplaza cada `[PENDIENTE_DE_GATE]` / `[DEFINIR_*]` con tu valor real de proyecto.
3. Mantén las banderas de autorización en `false` mientras no construyas software real.
4. Ejecuta `python3 scripts/run_all_checks.py` y confirma 5/5 PASS.

> **Recordatorio:** una validación verde **no** autoriza construir producto. La
> integración a un proyecto real requiere revisión humana explícita.
