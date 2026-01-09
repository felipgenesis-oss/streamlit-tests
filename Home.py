import streamlit as st

TJRO_BLUE = "#0c326f"
TJRO_IMAGE = "https://www.tjro.jus.br/templates/portal_tjro_helix_j5/images/presets/default/logo.png"

def render_svg_icon(svg_path):
    return f"""
    <div style="display: flex; justify-content: center; margin-bottom: 10px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="{TJRO_BLUE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            {svg_path}
        </svg>
    </div>
    """

st.set_page_config(
    page_title="Portal CPCAD", 
    layout="centered", 
    page_icon="⚖️", 
    initial_sidebar_state="auto"
)

st.image(TJRO_IMAGE, width=200)
st.title("Sistema de Gestão - CPCAD")
st.info("Bem-vindo ao sistema de monitoramento da Comissão de Enfrentamento ao Assédio.")


Atendimento, Operacional, Gestao = st.columns(3, gap="large", vertical_alignment="center")

with Atendimento:
    
    icon_doc = '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>'
    st.markdown(render_svg_icon(icon_doc), unsafe_allow_html=True)

    st.subheader("Atendimento", text_alignment="center")
    st.caption("Registro de denúncias e links públicos.")
    if st.button("Acessar Registro", use_container_width=True):
        st.switch_page("pages/Registrar_Denuncia.py")

with Operacional:

    icon_gear = '<circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>'
    st.markdown(render_svg_icon(icon_gear), unsafe_allow_html=True)

    st.subheader("Operacional", text_alignment="center")
    st.caption("Triagem, prazos e fluxo da comissão.")
    if st.button("Painel Interno", use_container_width=True):
        st.switch_page("pages/Operacional_CPCAD.py")

with Gestao:

    icon_chart = '<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>'
    st.markdown(render_svg_icon(icon_chart), unsafe_allow_html=True)

    st.subheader("Gestão", text_alignment="center")
    st.caption("Indicadores e relatórios gerenciais.")
    if st.button("Ver Dashboard", use_container_width=True):
        st.switch_page("pages/Indicadores_Gestao.py")

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 12px;">
       Desenvolvido pelo <strong>Laboratório de Inovação Gênesis</strong> - TJRO <br>© 2025 ViaJus. Todos os direitos reservados. 
    </div>
    """, 
    unsafe_allow_html=True
)