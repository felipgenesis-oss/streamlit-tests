# Requisitos do Módulo: Operacional CPCAD (Comissão)

## 1. Visão Geral
Este módulo é a área de trabalho da Comissão de Enfrentamento ao Assédio. Ele centraliza o controle de prazos, triagem de denúncias e o fluxo processual.

## 2. Objetivos
- **Controle de Prazos:** Evitar que denúncias fiquem paradas por mais tempo que o permitido (SLA).
- **Gestão de Fluxo:** Acompanhar a denúncia desde a triagem até o arquivamento ou encaminhamento.
- **Rastreabilidade:** Saber exatamente com quem está cada processo (Corregedoria, Presidência, Comissão).

## 3. Requisitos Funcionais
- **Painel de Prazos (SLA):**
  - Indicadores visuais (Semaforo: Verde/Amarelo/Vermelho) baseados na data da última movimentação.
  - Alerta para processos parados há mais de 48h.
- **Lista de Processos:**
  - Tabela interativa com filtros por Fase, Status e Responsável.
  - Visualização rápida dos detalhes do caso.
- **Atualização de Status (Admin):**
  - Permissão para alterar a "Fase Atual" e inserir "ID Processo SEI".
  - *Nota:* Atualmente a escrita pode estar limitada se usar apenas leitura de Planilha Pública, necessitando de Service Account para escrita real.

## 4. Detalhes Técnicos
- **Arquivo:** `pages/2_⚙️_Operacional_CPCAD.py`
- **Fonte de Dados:** Conexão com Google Sheets via `streamlit-gsheets`.
- **Lógica de Negócio:**
  - Cálculo de dias úteis/corridos (`src/utils.py`).
  - Regras de negócio para definição de responsabilidade (1º Grau vs 2º Grau).
- **Segurança:** Acesso protegido por senha (implementado via `src/auth.py`).
