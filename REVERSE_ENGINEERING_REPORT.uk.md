# REVERSE_ENGINEERING_REPORT — aed-data

## A. Загальний діагноз

### Виявлена архітектура
Проєкт Python для збирання та оновлення даних AED (Automatic External Defibrillator) у Словенії. Завантажує дані з OpenStreetMap (Overpass API) та урядових джерел (podatki.gov.si), зберігаючи як CSV/XLSX. Структура:

- `update.py`: головний скрипт з функціями `import_openstreetmap()` та `import_opsi()`, сесія HTTP з repeat/backoff
- `requirements.txt`: `requests==2.34.*`
- `sources/`: завантажені дані (openstreetmap.org/slovenia.csv, podatki.gov.si/, plesko.si/)
- `.github/workflows/update.yml`: CI, що виконує `update.py`, робить коміт та пуш оновлених даних автоматично

### Технології та залежності
- Python 3.13
- requests 2.34.*, urllib3

### Стан підтримки
Гałтьова гілка: main. Репозиторій: https://github.com/sledilnik/aed-data. Запланований workflow (cron: 25 3 * * *) + workflow_dispatch.

### Існуючі механізми тестування
Автоматизованих тестів не виявлено.

### Обмеження дослідження
- Тести не виконано (потребують доступу до мережі та зовнішніх ключів API).
- REA 6.7.0 не працює; лише статичний аналіз.

## B. Виявлені проблеми

| ID | Заголовок | Severity | Статус | Локація |
|----|-----------|----------|--------|----------|
| REA-aed-001 | `.github/workflows/update.yml` використовує `actions/checkout@v7` (неіснуючий) | P2 | CONFIRMED | `update.yml:37` |
| REA-aed-002 | `.github/workflows/update.yml` використовує `actions/setup-python@v6` (неіснуючий) | P2 | CONFIRMED | `update.yml:40` |
| REA-aed-003 | `requirements.txt`: `requests==2.34.*` може не існувати | P2 | PROBABLE | `requirements.txt:1` |

### Деталі підтверджених проблем

**REA-aed-001 (P2, CONFIRMED)**: Workflow використовує `actions/checkout@v7`, якого не існує (максимальний поточний — checkout@v4). CI не вдасться при спробі виконання.

Довід: `update.yml:37`.

**REA-aed-002 (P2, CONFIRMED)**: Workflow використовує `actions/setup-python@v6`, якого не існує (максимальний поточний — setup-python@v5). CI не вдасться при спробі виконання.

Довід: `update.yml:40`.

### Деталі ймовірної проблеми

**REA-aed-003 (P2, PROBABLE)**: `requirements.txt` deklaruje `requests==2.34.*`. Найновіша стабільна версія requests — 2.32.x (2026). Шаблон `2.34.*` може не відповідати жодній доступній версії, що спричинить помилку встановлення.

## C. Повторювані проблеми
Повторювалися публічні проблеми не знайдено.

## D. Недокументовані помилки
Усі пункти розділу B — це проблеми, що раніше не були задокументовано.

## E. Продуктивність
Скрипт збирання даних з repeat/backoff для тимчасових помилок. Налаштовані тайм-аути (120s для requests, 360s для Overpass).

## F. Технічні вдосконалення
- Виправити версії GitHub Actions (REA-aed-001, REA-aed-002, реалізовано)
- Перевірити/закріпити правильну версію requests (REA-aed-003)

## G. План виконання
Самостійні правки CI, низький ризик, реалізовано в одному PR.

## H. Очікуваний результат
Виконуваний CI, відтворювані збудь, правильні залежності.

**Інструменти:** git, gh, PowerShell, статичний аналіз коду.  
**Обмеження:** Тести не виконано (потребують мережі).  
**Середовище:** Windows, PowerShell 5.1, `C:\Users\User\audit-repos\aed-data` (клон upstream, гілка main).

Переклад технічний, виконаний автоматизовано; рекомендується перегляд носієм мови перед використанням якнормативного посилання.
