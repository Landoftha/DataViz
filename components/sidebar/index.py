import streamlit as st


def sidebar_navigation():
    st.sidebar.image("logo.png", use_container_width=True)
    st.sidebar.page_link("app.py", label="📂 Menu Principal")

    st.sidebar.markdown("---")  # Linha divisória
    st.sidebar.markdown("### 📌 Navegação", unsafe_allow_html=True)

    st.sidebar.page_link("pages/analysis.py", label="🔍 Análise")
    st.sidebar.page_link("pages/dashboard.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/about.py", label="📖 Sobre")

    st.sidebar.markdown("---")

