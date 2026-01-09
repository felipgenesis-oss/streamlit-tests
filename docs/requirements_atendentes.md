# Requisitos do Módulo: Atendentes (Registro de Denúncia)

## 1. Visão Geral
Este módulo é destinado aos atendentes e ao público em geral (quando acessado via link público) para o registro inicial de denúncias de assédio e discriminação. O objetivo é garantir um ambiente seguro, acolhedor e intuitivo para o preenchimento das informações.

## 2. Objetivos
- **Facilidade de Acesso:** Permitir o registro rápido de denúncias.
- **Segurança e Anonimato:** Oferecer opções claras para identificação ou anonimato.
- **Integração:** Conectar diretamente com a base de dados (Google Sheets ou banco relacional) para alimentar o fluxo operacional.

## 3. Requisitos Funcionais
- **Formulário de Denúncia:**
  - Campos para identificação da vítima (opcional/anônimo).
  - Identificação do denunciado (nome, cargo, setor).
  - Descrição do fato (data, local, relato detalhado).
  - Upload de evidências (se suportado).
  - Classificação inicial (Assédio Moral, Assédio Sexual, Discriminação).
- **Integração Externa:**
  - Incorporação do Google Forms (solução atual) ou formulário nativo Streamlit.
- **Confirmação:**
  - Exibição de mensagem de sucesso e orientações pós-registro (ex: canais de acolhimento psicológico).

## 4. Detalhes Técnicos
- **Arquivo:** `pages/1_📝_Registrar_Denuncia.py`
- **Componentes Streamlit:**
  - `st.components.v1.iframe` para incorporar o Google Forms existente.
  - Alternativamente, `st.form` para um formulário nativo, validado com Pydantic em `src/schemas.py`.
