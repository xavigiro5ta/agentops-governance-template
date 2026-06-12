#!/usr/bin/env python3
"""run_all_checks.py — Laboratorio AgentOps (LAB-ONLY).

Orquesta los validadores mecánicos y agrega el resultado. No modifica documentos,
no autoriza integración. Un PASS global NO habilita la integración al proyecto
principal (LAB-SRC-000).

Uso:
    python scripts/run_all_checks.py

Código de retorno 0 si todos pasan, 1 si alguno falla.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

CHECKS = [
    "check_metadata.py",
    "check_duplicate_ids.py",
    "check_status_values.py",
    "check_forbidden_real_data.py",
    "check_forbidden_secrets.py",
]


def main() -> int:
    results: list[tuple[str, bool]] = []

    for check in CHECKS:
        print("=" * 70)
        print(f"▶ Ejecutando {check}")
        print("=" * 70)
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / check)],
            cwd=str(SCRIPTS_DIR.parent),
        )
        results.append((check, proc.returncode == 0))
        print()

    print("=" * 70)
    print("RESUMEN DE VALIDACIÓN (LAB-ONLY)")
    print("=" * 70)
    all_pass = True
    for check, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {check}")
        all_pass = all_pass and ok

    print("-" * 70)
    if all_pass:
        print("RESULTADO GLOBAL: PASS")
        print(
            "Nota: una validación verde NO autoriza integración al proyecto "
            "principal. Requiere revisión humana (LAB-SRC-000)."
        )
        return 0
    print("RESULTADO GLOBAL: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
