---
document_id: LAB-ROUTER-000
title: Router Metodológico — Clasificación y Enrutamiento de Solicitudes
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

# Router Metodológico (LAB-ROUTER-000)

> Clasifica cada solicitud entrante y decide la **ruta**: aprobar como LAB,
> derivar, pedir aclaración o bloquear. Fuente de reglas: `LAB-SRC-000`.
> Aplica las reglas de `LAB-METHOD-000`.

## 1. Propósito

Dar a cada entrada una ruta trazable y un gate requerido, evitando que una
solicitud salte directamente a construcción o integración.

## 2. Tipos de entrada y clasificación

| Tipo de entrada | Naturaleza |
| --- | --- |
| Idea inicial | Intención sin definir |
| Problema operativo | Necesidad de análisis (demo) |
| Módulo funcional | Pedido de funcionalidad |
| Documento de arquitectura | Diseño técnico (en papel) |
| Prototipo visual | Maqueta no productiva |
| Bug o falla | Reporte de defecto |
| Cambio de alcance | Modificación del encargo |
| Solicitud de automatización | Pedido de automatizar |
| Solicitud de datos reales | Pedido de datos reales |
| Solicitud de integración externa | Conectar sistemas |
| Solicitud de código productivo | Construir software real |
| Solicitud ambigua | Sin información suficiente |

## 3. Rutas metodológicas

- **APROBAR_LAB**: admisible como documento/plan LAB-ONLY.
- **DERIVAR**: requiere otro documento/rol antes de avanzar.
- **ACLARAR**: falta información; se devuelve con preguntas.
- **BLOQUEAR**: viola las restricciones LAB-ONLY; no se ejecuta.

## 4. Quién/qué interviene

| Ruta | Interviene |
| --- | --- |
| APROBAR_LAB | `LAB-METHOD-000` (validación) + `LAB-STAGE-000` (estado) |
| DERIVAR | documento destino + rol correspondiente (`LAB-ROLES-000`) |
| ACLARAR | quien emite la solicitud (Usuario/Dirección) |
| BLOQUEAR | regla de `LAB-METHOD-000` §8 + alerta de `LAB-ALERTS-000` |

## 5. Matriz de decisión

Formato: **Input detectado | Riesgo | Ruta recomendada | Gate requerido | Resultado permitido**

| Input detectado | Riesgo | Ruta recomendada | Gate requerido | Resultado permitido |
| --- | --- | --- | --- | --- |
| Idea inicial | Bajo | APROBAR_LAB | GM-1 | Documento `IDEA`/`DISCOVERY` |
| Problema operativo | Bajo | APROBAR_LAB | GM-1, GM-2 | Análisis LAB (demo) |
| Módulo funcional | Medio | DERIVAR | GM-2, GM-4 | Especificación en papel (no código) |
| Documento de arquitectura | Medio | APROBAR_LAB | GM-2, GM-3 | Diseño documental LAB |
| Prototipo visual | Medio | DERIVAR | GM-2, GM-4 | Maqueta conceptual (sin software real) |
| Bug o falla | Bajo/Medio | ACLARAR/DERIVAR | GM-1 | Reporte LAB (sin parchear producción) |
| Cambio de alcance | Medio | ACLARAR | GM-1, GM-5 | Actualización de encargo + bitácora |
| Solicitud de automatización | Alto | BLOQUEAR | — | Plan en papel; sin activar nada |
| Solicitud de datos reales | Alto | BLOQUEAR | — | Sustituir por fixtures demo |
| Solicitud de integración externa | Alto | BLOQUEAR | — | Estrategia en papel (G4 cerrado) |
| Solicitud de código productivo | Alto | BLOQUEAR | — | Estrategia/diseño LAB, sin código |
| Solicitud ambigua | Medio | ACLARAR | GM-1 | Preguntas de clarificación |

## 6. Qué debe BLOQUEAR

Datos reales; código productivo; base de datos/migraciones; APIs/integraciones
externas; automatizaciones reales; CI/workflows; cambios en `package.json`/Next.js;
declarar canon; autorizaciones en `true`; tocar proyecto principal / "BaseConocimientoDemo
Sofward" / "DemoProducto productivo".

## 7. Qué debe DERIVAR

Módulos funcionales, prototipos y arquitecturas que requieren un documento destino
y un estado de madurez antes de continuar (a `LAB-STAGE-000` / rol responsable).

## 8. Qué debe pedir ACLARAR

Solicitudes ambiguas, cambios de alcance y bugs sin contexto suficiente: se
devuelven con preguntas antes de asignar ruta definitiva.

## 9. Qué puede APROBAR como LAB

Ideas, problemas operativos demo, documentos de arquitectura en papel y análisis,
siempre que pasen GM-1..GM-3 y permanezcan `NOT_CANON`.

## 10. Estado documental

`LAB-ONLY / NOT_CANON`. Autorizaciones en `false`.

> **Integración al proyecto principal: NO autorizada; requiere validación de
> laboratorio y revisión humana.**
