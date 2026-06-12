#!/usr/bin/env python3
"""check_status_values.py — Laboratorio AgentOps (LAB-ONLY).

Verifica el vocabulario controlado y las banderas de autorización del front matter,
según LAB-SRC-000:

  - status        ∈ {DRAFT, IN_REVIEW, APPROVED_LAB, DEPRECATED, ARCHIVED}
  - canon_status  == NOT_CANON
  - classification== LAB_INTERNAL
  - data_policy   == FICTITIOUS_ONLY
  - banderas de autorización == false (todas):
        implementation_authorized, code_authorized, database_authorized,
        automation_authorized, integration_authorized

Uso:
    python scripts/check_status_values.py

Código de retorno 0 si todo cumple, 1 si hay violaciones.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"

ALLOWED_STATUS = {"DRAFT", "IN_REVIEW", "APPROVED_LAB", "DEPRECATED", "ARCHIVED"}
FIXED_VALUES = {
    "canon_status": "NOT_CANON",
    "classification": "LAB_INTERNAL",
    "data_policy": "FICTITIOUS_ONLY",
}
MUST_BE_FALSE = [
    "implementation_authorized",
    "code_authorized",
    "database_authorized",
    "automation_authorized",
    "integration_authorized",
]


def parse_front_matter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    fm: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            return fm
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return None


def main() -> int:
    errors: list[str] = []
    checked = 0

    if not DOCS_DIR.exists():
        print(f"[error] No existe el directorio docs/: {DOCS_DIR}")
        return 1

    for md in sorted(DOCS_DIR.rglob("*.md")):
        rel = md.relative_to(REPO_ROOT)
        fm = parse_front_matter(md.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: sin front matter; no se puede validar vocabulario")
            continue
        checked += 1

        status = fm.get("status", "")
        if status not in ALLOWED_STATUS:
            errors.append(
                f"{rel}: status '{status}' inválido (permitidos: {sorted(ALLOWED_STATUS)})"
            )

        for field, expected in FIXED_VALUES.items():
            if fm.get(field, "") != expected:
                errors.append(
                    f"{rel}: {field} debe ser '{expected}', no '{fm.get(field, '')}'"
                )

        for field in MUST_BE_FALSE:
            value = fm.get(field, "").lower()
            if value != "false":
                errors.append(
                    f"{rel}: {field} debe ser 'false' en modo LAB-ONLY, no '{fm.get(field, '')}'"
                )

    print(f"check_status_values: {checked} documento(s) analizado(s).")
    if errors:
        print(f"[FAIL] {len(errors)} hallazgo(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("[PASS] Vocabulario controlado y autorizaciones (=false) correctos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
