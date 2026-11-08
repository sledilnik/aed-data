# REVERSE_ENGINEERING_REPORT — aed-data

## A. General diagnosis

### Architecture identified
Python project for collection and update of AED (Automatic External Defibrillator) data in Slovenia. Downloads data from OpenStreetMap (Overpass API) and government sources (podatki.gov.si), saving as CSV/XLSX. Structure:

- `update.py`: main script with functions `import_openstreetmap()` and `import_opsi()`, HTTP session with retry/backoff
- `requirements.txt`: `requests==2.34.*`
- `sources/`: downloaded data (openstreetmap.org/slovenia.csv, podatki.gov.si/, plesko.si/)
- `.github/workflows/update.yml`: CI that runs `update.py`, commits and pushes updated data automatically

### Technologies and dependencies
- Python 3.13
- requests 2.34.*, urllib3

### Maintenance state
Default branch: main. Repository: https://github.com/sledilnik/aed-data. Scheduled workflow (cron: 25 3 * * *) + workflow_dispatch.

### Existing testing mechanisms
No automated tests found.

### Investigation limitations
- Tests not executed (require network access and external API keys).
- REA 6.7.0 not operational; static analysis only.

## B. Problems found

| ID | Title | Severity | Status | Location |
|----|-------|----------|--------|----------|
| REA-aed-001 | `.github/workflows/update.yml` uses `actions/checkout@v7` (nonexistent) | P2 | CONFIRMADO | `update.yml:37` |
| REA-aed-002 | `.github/workflows/update.yml` uses `actions/setup-python@v6` (nonexistent) | P2 | CONFIRMED | `update.yml:40` |
| REA-aed-003 | `requirements.txt`: `requests==2.34.*` may not exist | P2 | PROVÁVEL | `requirements.txt:1` |

### Details of confirmed problems

**REA-aed-001 (P2, CONFIRMED)**: The workflow uses `actions/checkout@v7`, which does not exist (maximum current is checkout@v4). CI would fail when trying to execute.

Evidence: `update.yml:37`.

**REA-aed-002 (P2, CONFIRMED)**: The workflow uses `actions/setup-python@v6`, which does not exist (maximum current is setup-python@v5). CI would fail when trying to execute.

Evidence: `update.yml:40`.

### Details of the probable problem

**REA-aed-003 (P2, PROVÁVEL)**: `requirements.txt` declares `requests==2.34.*`. The latest stable requests version is 2.32.x (2026). The pattern `2.34.*` may not match any available version, causing installation failure.

## C. Recurring problems
No recurring public issues found.

## D. Undocumented errors
All items in section B are problems not previously documented.

## E. Performance
Data collection script with retry/backoff for transient failures. Configured timeouts (120s for requests, 360s for Overpass).

## F. Technical improvements
- Fix GitHub Actions versions (REA-aed-001, REA-aed-002, implemented)
- Verify/pin correct requests version (REA-aed-003)

## G. Execution plan
Independent CI corrections, low risk, implemented in a single PR.

## H. Expected outcome
Executable CI, reproducible builds, correct dependencies.

**Tools used:** git, gh, PowerShell, static code inspection.  
**Limitation:** Tests not executed (require network).  
**Environment:** Windows, PowerShell 5.1, `C:\Users\User\audit-repos\aed-data` (clone of upstream, branch main).
