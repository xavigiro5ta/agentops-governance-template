---
document_id: LAB-SRC-000
title: Fuente Única de Control — Laboratorio AgentOps
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

# Fuente Única de Control (Single Source of Truth)

> **Modo:** LAB-ONLY. Este documento es la **fuente única** de reglas de gobierno
> del laboratorio. Si cualquier otro documento contradice a este, este documento
> prevalece **dentro del laboratorio**. Este documento **no declara canon** para el
> proyecto principal.

## 1. Propósito

Definir, en un único lugar, las reglas, vocabularios controlados y límites de
autorización del laboratorio AgentOps. El laboratorio existe para **probar el
sistema de gobierno** (AGENTS.md, CLAUDE.md, skills, índice, bitácora,
validadores y pruebas de comportamiento) **antes** de integrar cualquier patrón
al proyecto principal.

## 2. Qué es y qué no es este laboratorio

- **Es:** un banco de pruebas de gobernanza documental y de comportamiento de agentes.
- **No es:** el software real. No construye producto real, ni base de datos,
  ni migraciones, ni integraciones, ni automatizaciones.

## 3. Política de datos (obligatoria)

- `data_policy: FICTITIOUS_ONLY`.
- Prohibido usar nombres reales de empresa, restaurante, unidad, personas,
  clientes, proveedores, teléfonos, correos reales o datos financieros reales.
- Entidades ficticias permitidas (y **únicas** permitidas):
  - **Empresa Demo**
  - **Unidad Operativa Demo**
  - **Usuario Demo**
  - **Proveedor Demo**
  - **Documento Demo**
- Dominios/correos: solo placeholders (`@example.com`, `@demo.local`).

## 4. Vocabulario controlado

### 4.1 `status`
| Valor | Significado |
| --- | --- |
| `DRAFT` | Borrador en construcción. |
| `IN_REVIEW` | En revisión humana. |
| `APPROVED_LAB` | Aprobado **solo** para uso de laboratorio. |
| `DEPRECATED` | Reemplazado por una versión posterior. |
| `ARCHIVED` | Conservado como histórico, sin uso activo. |

### 4.2 `canon_status`
| Valor | Significado |
| --- | --- |
| `NOT_CANON` | **Único valor permitido** en el laboratorio. No es verdad oficial del proyecto principal. |

### 4.3 `classification`
| Valor | Significado |
| --- | --- |
| `LAB_INTERNAL` | Uso interno del laboratorio. Único valor permitido. |

### 4.4 `data_policy`
| Valor | Significado |
| --- | --- |
| `FICTITIOUS_ONLY` | Solo datos ficticios. Único valor permitido. |

### 4.5 Banderas de autorización (booleanas)
En modo LAB-ONLY **todas** deben ser `false`:
`implementation_authorized`, `code_authorized`, `database_authorized`,
`automation_authorized`, `integration_authorized`.

## 5. Metadata mínima obligatoria

Todo documento controlado en `docs/00_CONTROL_DOCUMENTAL/` debe incluir front
matter YAML con **todos** estos campos:

```
document_id, title, version, status, canon_status, classification,
created_by, requested_by, date, data_policy, implementation_authorized,
code_authorized, database_authorized, automation_authorized, integration_authorized
```

Los validadores en `scripts/` verifican mecánicamente este contrato.

## 6. Convención de `document_id`

Formato: `LAB-<TIPO>-<NNN>` (mayúsculas, sin espacios).

| Tipo | Uso |
| --- | --- |
| `SRC` | Fuente única de control. |
| `IDX` | Índice maestro. |
| `LOG` | Bitácora. |
| `MODEL` | Modelo maestro AgentOps. |
| `FIX` | Fixtures de prueba. |
| `REP` | Reportes. |
| `VAL` | Resultados de validación. |
| `VOCAB` | Vocabulario controlado y equivalencias. |
| `REQ` | Necesidades funcionales esperadas. |
| `GATES` | Matriz de gates. |
| `ROLES` | Matriz de roles de agentes. |
| `DOD` | Definition of Done. |
| `TEST` | Casos de comportamiento de agentes. |
| `AUDIT` | Auditorías de necesidades, especificaciones y continuidad. |
| `METHGOV` | Gobierno metodológico — índice/guía y checklist de la capa (PR #2). |
| `METHOD` | Control metodológico (entradas/salidas, gates, bloqueo/advertencia/aprobación). |
| `ROUTER` | Router metodológico de clasificación y enrutamiento de solicitudes. |
| `STAGE` | Control de estados de madurez y transiciones. |
| `ALERTS` | Catálogo de alertas metodológicas (INFO/WARNING/BLOCKER). |
| `MAP` | Mapa ejecutivo/operativo del laboratorio (navegación y control de alto nivel). |
| `ADV` | Validación adversarial controlada (bloqueo/derivación/advertencia/aclaración ante solicitudes peligrosas o fuera de alcance). |
| `AI-TECH-INTEL` | Documentos de inteligencia tecnológica IA (evaluación estratégica de herramientas IA externas). Capa `AI_TECH_INTELLIGENCE`. |
| `AUDIT-AI-TOOLS` | Auditorías documentales de herramientas IA externas. Familia `AUDIT`, capa `AI_TECH_INTELLIGENCE`; subordinado a `AI-TECH-INTEL`. |
| `AI-TOOLS-MATRIX` | Matrices comparativas derivadas de auditorías IA. Familia matriz/decisión documental, capa `AI_TECH_INTELLIGENCE`; depende de `AI-TECH-INTEL` (marco) y deriva de `AUDIT-AI-TOOLS`. |
| `PROJECT-IDENTITY` | Documentos de identidad interna del proyecto (nombre canónico, alcance, especialización de dominio, reglas de nomenclatura). No autoriza nombre comercial definitivo sin gate humano. |
| `PACKAGE` | Documentos de cierre del paquete de laboratorio independiente (qué contiene el LAB, cómo se usa, qué permite/prohíbe, fases futuras y gates). Capa `CONTROL_DOCUMENTAL`; **no** autoriza implementación, integración, adopción de proveedor ni software productivo. |
| `ARCH` | Propuestas de arquitectura técnica de producto (SaaS, AaaS, modelo de datos, MVP, reglas duras, gates de aprobación). Documentación estratégica de diseño; **no** autoriza implementación, código, base de datos, despliegue ni integración al proyecto principal. |

> **Procedencia de los tipos (extensión LAB-ONLY):**
> - `METHGOV`, `METHOD`, `ROUTER`, `STAGE`, `ALERTS`: incorporados por **PR #3**
>   como consolidación de los documentos de **PR #2** (gobierno metodológico).
> - `MAP`: incorporado por **PR #4** (mapa ejecutivo, `LAB-MAP-000`).
> - `ADV`: incorporado por **GitHub PR #5** (validación adversarial, `LAB-ADV-000`).
> - `AI-TECH-INTEL`: incorporado por **PR #20** (consolidación de la capa
>   `AI_TECH_INTELLIGENCE` creada en PR #19, `AI-TECH-INTEL-000`). **Uso:** documentos
>   de inteligencia tecnológica IA. **Alcance:** LAB-ONLY. **Canon:** `NOT_CANON`.
>   **Función:** evaluación estratégica de herramientas IA externas. **No** autoriza
>   implementación, integración, adopción de proveedor ni software productivo.
>   Ejemplo actual: `AI-TECH-INTEL-000`.
> - `AUDIT-AI-TOOLS`: incorporado por **PR #23** (consolidación del namespace creado
>   por `AUDIT-AI-TOOLS-001` en PR #22). **Familia documental:** `AUDIT`. **Capa:**
>   `AI_TECH_INTELLIGENCE`. **Relación:** subordinado/metodológicamente dependiente de
>   `AI-TECH-INTEL` (no lo reemplaza). **Propósito:** auditorías documentales de
>   herramientas IA externas. **NO** autoriza implementación, integración, uso de
>   APIs, proveedor definitivo, datos reales, secretos, agentes operativos ni software
>   productivo; **no** crea matriz por sí mismo. Ejemplo actual: `AUDIT-AI-TOOLS-001`.
> - `AI-TOOLS-MATRIX`: incorporado por **PR #25** (consolidación del namespace creado
>   por `AI-TOOLS-MATRIX-001` en PR #24). **Familia documental:** matriz/decisión
>   documental. **Capa:** `AI_TECH_INTELLIGENCE`. **Relación:** depende de
>   `AI-TECH-INTEL` (marco) y **deriva de** `AUDIT-AI-TOOLS` (auditoría). **Propósito:**
>   matrices comparativas de herramientas IA ya auditadas — **comparación documental,
>   no decisión ejecutiva final**; subordinado a revisión humana. **NO** autoriza
>   implementación, proveedor, APIs, secretos, datos reales, agentes operativos ni
>   software productivo. Ejemplo actual: `AI-TOOLS-MATRIX-001`.
> - **Relación documental:** `AI-TECH-INTEL-000` define el marco; `AUDIT-AI-TOOLS-001`
>   audita herramientas IA; `AI-TOOLS-MATRIX-001` compara herramientas auditadas.
>   Ninguno autoriza adopción, implementación o integración; cualquier prueba futura
>   requiere PR separado, gate humano y prueba LAB aislada.
> - `PACKAGE`: incorporado por **PR #30** (consolidación del namespace creado por
>   `LAB-PACKAGE-001` en PR #29). **Capa:** `CONTROL_DOCUMENTAL`. **Propósito:**
>   documentos de cierre del paquete de laboratorio independiente (contenido, uso,
>   flujo de PR, roles, qué permite/prohíbe, fases futuras y condiciones de gate). **NO**
>   autoriza implementación, integración, uso de APIs, proveedor, datos reales, secretos,
>   agentes operativos, prototipo visual ni software productivo; es **solo cierre
>   documental** (`package_closure_only: true`). Ejemplo actual: `LAB-PACKAGE-001`.
> - **Calificador `FUTURE_CANDIDATE`:** calificador **documental de no-adopción** (no
>   un estado operativo independiente). Indica posible interés/candidato futuro sujeto
>   a gate humano, PR separado, prueba LAB aislada, revisión de seguridad y nueva
>   autorización documental. **No** equivale a proveedor elegido, adopción,
>   implementación ni integración; **no** autoriza prueba real, APIs, secretos ni datos
>   reales. **No reemplaza** los estados existentes (`OBSERVE`/`STUDY`/`CANDIDATE`/
>   `LAB_TEST_ONLY`/`HOLD`/`REJECT`/`ADOPTABLE_PENDING_GATE`); es auxiliar a `CANDIDATE`.
> - `PROJECT-IDENTITY`: incorporado por **PR #31** (línea base de identidad del proyecto
>   `PROJECT-IDENTITY-001`). **Propósito:** documentar el nombre canónico, alcance,
>   especialización de dominio y reglas de nomenclatura del proyecto. **NO** autoriza
>   nombre comercial definitivo, implementación, integración, prototipo ni software
>   productivo. Nombre definitivo del sistema: pendiente de gate humano.
> - `ARCH`: incorporado por un PR de arquitectura del proyecto (ejemplo de
>   propuesta de arquitectura técnica). **Propósito:** propuestas de arquitectura técnica de producto —
>   base SaaS, modelo de datos, MVP, reglas duras, gates de aprobación y referencias
>   de benchmarks. **NO** autoriza implementación, código, base de datos, despliegue,
>   proveedor, APIs, integración al proyecto principal ni construcción del SaaS/AaaS.
>   Capa `PRODUCT_ARCHITECTURE`. Ejemplo actual: un documento ARCH de ejemplo.
>
> Todos son **extensión LAB-ONLY**; **nada** de esto autoriza integración al
> proyecto principal. El checklist usa el espacio `METHGOV` con sufijo `CHK`
> (`LAB-METHGOV-CHK-001`).

Los `document_id` deben ser **únicos** en todo el repo (validado mecánicamente).

> **Tabla extendida de vocabulario controlado:** `LAB-VOCAB-000`
> (`LAB_VOCAB_000_VOCABULARIO_CONTROLADO_v0.1.0.md`) es la **referencia
> autoritativa** del vocabulario y de los tipos documentales. Esta tabla de §6 y
> la de `LAB-VOCAB-000` §6 deben mantenerse alineadas; ante divergencia, se
> reconcilian vía la skill `source-consolidation` conservando ambos tokens.

## 7. Límite de integración (no negociable)

> **Integración al proyecto principal: NO autorizada.** Requiere validación de
> laboratorio y revisión humana explícita. Ningún patrón, skill o documento de
> este laboratorio se considera apto para producción por el solo hecho de existir aquí.

## 8. Jerarquía de autoridad documental

1. `LAB-SRC-000` (este documento) — reglas de gobierno del laboratorio.
2. `LAB-MODEL-000` — modelo maestro AgentOps (cómo se organiza el sistema).
3. `AGENTS.md` / `CLAUDE.md` — instrucciones operativas para agentes.
4. Skills en `.agents/skills/` — procedimientos estrechos.
5. Resto de documentos.

Ante conflicto entre rapidez y trazabilidad, **prevalece la trazabilidad**.
