#!/usr/bin/env python3
"""check_duplicate_ids.py — Laboratorio AgentOps (LAB-ONLY).

Verifica que cada `document_id` declarado en el front matter de los documentos de
docs/ sea único en todo el repositorio (regla de LAB-SRC-000).

Uso:
    python scripts/check_duplicate_ids.py

Código de retorno 0 si no hay duplicados, 1 si los hay (o si falta document_id).
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"


def front_matter_value(text: str, key: str) -> str | None:
    if not text.startswith("---"):
        return None
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            k, _, v = line.partition(":")
            if k.strip() == key:
                return v.strip()
    return None


def main() -> int:
    ids: dict[str, list[str]] = defaultdict(list)
    missing: list[str] = []

    if not DOCS_DIR.exists():
        print(f"[error] No existe el directorio docs/: {DOCS_DIR}")
        return 1

    for md in sorted(DOCS_DIR.rglob("*.md")):
        rel = str(md.relative_to(REPO_ROOT))
        doc_id = front_matter_value(md.read_text(encoding="utf-8"), "document_id")
        if not doc_id:
            missing.append(rel)
            continue
        ids[doc_id].append(rel)

    duplicates = {k: v for k, v in ids.items() if len(v) > 1}

    print(f"check_duplicate_ids: {len(ids)} document_id único(s) detectado(s).")
    failed = False
    if missing:
        failed = True
        print(f"[FAIL] {len(missing)} documento(s) sin document_id:")
        for m in missing:
            print(f"  - {m}")
    if duplicates:
        failed = True
        print(f"[FAIL] {len(duplicates)} document_id duplicado(s):")
        for doc_id, files in duplicates.items():
            print(f"  - {doc_id}: {', '.join(files)}")

    if failed:
        return 1
    print("[PASS] Todos los document_id son únicos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
