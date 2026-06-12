---
document_id: LAB-VOCAB-000
title: Vocabulario Controlado y Equivalencias — Laboratorio AgentOps
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

# Vocabulario Controlado y Equivalencias

> Normaliza términos para que humanos y validadores hablen el mismo idioma.
> El **token canónico** es el que debe aparecer en el front matter (lo verifican
> los scripts). Las variantes en español son sinónimos válidos **solo en prosa**,
> nunca en metadata. Fuente de reglas: `LAB-SRC-000`. Extiende la tabla de tipos
> de `LAB-SRC-000` §6.

## 1. Principio

- **Metadata (front matter):** siempre token canónico en MAYÚSCULAS / `true`/`false`.
- **Prosa (cuerpo del documento):** puede usar la etiqueta humana, citando el token.
- Ante conflicto, **gana el token canónico** (el que valida `scripts/`).

## 2. Equivalencias de `canon_status`

| Token canónico (metadata) | Variante a evitar en metadata | Etiqueta humana (prosa) |
| --- | --- | --- |
| `NOT_CANON` | `NO_CANON`, `NOT-CANON`, `no_canon` | "no canónico" |

> `NOT_CANON` es el **único** valor permitido. `NO_CANON` se considera **error de
> escritura** y debe corregirse a `NOT_CANON`.

## 3. Equivalencias de `status`

| Token canónico | Variantes a evitar en metadata | Etiqueta humana |
| --- | --- | --- |
| `DRAFT` | `BORRADOR` | "borrador" |
| `IN_REVIEW` | `EN_REVISION`, `IN-REVIEW` | "en revisión" |
| `APPROVED_LAB` | `VALIDADO_LAB`, `APROBADO_LAB` | "validado en laboratorio" |
| `DEPRECATED` | `OBSOLETO`, `DEPRECADO` | "obsoleto / reemplazado" |
| `ARCHIVED` | `ARCHIVADO` | "archivado" |

## 4. Equivalencias booleanas (autorizaciones y banderas)

| Token canónico (metadata) | Variantes a evitar | Significado |
| --- | --- | --- |
| `false` | `SI`/`NO`, `SÍ`, `true` en LAB-ONLY, `0`/`1` | "no autorizado" |
| `true` | `SI`, `1` | "autorizado" (PROHIBIDO en modo LAB-ONLY) |

> En modo LAB-ONLY **todas** las banderas de autorización son `false`. El uso de
> `SI`/`NO` en metadata es inválido; usar `true`/`false` en minúscula.

## 5. Equivalencias de otros campos fijos

| Campo | Token canónico | Variante a evitar |
| --- | --- | --- |
| `classification` | `LAB_INTERNAL` | `INTERNO_LAB`, `LAB-INTERNAL` |
| `data_policy` | `FICTITIOUS_ONLY` | `SOLO_FICTICIO`, `DEMO_ONLY` |

## 6. Vocabulario de tipos de `document_id` (extiende `LAB-SRC-000` §6)

| Tipo | Uso |
| --- | --- |
| `SRC` | Fuente única de control. |
| `IDX` | Índice maestro. |
| `LOG` | Bitácora. |
| `MODEL` | Modelo maestro AgentOps. |
| `FIX` | Fixtures de prueba. |
| `REP` | Reportes. |
| `VAL` | Resultados de validación. |
| `TEST` | Casos de comportamiento de agentes. |
| `VOCAB` | Vocabulario controlado (este documento). |
| `REQ` | Necesidades funcionales esperadas. |
| `GATES` | Matriz de gates. |
| `ROLES` | Matriz de roles de agentes. |
| `DOD` | Definition of Done. |
| `AUDIT` | Auditorías de necesidades, especificaciones y continuidad. |
| `METHGOV` | Gobierno metodológico — índice/guía y checklist (PR #2). |
| `METHOD` | Control metodológico. |
| `ROUTER` | Router metodológico de clasificación/enrutamiento. |
| `STAGE` | Control de estados de madurez y transiciones. |
| `ALERTS` | Catálogo de alertas metodológicas (INFO/WARNING/BLOCKER). |
| `MAP` | Mapa ejecutivo/operativo del laboratorio (PR #4). |
| `ADV` | Validación adversarial controlada del laboratorio (PR #5). |
| `AI-TECH-INTEL` | Namespace documental de la capa `AI_TECH_INTELLIGENCE` (PR #20). |
| `AUDIT-AI-TOOLS` | Auditorías documentales de herramientas IA externas; familia `AUDIT`, capa `AI_TECH_INTELLIGENCE`; subordinado a `AI-TECH-INTEL` (PR #23). |
| `AI-TOOLS-MATRIX` | Matrices comparativas derivadas de auditorías IA; familia matriz/decisión documental, capa `AI_TECH_INTELLIGENCE`; depende de `AI-TECH-INTEL` y deriva de `AUDIT-AI-TOOLS` (PR #25). |
| `PROJECT-IDENTITY` | Documentos de identidad interna del proyecto (nombre canónico, alcance, especialización de dominio, reglas de nomenclatura). No autoriza nombre comercial definitivo sin gate humano. Incorporado por PR #31 (`PROJECT-IDENTITY-001`). |
| `PACKAGE` | Cierre documental del paquete de laboratorio independiente; capa `CONTROL_DOCUMENTAL`; solo cierre (`package_closure_only`), sin autorizar implementación/integración/proveedor/software productivo (PR #30). |
| `ARCH` | Propuestas de arquitectura técnica de producto (SaaS, AaaS, modelo de datos, MVP, reglas duras, gates); capa `PRODUCT_ARCHITECTURE`; solo documentación estratégica, sin autorizar implementación, código, base de datos, despliegue ni integración al proyecto principal. |

> Alineado: `LAB-SRC-000` §6 reconoce estos tipos y referencia este documento
> (`LAB-VOCAB-000`) como tabla extendida autoritativa del vocabulario controlado.
> Los tipos `METHGOV/METHOD/ROUTER/STAGE/ALERTS` se añadieron en PR #3 (consolidación
> del gobierno metodológico de PR #2); `MAP` en PR #4; `ADV` en GitHub PR #5;
> `AI-TECH-INTEL` en PR #20; `AUDIT-AI-TOOLS` en PR #23; `AI-TOOLS-MATRIX` en PR #25;
> `PROJECT-IDENTITY` en PR #31 (línea base de identidad del proyecto);
> `PACKAGE` en PR #30 (cierre del paquete de laboratorio);
> `ARCH` (una propuesta de arquitectura del proyecto).
> Todos son extensión LAB-ONLY. `canon_status: NOT_CANON` y `data_policy: FICTITIOUS_ONLY`
> permanecen sin cambios.

## 6.1 Vocabulario de la capa AI Tech Intelligence

| Término | Significado |
| --- | --- |
| `AI_TECH_INTELLIGENCE` | Capa documental para evaluación de herramientas IA externas. |
| `AI-TECH-INTEL` | Namespace documental de la capa. |

**Estados de clasificación de herramientas IA** (no equivalen a adopción,
implementación ni integración):

| Estado | Significado |
| --- | --- |
| `OBSERVE` | Se observa; sin estudio formal aún. |
| `STUDY` | En estudio documental con fuentes oficiales. |
| `CANDIDATE` | Candidata a evaluación más profunda. |
| `LAB_TEST_ONLY` | Solo pruebas de laboratorio aisladas (si se autoriza en PR futuro). |
| `HOLD` | En espera (madurez, costo, riesgo o timing). |
| `REJECT` | Descartada para el objetivo actual. |
| `ADOPTABLE_PENDING_GATE` | Podría adoptarse, pero requiere **gate humano explícito**. |

> Estos estados **no** significan adopción, implementación ni integración; son
> etiquetas de evaluación documental sujetas a revisión humana.

### Namespace `AUDIT-AI-TOOLS` (PR #23)

- **Familia documental:** `AUDIT`. **Capa:** `AI_TECH_INTELLIGENCE`.
- **Relación:** subordinado/metodológicamente dependiente de `AI-TECH-INTEL`; **no lo
  reemplaza**.
- **Propósito:** documentos de auditoría documental de herramientas IA externas
  (ejemplo: `AUDIT-AI-TOOLS-001`).
- **Estados permitidos:** los mismos de la tabla anterior
  (`OBSERVE`/`STUDY`/`CANDIDATE`/`LAB_TEST_ONLY`/`HOLD`/`REJECT`/`ADOPTABLE_PENDING_GATE`),
  entendidos como **estados de inteligencia documental** — **no** son adopción, **no**
  son implementación, **no** son autorización operativa.
- **Límites:** `AUDIT-AI-TOOLS` **no** autoriza implementación · integración · uso de
  APIs · proveedor definitivo · datos reales · secretos · agentes operativos ·
  software productivo; **no** crea matriz (`AI_TOOLS_MATRIX_001` queda para un PR
  futuro).
- **Relación entre documentos:** `AI-TECH-INTEL-000` define el marco;
  `AUDIT-AI-TOOLS-001` aplica ese marco a una auditoría documental; `AI-TOOLS-MATRIX-001`
  compara las herramientas auditadas.

### Namespace `AI-TOOLS-MATRIX` (PR #25)

- **Familia documental:** matriz/decisión documental. **Capa:** `AI_TECH_INTELLIGENCE`.
- **Relación:** depende de `AI-TECH-INTEL` (marco) y **deriva de** `AUDIT-AI-TOOLS`
  (auditoría). **No** lo reemplaza.
- **Propósito:** matrices comparativas de herramientas IA ya auditadas — **comparación
  documental, no decisión ejecutiva final**; subordinado a revisión humana. Ejemplo:
  `AI-TOOLS-MATRIX-001`.
- **Límites:** **no** autoriza implementación · proveedor · APIs · secretos · datos
  reales · agentes operativos · software productivo. Cualquier prueba futura requiere
  **PR separado, gate humano y prueba LAB aislada**.

### Calificador `FUTURE_CANDIDATE` (PR #25)

`FUTURE_CANDIDATE` es un **calificador documental de no-adopción**, **no** un estado
operativo independiente y **no** reemplaza los estados existentes
(`OBSERVE`/`STUDY`/`CANDIDATE`/`LAB_TEST_ONLY`/`HOLD`/`REJECT`/`ADOPTABLE_PENDING_GATE`);
es **auxiliar a `CANDIDATE`**. Indica **posible interés/candidato futuro**, y:

- **no** equivale a proveedor elegido · adopción · implementación · integración;
- **no** autoriza prueba real · uso de APIs · uso de secretos · datos reales;
- **solo** señala posible candidato futuro sujeto a: **gate humano · PR separado ·
  prueba LAB aislada · revisión de seguridad · nueva autorización documental**.

### Namespace `PACKAGE` (PR #30)

- **Familia documental:** cierre de paquete. **Capa:** `CONTROL_DOCUMENTAL`.
- **Propósito:** documentos que **cierran** el paquete de laboratorio independiente como
  paquete reutilizable LAB-ONLY (contenido, uso, flujo de PR, roles, qué permite/prohíbe,
  estados de las capas, fases futuras posibles y condiciones de gate). Ejemplo actual:
  `LAB-PACKAGE-001`.
- **Naturaleza:** solo cierre documental (`package_closure_only: true`); **no** es marco,
  auditoría, matriz, gate ni protocolo, y **no** los reemplaza.
- **Límites:** **no** autoriza implementación · integración · APIs · proveedor · datos
  reales · secretos · agentes operativos · prototipo visual · software productivo. Toda
  fase futura requiere **gate humano + PR separado**.

### Namespace `ARCH`

- **Familia documental:** arquitectura técnica de producto. **Capa:** `PRODUCT_ARCHITECTURE`.
- **Propósito:** propuestas de arquitectura técnica de producto — base SaaS, capa AaaS,
  modelo de datos candidato, alcance MVP, reglas duras de proyecto, gates de aprobación
  y benchmarks de referencia. Ejemplo actual: un documento ARCH de ejemplo.
- **Naturaleza:** solo documentación estratégica de diseño (`architecture_proposal_only:
  true`); **no** es código, base de datos, migración ni despliegue.
- **Límites:** **no** autoriza implementación · código productivo · base de datos ·
  despliegue en ningún entorno · uso de APIs externas · conexión de proveedores IA ·
  integración al proyecto principal · construcción del SaaS/AaaS. Toda fase ejecutable
  requiere **gate humano explícito + PR separado**.

> Si un validador (`scripts/`) rechaza un valor, **el validador tiene razón**:
> corregir el documento al token canónico, no relajar el validador.
