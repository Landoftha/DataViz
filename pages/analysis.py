import streamlit as st
from data.data_loader import load_data
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css

st.set_page_config(
    page_title="Hipóteses",
    page_icon="🧠",
    layout="centered"
)

style_css()
sidebar_navigation() 

st.title("Hipóteses")
st.write("Bem vindo a pagina!")

st.write("Descrição do Projeto : Este projeto foi criado para ajudar a entender, na prática, como funcionam as teorias de hipóteses. A ideia é usar dados de empresas — reais ou simuladas — para formular perguntas (hipóteses) e testar se elas fazem sentido com base na estatística. Vamos passar por etapas como escolher os dados, preparar tudo para análise, aplicar testes estatísticos (como teste t ou ANOVA) e tirar conclusões a partir dos resultados. No final, tudo será reunido em um relatório que mostra o que foi aprendido e como aplicar isso no mundo real. É uma forma prática e organizada de fixar o conhecimento sobre hipóteses e análise de dados.")