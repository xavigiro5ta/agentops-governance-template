---
document_id: LAB-IDX-000
title: Índice Maestro de Documentos Controlados
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

# Índice Maestro de Documentos Controlados

> Mapa único de los artefactos de gobierno de esta plantilla. Cada documento tiene
> un `document_id` único y la metadata mínima de 15 campos. Fuente de reglas:
> `LAB-SRC-000`. Mantener este índice al día cada vez que se añade o retira un documento.

## Control documental (`docs/00_CONTROL_DOCUMENTAL/`)

| document_id | Documento | Propósito |
| --- | --- | --- |
| `LAB-SRC-000` | Fuente Única de Control | Autoridad de gobierno; gana ante conflicto |
| `LAB-MODEL-000` | Modelo Maestro AgentOps | Modelo conceptual del método |
| `LAB-ROLES-000` | Matriz de Roles de Agentes | Quién hace qué y con qué límites |
| `LAB-DOD-000` | Definition of Done | Cuándo un documento está terminado |
| `LAB-GATES-000` | Matriz de Gates | Puertas de autorización humana |
| `LAB-VOCAB-000` | Vocabulario Controlado | Términos, namespaces y estados válidos |
| `LAB-REQ-000` | Necesidades Funcionales | Qué se espera del método |
| `PROJECT-IDENTITY-001` | Baseline de Identidad | Plantilla de identidad del proyecto |
| `LAB-IDX-000` | Índice Maestro | Este documento |
| `LAB-LOG-001` | Bitácora | Registro append-only de decisiones |

## Espina del método (`docs/lab-agentops/pr2-method-governance/`)

| document_id | Documento | Propósito |
| --- | --- | --- |
| `LAB-METHGOV-000` | Gobierno del Método | Cómo se gobierna el propio método |
| `LAB-METHOD-000` | Control de Método | Reglas operativas del método |
| `LAB-ROUTER-000` | Router de Método | Enrutado de decisiones a la regla correcta |
| `LAB-STAGE-000` | Control de Etapas | Control de avance por capas |
| `LAB-ALERTS-000` | Alertas | Señales y banderas de riesgo |
| `LAB-METHGOV-CHK-001` | Checklist de Auditoría | Verificación del método |

## Fixtures y plantillas

| document_id | Documento | Propósito |
| --- | --- | --- |
| `LAB-FIX-001` | Fixtures de Datos Demo | Entidades ficticias para pruebas |
| `LAB-REP-000` | Plantilla de Reporte | Formato base de reportes |
| `LAB-VAL-000` | Plantilla de Resultado de Validación | Formato base de validación |

## Validadores mecánicos (`scripts/`)

| Script | Verifica |
| --- | --- |
| `run_all_checks.py` | Orquesta todos los validadores |
| `check_metadata.py` | 15 campos de metadata presentes y no vacíos |
| `check_duplicate_ids.py` | `document_id` únicos |
| `check_status_values.py` | Vocabulario y autorizaciones (=false) |
| `check_forbidden_real_data.py` | Sin datos reales (solo demo) |
| `check_forbidden_secrets.py` | Sin secretos/tokens |
