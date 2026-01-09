import streamlit as st

#TODO: OAuth with google

def check_password():
    """
    Verifica se o usuário inseriu a senha correta para acessar áreas restritas.
    Retorna True se autenticado, False caso contrário.
    """
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.markdown("### 🔒 Acesso Restrito")
    password = st.text_input("Digite a senha de acesso:", type="password")
    
    if st.button("Entrar"):
        # Em produção, use st.secrets para a senha
        if password == "tjro123":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Senha incorreta.")
            
    return False

def logout():
    """Limpa a sessão de autenticação."""
    st.session_state["password_correct"] = False
    st.rerun()
