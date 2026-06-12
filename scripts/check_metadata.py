#!/usr/bin/env python3
"""check_metadata.py — Laboratorio AgentOps (LAB-ONLY).

Verifica que todo documento controlado en docs/ incluya el front matter YAML con
los 15 campos de metadata mínima exigidos por LAB-SRC-000, y que ninguno esté vacío.

Uso:
    python scripts/check_metadata.py

Salida:
    Imprime hallazgos. Código de retorno 0 si todo OK, 1 si hay errores.

Sin dependencias externas: parser de front matter minimalista.
"""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "document_id",
    "title",
    "version",
    "status",
    "canon_status",
    "classification",
    "created_by",
    "requested_by",
    "date",
    "data_policy",
    "implementation_authorized",
    "code_authorized",
    "database_authorized",
    "automation_authorized",
    "integration_authorized",
]

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"


def parse_front_matter(text: str) -> dict[str, str] | None:
    """Devuelve el front matter YAML (clave: valor planos) o None si no existe."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    fm: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fm
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return None  # cierre '---' no encontrado


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
            errors.append(f"{rel}: falta front matter YAML al inicio del archivo")
            continue
        checked += 1
        for field in REQUIRED_FIELDS:
            if field not in fm:
                errors.append(f"{rel}: falta campo requerido '{field}'")
            elif fm[field] == "":
                errors.append(f"{rel}: campo '{field}' está vacío")

    print(f"check_metadata: {checked} documento(s) con front matter analizado(s).")
    if errors:
        print(f"[FAIL] {len(errors)} hallazgo(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("[PASS] Metadata mínima presente y no vacía en todos los documentos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
