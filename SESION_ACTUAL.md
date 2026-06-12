# SESION_ACTUAL — AgentOps Governance Template

> Leer al inicio de cada sesión. Actualizar al cerrar. Máximo 1 página.
> Es el ancla de contexto: refleja siempre el estado real del repositorio.

## Estado

**Fecha última sesión:** 2026-06-12
**Quién trabajó:** —
**Estado del repo:** plantilla base v0.1.0 · idioma por defecto: español

## Lo que está hecho

- ✅ Gobierno documental base (15 documentos controlados + índice + bitácora).
- ✅ 6 validadores mecánicos (`scripts/`) — `run_all_checks.py` 5/5 PASS.
- ✅ 6 skills de método (`.agents/skills/`).
- ✅ Datos 100% ficticios; 0 autorizaciones activas; `canon_status: NOT_CANON`.

## Próximo paso (solo uno)

**Adoptar la plantilla para tu proyecto:**
1. Completar `PROJECT-IDENTITY-001` con la identidad real (vía gate humano).
2. Adaptar `LAB-SRC-000`, `AGENTS.md` y `CLAUDE.md` a tu dominio.
3. Registrar la decisión en `LAB-LOG-001` y validar con `run_all_checks.py`.

## No tocar sin gate

- Los validadores de `scripts/` — funcionan; cambiarlos requiere decisión registrada.
- Las banderas de autorización — se mantienen en `false` hasta gate humano.
- La historia de la bitácora — es append-only: no se reescribe.

## Señal de alerta

Si llevas más de 30 minutos sin cerrar nada concreto → para, actualiza este archivo
y cierra la sesión.
