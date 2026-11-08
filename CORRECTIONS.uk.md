# CORRECTIONS.md — aed-data

Project: sledilnik/aed-data
Base branch analyzed: main
Destination fork: https://github.com/admeduardovieira/aed-data

## Corrections implemented

| ID | Title | Severity | Status | Risk | Files involved |
|----|-------|----------|--------|------|----------------|
| REA-aed-001 | `.github/workflows/update.yml` uses `actions/checkout@v7` (nonexistent) | P2 | IMPLEMENTED | Low | `.github/workflows/update.yml` |
| REA-aed-002 | `.github/workflows/update.yml` uses `actions/setup-python@v6` (nonexistent) | P2 | IMPLEMENTED | Low | `.github/workflows/update.yml` |
| REA-aed-003 | `requirements.txt`: `requests==2.34.*` may not exist | P2 | NOT IMPLEMENTED | Low | `requirements.txt` |

## Details of implemented corrections

### REA-aed-001 — Nonexistent checkout@v7
**Problem:** `update.yml` used `actions/checkout@v7`, which does not exist (maximum is checkout@v4).
**Fix:** Changed to `actions/checkout@v4`.
**Validation:** File syntax verified.

### REA-aed-002 — Nonexistent setup-python@v6
**Problem:** `update.yml` used `actions/setup-python@v6`, which does not exist (maximum is setup-python@v5).
**Fix:** Changed to `actions/setup-python@v5`.
**Validation:** File syntax verified.

## Corrections not implemented

### REA-aed-003 — requests version may not exist
Not implemented: requires verifying the actual latest requests version. Suggested: pin to `requests==2.32.*` or remove version pin.

## Publication plan
- Fork: `admeduardovieira/aed-data` (created).
- Branch `fix/rea-aed-001-002` for corrections.
- Commit identity: `admeduardovieira <admeduardovieira@users.noreply.github.com>`.
- PR #25: https://github.com/sledilnik/aed-data/pull/25 (open, base main).

Переклад технічний, виконаний автоматизовано; рекомендується перегляд носієм мови перед використанням якнормативного посилання.
