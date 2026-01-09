# Requisitos do Módulo: Indicadores de Gestão (Gestores)

## 1. Visão Geral
Módulo focado em visão macro e estatística para a alta gestão do Tribunal (Presidência, Corregedoria). Não foca em casos individuais, mas em tendências, volumes e performance da comissão.

## 2. Objetivos
- **Transparência:** Apresentar dados consolidados sobre o enfrentamento ao assédio.
- **Tomada de Decisão:** Identificar setores ou cargos com maior incidência para ações preventivas.
- **Monitoramento de Performance:** Avaliar a agilidade da comissão e das unidades responsáveis.

## 3. Requisitos Funcionais
- **KPIs Principais:**
  - Total de denúncias no período.
  - Taxa de resolução (Arquivados vs Em Andamento).
  - Tempo médio de atendimento.
- **Gráficos e Visualizações:**
  - Distribuição por Tipo de Assédio (Moral, Sexual, Discriminação).
  - Volume de denúncias por Unidade/Setor.
  - Série temporal (evolução mensal das denúncias).
- **Filtros:**
  - Filtragem por período (ano/mês).

## 4. Detalhes Técnicos
- **Arquivo:** `pages/3_📊_Indicadores_Gestao.py`
- **Bibliotecas:** `pandas` para agregação de dados, `altair` ou `st.bar_chart` para visualizações.
- **Performance:** Cache de dados (`st.cache_data`) é crítico aqui para não recarregar a planilha inteira a cada interação de filtro.
