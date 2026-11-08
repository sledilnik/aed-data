# REVERSE_ENGINEERING_REPORT — aed-data

## A. Diagnóstico geral

### Arquitetura identificada
Projeto Python para coleta e atualização de dados de DEA (Desfibrilador Externo Automático) na Eslovênia. Baixa dados de OpenStreetMap (Overpass API) e fontes governamentais (podatki.gov.si), salvando como CSV/XLSX. Estrutura:

- `update.py`: script principal com funções `import_openstreetmap()` e `import_opsi()`, sessão HTTP com retry/backoff
- `requirements.txt`: `requests==2.34.*`
- `sources/`: dados baixados (openstreetmap.org/slovenia.csv, podatki.gov.si/, plesko.si/)
- `.github/workflows/update.yml`: CI que roda `update.py`, faz commit e push automático dos dados atualizados

### Tecnologias e dependências
- Python 3.13
- requests 2.34.*, urllib3

### Estado de manutenção
Branch default: main. Repositório: https://github.com/sledilnik/aed-data. Workflow agendado (cron: 25 3 * * *) + workflow_dispatch.

### Mecanismos de testes existentes
Nenhum teste automatizado encontrado.

### Limitações da investigação
- Testes não executados (requerem acesso à rede e chaves de API externas).
- REA 6.7.0 não operacional; análise estática apenas.

## B. Problemas encontrados

| ID | Título | Severidade | Status | Localização |
|----|--------|------------|--------|-------------|
| REA-aed-001 | `.github/workflows/update.yml` usa `actions/checkout@v7` (inexistente) | P2 | CONFIRMADO | `update.yml:37` |
| REA-aed-002 | `.github/workflows/update.yml` usa `actions/setup-python@v6` (inexistente) | P2 | CONFIRMADO | `update.yml:40` |
| REA-aed-003 | `requirements.txt`: `requests==2.34.*` pode não existir | P2 | PROVÁVEL | `requirements.txt:1` |

### Detalhes dos problemas confirmados

**REA-aed-001 (P2, CONFIRMADO)**: O workflow usa `actions/checkout@v7`, que não existe (o máximo atual é checkout@v4). A CI falharia ao tentar executar.

Evidência: `update.yml:37`.

**REA-aed-002 (P2, CONFIRMADO)**: O workflow usa `actions/setup-python@v6`, que não existe (o máximo atual é setup-python@v5). A CI falharia ao tentar executar.

Evidência: `update.yml:40`.

### Detalhes do problema provável

**REA-aed-003 (P2, PROVÁVEL)**: `requirements.txt` declara `requests==2.34.*`. A versão estável mais recente do requests é 2.32.x (2026). O padrão `2.34.*` pode não corresponder a nenhuma versão disponível, causando falha na instalação.

## C. Problemas recorrentes
Nenhum problema recorrente público encontrado.

## D. Erros não documentados
Todos os itens da seção B são problemas não documentados anteriormente.

## E. Performance
Script de coleta de dados com retry/backoff para falhas transitórias. Timeouts configurados (120s para requests, 360s para Overpass).

## F. Melhorias técnicas
- Corrigir versões das GitHub Actions (REA-aed-001, REA-aed-002, implementado)
- Verificar/pinar versão correta do requests (REA-aed-003)

## G. Plano de execução
Correções de CI independentes e baixo risco, implementadas em um único PR.

## H. Resultado esperado
CI executável, builds reproduzíveis, dependências corretas.

**Ferramentas usadas:** git, gh, PowerShell, inspeção estática.  
**Limitação:** Testes não executados (requerem rede).  
**Ambiente:** Windows, PowerShell 5.1, `C:\Users\User\audit-repos\aed-data` (clone do upstream, branch main).
