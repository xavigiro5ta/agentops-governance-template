---
document_id: LAB-ROLES-000
title: Matriz de Roles de Agentes — Laboratorio AgentOps
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

# Matriz de Roles de Agentes

> Define quién hace qué en el laboratorio y, sobre todo, **qué no puede autorizar
> cada rol**. Solo la persona (Usuario/Dirección) autoriza avances de gate.
> Fuente de reglas: `LAB-SRC-000`. Ver gates en `LAB-GATES-000`.

## 1. Matriz de roles

| Rol | Responsabilidad principal | Puede | NO puede | Gate que opera |
| --- | --- | --- | --- | --- |
| **Usuario / Dirección** | Autoridad humana del laboratorio | Aprobar gates, fijar objetivos, autorizar (o no) integración futura | Delegar la decisión de integración en un agente | G3, G4 |
| **ChatGPT** | Diseño conceptual y estrategia documental | Proponer modelos, redactar borradores, revisar coherencia | Ejecutar comandos en el repo; declarar canon | G0–G2 (asesoría) |
| **Claude (Claude Code)** | Operación documental en el repo | Crear/editar documentos, skills y scripts; correr validadores (solo lectura) | Tocar Next.js; cambiar autorizaciones a `true`; mergear | G0–G2 (ejecución) |
| **Codex** | Generación/asistencia de código (cuando se autorice) | Proponer código **en diseño** dentro del laboratorio | Escribir código productivo sin gate; crear DB/migraciones | Ninguno activo (bloqueado por `code_authorized: false`) |
| **Scripts (`scripts/`)** | Validación mecánica determinista | Verificar metadata, ids, estados y datos prohibidos | Interpretar negocio; modificar documentos | G1 (evidencia) |
| **GitHub** | Alojamiento, PRs y trazabilidad | Versionar, alojar PR #1, registrar revisión | Mergear automáticamente; ejecutar CI (no habilitada) | G3 (soporte) |

## 2. Reglas de separación de poderes

- **Ningún agente automático** (ChatGPT, Claude, Codex, scripts, GitHub) puede
  cruzar G3 ni G4: eso es exclusivo de Usuario/Dirección.
- **Claude** ejecuta en el repo pero **no** decide integración ni toca el proyecto
  principal.
- **Codex** permanece inactivo para código productivo mientras `code_authorized`
  sea `false`.
- **GitHub** no mergea ni corre CI sin autorización humana explícita.

## 3. Flujo de colaboración típico

1. Usuario/Dirección fija el objetivo.
2. ChatGPT propone diseño/estrategia.
3. Claude materializa documentos/skills/scripts en el repo.
4. Scripts validan (evidencia mecánica).
5. Claude corre `agent-behaviour-test`.
6. Usuario/Dirección revisa en GitHub (PR) y, si procede, marca `APPROVED_LAB` (G3).
7. Integración (G4): **no** se ejecuta; queda para decisión humana separada.

> **Integración al proyecto principal: NO autorizada** por ningún rol en el estado actual.
