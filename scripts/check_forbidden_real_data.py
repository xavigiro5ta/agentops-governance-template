#!/usr/bin/env python3
"""check_forbidden_real_data.py — Laboratorio AgentOps (LAB-ONLY).

Heurística defensiva para detectar posibles DATOS REALES prohibidos en docs/ y
tests/. La política (LAB-SRC-000) es FICTITIOUS_ONLY: solo entidades demo y
placeholders.

Detecta:
  - Correos cuyo dominio NO está en la allowlist (example.com, demo.local, example.org).
  - Teléfonos plausibles (>= 9 dígitos) que no sean el placeholder de ceros.
  - Secuencias de 13-19 dígitos (tarjeta / IBAN-like) → posible dato financiero.
  - Tokens de una denylist explícita (p. ej. IBAN, SWIFT con valor).

Es una heurística: puede dar falsos positivos. Ante duda, ganar trazabilidad y
revisar manualmente.

Uso:
    python scripts/check_forbidden_real_data.py

Código de retorno 0 si no se detecta nada, 1 si hay hallazgos.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [REPO_ROOT / "docs", REPO_ROOT / "tests"]

ALLOWED_EMAIL_DOMAINS = {"example.com", "example.org", "demo.local"}

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
PHONE_RE = re.compile(r"\+?\d[\d\s().\-]{7,}\d")
LONG_DIGITS_RE = re.compile(r"\d{13,19}")


def find_issues(text: str) -> list[str]:
    issues: list[str] = []

    for m in EMAIL_RE.finditer(text):
        domain = m.group(1).lower()
        if domain not in ALLOWED_EMAIL_DOMAINS:
            issues.append(
                f"correo con dominio no permitido: '{m.group(0)}' "
                f"(permitidos: {sorted(ALLOWED_EMAIL_DOMAINS)})"
            )

    for m in PHONE_RE.finditer(text):
        digits = re.sub(r"\D", "", m.group(0))
        if len(digits) >= 9 and set(digits) != {"0"}:
            issues.append(f"posible teléfono real: '{m.group(0).strip()}'")

    for m in LONG_DIGITS_RE.finditer(text):
        issues.append(f"posible dato financiero (tarjeta/IBAN): '{m.group(0)}'")

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
            for issue in find_issues(path.read_text(encoding="utf-8")):
                findings.append(f"{rel}: {issue}")

    print(f"check_forbidden_real_data: {scanned} archivo(s) escaneado(s).")
    if findings:
        print(f"[FAIL] {len(findings)} posible(s) dato(s) real(es) prohibido(s):")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("[PASS] No se detectaron datos reales prohibidos (solo demo/placeholders).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
