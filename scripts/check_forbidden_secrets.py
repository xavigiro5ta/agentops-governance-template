#!/usr/bin/env python3
"""check_forbidden_secrets.py — Laboratorio AgentOps (LAB-ONLY).

Detector mínimo, local y determinista de secretos/tokens en la documentación del
laboratorio. Implementa el protocolo `LAB-METHOD-002` (PR #11), que baja a concreto
el plan `LAB-METHOD-001` (PR #10) y el riesgo `SECRET_TOKEN_RISK`/AL-16 (PR #7).

Diseño (prudente, para evitar falsos positivos):
  - Escanea SOLO archivos Markdown bajo docs/ y tests/ (no toca scripts/, por lo que
    no se auto-detecta).
  - Marca como BLOQUEANTE únicamente una *asignación* con una palabra clave de
    secreto (api key / token / secret / password / credential / bearer) seguida de
    `:` o `=` (o `bearer <valor>`) cuyo valor PAREZCA una credencial real.
  - Permite placeholders claramente inválidos y menciones de riesgo sin valor.

No usa dependencias externas (solo librería estándar). No usa secretos reales.

Uso:
    python scripts/check_forbidden_secrets.py

Código de retorno 0 si no hay hallazgos bloqueantes, 1 si los hay.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [REPO_ROOT / "docs", REPO_ROOT / "tests"]

# Palabras clave de claves sospechosas (no incluye genéricos como "clave"/"key" sueltos
# para no generar ruido sobre el vocabulario del laboratorio).
SECRET_KEY = r"(?:api[_\-\s]?key|secret(?:[_\-]?key)?|token|password|passwd|pwd|credential)"

# Asignación: <clave-secreta> [:=] <valor>
ASSIGN_RE = re.compile(
    r"(?i)\b" + SECRET_KEY + r"\b\s*[`\"']?\s*[:=]\s*[`\"']?\s*([^\s`\"',|*]+)"
)
# Bearer <valor>
BEARER_RE = re.compile(r"(?i)\bbearer\s+[`\"']?([A-Za-z0-9\-_\.\+/=]+)")

# Valores claramente inválidos / placeholders permitidos.
ALLOWLIST_VALUES = {
    "demo-not-a-real-token",
    "placeholder-secret-invalid",
    "fake-credential-do-not-use",
    "secret_token_risk",
    "lab_secret_detector_protocol_001",
}
SAFE_MARKERS = (
    "demo", "placeholder", "fake", "invalid", "example", "not-a-real",
    "notareal", "do-not-use", "donotuse", "redacted", "changeme", "your-",
    "xxx", "...", "<", "fictic", "sospechos", "valor",
)


def _normalize(value: str) -> str:
    return value.strip().strip("`\"'.,()[]{}*").strip()


def _is_safe(value: str) -> bool:
    v = value.lower()
    if v in ALLOWLIST_VALUES:
        return True
    return any(marker in v for marker in SAFE_MARKERS)


def _looks_like_secret(value: str) -> bool:
    """Heurística conservadora: token contiguo, largo y de aspecto credencial."""
    if len(value) < 20:
        return False
    if not re.fullmatch(r"[A-Za-z0-9\-_\.\+/=]+", value):
        return False
    has_alpha = bool(re.search(r"[A-Za-z]", value))
    has_digit = bool(re.search(r"[0-9]", value))
    # Exigir mezcla letra+dígito (aspecto credencial), o longitud muy alta.
    return (has_alpha and has_digit) or len(value) >= 40


def find_issues(text: str) -> list[tuple[int, str]]:
    issues: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        candidates: list[str] = []
        for m in ASSIGN_RE.finditer(line):
            candidates.append(m.group(1))
        for m in BEARER_RE.finditer(line):
            candidates.append(m.group(1))
        for raw in candidates:
            value = _normalize(raw)
            if not value:
                continue
            if _is_safe(value):
                continue
            if _looks_like_secret(value):
                issues.append((lineno, value))
    return issues


def main() -> int:
    findings: list[str] = []
    scanned = 0

    for base in SCAN_DIRS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            scanned += 1
            rel = path.relative_to(REPO_ROOT)
            for lineno, value in find_issues(path.read_text(encoding="utf-8")):
                # Seguridad: NUNCA imprimir el valor; solo su longitud redactada,
                # sin prefijo, sufijo ni fragmentos.
                redacted = f"<redacted:{len(value)} chars>"
                findings.append(
                    f"{rel}:{lineno}: posible secreto/credencial: {redacted} "
                    f"(usar placeholder claramente inválido; rotar fuera del repo si fuese real)"
                )

    print(f"check_forbidden_secrets: {scanned} archivo(s) Markdown escaneado(s).")
    if findings:
        print(f"[FAIL] {len(findings)} hallazgo(s) de secretos/tokens:")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("[PASS] No se detectaron secretos/tokens (solo placeholders inválidos / menciones de riesgo).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
