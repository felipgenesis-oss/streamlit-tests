import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Registrar Denúncia", layout="wide")

st.title("📝 Canal de Denúncias")
st.markdown("### Envie seu relato de forma segura")

st.info("Este canal é seguro e pode ser utilizado para denúncias anônimas ou identificadas.")

# URL do formulário Google Forms (pode ser movido para config/secrets futuramente)
URL_DO_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfMruCNLgN07W8S-qldf4KcezQBAxA2D0kHZokVcM-8n4N6Mg/viewform?embedded=true"

# Renderiza o formulário
components.iframe(URL_DO_FORM, height=1200, scrolling=True)
