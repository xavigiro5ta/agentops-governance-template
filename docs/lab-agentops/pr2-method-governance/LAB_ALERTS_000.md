---
document_id: LAB-ALERTS-000
title: Catálogo de Alertas Metodológicas — Laboratorio AgentOps
project: AgentOps LAB
version: 0.1.0
status: DRAFT
canon_status: NOT_CANON
classification: LAB_INTERNAL
method_classification: METHOD_GOVERNANCE
created_by: Claude Code
requested_by: Usuario Demo
date: 2026-06-08
data_policy: FICTITIOUS_ONLY
scope: Experimental methodological governance layer (LAB-ONLY)
implementation_authorized: false
code_authorized: false
database_authorized: false
automation_authorized: false
integration_authorized: false
---

# Catálogo de Alertas Metodológicas (LAB-ALERTS-000)

> Alertas transversales que vigilan el flujo de trabajo. Severidad: **INFO**
> (registrar), **WARNING** (corregir antes de avanzar), **BLOCKER** (detener).
> Fuente de reglas: `LAB-SRC-000`. Todos los ejemplos son ficticios.

## 1. Resumen por severidad

| ID | Nombre | Severidad |
| --- | --- | --- |
| AL-01 | SCOPE_CREEP | WARNING |
| AL-02 | PRODUCTIVE_CODE_RISK | BLOCKER |
| AL-03 | REAL_DATA_RISK | BLOCKER |
| AL-04 | CI_ACTIVATION_RISK | BLOCKER |
| AL-05 | PACKAGE_MODIFICATION_RISK | BLOCKER |
| AL-06 | MAIN_PROJECT_CONTAMINATION | BLOCKER |
| AL-07 | OVERDOCUMENTATION_RISK | WARNING |
| AL-08 | UNDERDOCUMENTATION_RISK | WARNING |
| AL-09 | AMBIGUOUS_REQUEST | WARNING |
| AL-10 | UNVALIDATED_ASSUMPTION | WARNING |
| AL-11 | PREMATURE_AUTOMATION | BLOCKER |
| AL-12 | MISSING_GATE | WARNING |
| AL-13 | BROKEN_TRACEABILITY | WARNING |
| AL-14 | ROLE_CONFUSION | INFO |
| AL-15 | CANONIZATION_RISK | BLOCKER |
| AL-16 | SECRET_TOKEN_RISK | BLOCKER |

## 2. Detalle de alertas

### AL-01 · SCOPE_CREEP
- **Severidad:** WARNING
- **Descripción:** El alcance crece más allá de lo acordado.
- **Condición de activación:** Se añaden entregables no pedidos o el encargo se expande sin gate.
- **Acción recomendada:** Volver al encargo; registrar cambio de alcance vía ACLARAR (`LAB-ROUTER-000`).
- **Qué NO hacer:** Continuar ejecutando el alcance ampliado en silencio.
- **Ejemplo ficticio:** Se pide un README y aparecen además 5 documentos no solicitados.

### AL-02 · PRODUCTIVE_CODE_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de escribir software productivo.
- **Condición de activación:** Se solicita o se intenta crear código ejecutable de producción.
- **Acción recomendada:** Bloquear; ofrecer estrategia en papel (`code_authorized: false`).
- **Qué NO hacer:** Escribir el código "solo como ejemplo" en el repo productivo.
- **Ejemplo ficticio:** "Crea el endpoint real de pedidos de la Unidad Operativa Demo."

### AL-03 · REAL_DATA_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de uso de datos reales.
- **Condición de activación:** Aparecen nombres, correos, teléfonos o finanzas reales.
- **Acción recomendada:** Bloquear; sustituir por fixtures demo; `check_forbidden_real_data.py`.
- **Qué NO hacer:** Guardar el dato real "temporalmente".
- **Ejemplo ficticio:** Sustituir `usuario.demo@example.com` por un correo de una persona real.

### AL-04 · CI_ACTIVATION_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de activar CI antes de validar.
- **Condición de activación:** Se intenta crear/activar workflows o pipelines.
- **Acción recomendada:** Bloquear; CI se evalúa en un PR futuro, solo LAB.
- **Qué NO hacer:** Crear `.github/workflows/*`.
- **Ejemplo ficticio:** "Agrega un workflow que corra los checks en cada push."

### AL-05 · PACKAGE_MODIFICATION_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de modificar dependencias/build.
- **Condición de activación:** Cambios en `package.json`, lockfiles o configuración de build.
- **Acción recomendada:** Bloquear; no tocar dependencias.
- **Qué NO hacer:** Añadir paquetes "para una utilidad pequeña".
- **Ejemplo ficticio:** "Instala una librería para parsear YAML en `package.json`."

### AL-06 · MAIN_PROJECT_CONTAMINATION
- **Severidad:** BLOCKER
- **Descripción:** Mezcla del laboratorio con el proyecto principal.
- **Condición de activación:** Se editan archivos Next.js o se entrelaza lab con producción.
- **Acción recomendada:** Bloquear; mantener separación estricta.
- **Qué NO hacer:** Importar documentos LAB desde el código del sitio.
- **Ejemplo ficticio:** "Renderiza los documentos LAB dentro de una página del sitio."

### AL-07 · OVERDOCUMENTATION_RISK
- **Severidad:** WARNING
- **Descripción:** Documentación excesiva o duplicada.
- **Condición de activación:** Se duplica contenido o se documenta sin decisión asociada.
- **Acción recomendada:** Consolidar vía `source-consolidation`; eliminar duplicados.
- **Qué NO hacer:** Crear un tercer documento que repite a otros dos.
- **Ejemplo ficticio:** Tres documentos describiendo el mismo gate con palabras distintas.

### AL-08 · UNDERDOCUMENTATION_RISK
- **Severidad:** WARNING
- **Descripción:** Documentación insuficiente para decidir.
- **Condición de activación:** Falta propósito, criterios o trazabilidad mínima.
- **Acción recomendada:** Completar metadata y secciones mínimas (`LAB-DOD-000`).
- **Qué NO hacer:** Aprobar una pieza sin criterios de validación.
- **Ejemplo ficticio:** Un documento sin sección de "criterios de aprobación".

### AL-09 · AMBIGUOUS_REQUEST
- **Severidad:** WARNING
- **Descripción:** Solicitud ambigua o incompleta.
- **Condición de activación:** No hay objetivo claro ni datos suficientes.
- **Acción recomendada:** Ruta ACLARAR; devolver con preguntas.
- **Qué NO hacer:** Asumir intención y ejecutar.
- **Ejemplo ficticio:** "Mejora el laboratorio" sin especificar qué.

### AL-10 · UNVALIDATED_ASSUMPTION
- **Severidad:** WARNING
- **Descripción:** Supuesto no verificado.
- **Condición de activación:** Una decisión depende de algo no comprobado.
- **Acción recomendada:** Marcar el supuesto y validarlo antes de avanzar.
- **Qué NO hacer:** Construir sobre el supuesto como si fuera hecho.
- **Ejemplo ficticio:** Suponer que "el Proveedor Demo acepta X" sin evidencia.

### AL-11 · PREMATURE_AUTOMATION
- **Severidad:** BLOCKER
- **Descripción:** Automatizar antes de validar comportamiento.
- **Condición de activación:** Se pide activar automatizaciones reales.
- **Acción recomendada:** Bloquear; mantener todo manual y en papel.
- **Qué NO hacer:** Conectar un disparador automático "de prueba".
- **Ejemplo ficticio:** "Que el sistema mande avisos automáticos al cerrar caja."

### AL-12 · MISSING_GATE
- **Severidad:** WARNING
- **Descripción:** Se intenta avanzar sin el gate requerido.
- **Condición de activación:** Transición de estado sin su gate (`LAB-STAGE-000`).
- **Acción recomendada:** Detener y exigir el gate correspondiente.
- **Qué NO hacer:** Pasar a `LAB_ACCEPTED` saltando `LAB_REVIEW`.
- **Ejemplo ficticio:** Aprobar como LAB sin que `run_all_checks.py` esté en PASS.

### AL-13 · BROKEN_TRACEABILITY
- **Severidad:** WARNING
- **Descripción:** Se pierde el rastro entre documentos/decisiones.
- **Condición de activación:** Falta entrada en índice/bitácora o referencias cruzadas.
- **Acción recomendada:** Restaurar enlaces; registrar en `LAB-IDX-000`/`LAB-LOG-001`.
- **Qué NO hacer:** Continuar sin registrar el cambio.
- **Ejemplo ficticio:** Un documento nuevo que no aparece en ningún índice.

### AL-14 · ROLE_CONFUSION
- **Severidad:** INFO
- **Descripción:** Un agente actúa fuera de su rol.
- **Condición de activación:** Un rol intenta una acción reservada a otro (`LAB-ROLES-000`).
- **Acción recomendada:** Reasignar la acción al rol correcto.
- **Qué NO hacer:** Permitir que un agente cruce un gate humano (G3/G4/GM-5).
- **Ejemplo ficticio:** Un script "aprobando" canon en lugar de solo validar.

### AL-15 · CANONIZATION_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de declarar canon sin gate humano.
- **Condición de activación:** Se intenta marcar `CANON_APPROVED` o `canon_status` ≠ `NOT_CANON`.
- **Acción recomendada:** Bloquear; canon solo por gate humano explícito separado.
- **Qué NO hacer:** Cambiar `canon_status` a un valor distinto de `NOT_CANON`.
- **Ejemplo ficticio:** "Marca este documento como canon oficial del proyecto."

### AL-16 · SECRET_TOKEN_RISK
- **Severidad:** BLOCKER
- **Descripción:** Riesgo de introducir secretos, tokens, API keys o credenciales
  en el repositorio (reales o ficticios que parezcan reales).
- **Condición de activación:** Se intenta guardar un token en el repo; pegar
  credenciales en un documento; usar API keys; registrar claves, contraseñas o
  credenciales; o pedir a un agente que almacene o reutilice secretos.
- **Acción recomendada:** **Bloquear**; eliminar el secreto del contenido si
  aparece; si hubiese sido real, exigir su **rotación fuera del repositorio**; no
  continuar hasta limpiar el input. Sustituir por un placeholder claramente inválido.
- **Qué NO hacer:** Guardar el secreto "temporalmente"; commitearlo; reutilizarlo;
  ni siquiera dejarlo en el historial.
- **Ejemplo ficticio:** "Guarda esta API key `DEMO-NOT-A-REAL-TOKEN-xxxx` en el
  repositorio para usarla después." (placeholder ficticio, no es un token válido).

## 3. Estado documental

`LAB-ONLY / NOT_CANON`. Autorizaciones en `false`.

> **Integración al proyecto principal: NO autorizada; requiere validación de
> laboratorio y revisión humana.**
