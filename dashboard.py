import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import streamlit.components.v1 as components
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Monitoramento CPCAD", layout="wide")

# --- SISTEMA DE SENHA SIMPLES ---
def check_password():
    """Retorna True se o usuário inseriu a senha correta."""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # Tela de Login
    st.title("Acesso Restrito - CPCAD")
    password = st.text_input("Digite a senha de acesso:", type="password")
    if st.button("Entrar"):
        if password == "tjro123": # <--- Mude sua senha aqui!
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Senha incorreta.")
    return False

if not check_password():
    st.stop() # Interrompe o script se não estiver logado

# --- CONTINUAÇÃO DO CÓDIGO ORIGINAL ---
def render_dashboard():
    st.title("Painel de Monitoramento - CPCAD/TJRO")
    st.markdown("### Controle de Prazos e Fluxos de Denúncias")

    # --- 1. CARREGAMENTO DOS DADOS (Google Sheets ao vivo) ---
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    try:
        # Lê a planilha configurada no secrets.toml
        # ttl=0 garante que ele busque dados novos sempre que der F5
        df = conn.read(ttl=0)
    except Exception as e:
        st.error(f"Erro ao conectar com o Google Sheets: {e}")
        st.info("Verifique se a planilha está compartilhada como 'Qualquer pessoa com o link pode ler'.")
        return

    # Limpar linhas totalmente vazias (comum em planilhas de Forms)
    df = df.dropna(how='all')

    if df.empty:
        st.warning("A planilha está vazia. Aguardando denúncias...")
        return

    # Mapeamento de colunas (Para lidar com nomes longos do Forms)
    # Vamos tentar encontrar as colunas essenciais
    col_data = df.columns[0] # Geralmente 'Carimbo de data/hora'
    col_cargo = next((c for c in df.columns if 'cargo' in c.lower()), df.columns[-1])
    col_tipo = next((c for c in df.columns if 'tipo' in c.lower() or 'notícia' in c.lower()), df.columns[1])
    
    # Garantir colunas de controle (Caso não existam na planilha original, o robô cria)
    if 'ID Processo SEI' not in df.columns:
        df['ID Processo SEI'] = 'PENDENTE'
    if 'Fase Atual' not in df.columns:
        df['Fase Atual'] = 'Triagem Inicial'
    if 'Data Ultima Movimentacao' not in df.columns:
        df['Data Ultima Movimentacao'] = df[col_data]

    # --- 2. TRATAMENTO DE DADOS (A Lógica do Robô) ---
    df[col_data] = pd.to_datetime(df[col_data])
    df['Data Ultima Movimentacao'] = pd.to_datetime(df['Data Ultima Movimentacao'])
    agora = datetime.now()

    def definir_responsavel(cargo):
        cargo = str(cargo).lower()
        if 'juiz' in cargo or 'magistrado' in cargo:
            return 'Corregedoria (1º Grau)'
        elif 'desembargador' in cargo:
            return 'Presidência (2º Grau)'
        else:
            return 'CPCAD (Comissão)'

    df['Unidade Responsável'] = df[col_cargo].apply(definir_responsavel)

    def calcular_dias_parado(row):
        return (agora - row['Data Ultima Movimentacao']).days

    df['Dias Sem Movimentação'] = df.apply(calcular_dias_parado, axis=1)

    def calcular_status(row):
        dias_parado = row['Dias Sem Movimentação']
        if dias_parado >= 2: return '🔴 ATRASADO (> 2 dias)'
        elif dias_parado >= 1: return '🟡 ATENÇÃO'
        else: return '🟢 NO PRAZO'

    df['Status Prazos'] = df.apply(calcular_status, axis=1)

    # --- 3. O DASHBOARD ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Denúncias", len(df))
    col2.metric("Casos Críticos", len(df[df['Status Prazos'].str.contains('ATRASADO')]))
    col3.metric("Novos (24h)", len(df[df[col_data] > (agora - timedelta(days=1))]))

    st.divider()

    st.subheader("Monitoramento de Prazos (Urgente)")
    
    # Exibe apenas as colunas importantes
    cols_to_show = ['ID Processo SEI', col_data, col_tipo, 'Unidade Responsável', 'Dias Sem Movimentação', 'Fase Atual', 'Status Prazos']
    
    # Filtrar apenas colunas que realmente existem
    cols_to_show = [c for c in cols_to_show if c in df.columns]
    
    def color_status(val):
        if 'ATRASADO' in str(val): return 'background-color: red; color: white'
        if 'ATENÇÃO' in str(val): return 'background-color: orange; color: white'
        return 'background-color: green; color: white'

    st.dataframe(df[cols_to_show].style.applymap(color_status, subset=['Status Prazos']), use_container_width=True, hide_index=True)

    # Gráficos
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Tipos de Denúncia")
        st.bar_chart(df[col_tipo].value_counts())
    with c2:
        st.subheader("Volume por Unidade Responsável")
        st.bar_chart(df['Unidade Responsável'].value_counts())

    # Nota sobre gravação
    with st.expander("🔧 Área Admin: Como atualizar?"):
        st.info("""
        **Modo Somente Leitura Ativado:** 
        Como estamos usando o link público da planilha, o painel Admin consegue ler tudo em tempo real, mas para **salvar** o número do SEI ou a Fase de volta na planilha, você deve:
        
        1. Abrir a planilha do Google Sheets diretamente.
        2. Preencher a coluna 'ID Processo SEI' ou 'Fase Atual' lá.
        3. O painel aqui atualizará automaticamente ao recarregar.
        
        *Dica: Se quiser que o botão 'Salvar' do Admin funcione diretamente por aqui, precisaremos configurar uma 'Service Account' do Google Cloud.*
        """)
        processo = st.selectbox("Selecione o Processo (Data/Tipo)", df['Carimbo de data/hora'].astype(str) + " - " + df['Tipo de notícia'])
        nova_fase = st.selectbox("Nova Fase", ["Triagem Inicial", "Acolhimento Psicológico", "Junta de Apuração", "Presidência", "Arquivado"])
        if st.button("Atualizar Fase"):
            st.success(f"Processo atualizado para: {nova_fase} (Simulação)")

def render_canal_denuncia():
    st.title("Canal de Denúncias")
    st.markdown("### Envie seu relato de forma segura")
    
    # O link do seu formulário (versão embedded)
    url_do_form = "https://docs.google.com/forms/d/e/1FAIpQLSfMruCNLgN07W8S-qldf4KcezQBAxA2D0kHZokVcM-8n4N6Mg/viewform?embedded=true"

    # Renderiza o iframe
    # height: altura em pixels (ajuste conforme o tamanho do form)
    # scrolling: permite rolar se o form for maior que a janela
    components.iframe(url_do_form, height=1200, scrolling=True)

# --- Navegação Lateral ---
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Painel de Monitoramento", "Canal de Denúncias"])

if pagina == "Painel de Monitoramento":
    render_dashboard()
else:
    render_canal_denuncia()