import streamlit as st


def sidebar_navigation():
    st.sidebar.image("logo1.png", use_container_width=True)
    st.sidebar.page_link("app.py", label=" Sobre ")

    st.sidebar.markdown("---")  # Linha divisória
    st.sidebar.markdown("###  Navegação", unsafe_allow_html=True)

    st.sidebar.page_link("pages/analysis.py", label=" Hipóteses")
    st.sidebar.page_link("pages/ml.py", label="Aprendizado de Máquina ")
    st.sidebar.page_link("pages/database.py", label=" Banco de Dados")
    st.sidebar.page_link("pages/dataviz.py", label=" Visualização de Dados")

    st.sidebar.markdown("---")

