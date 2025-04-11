import streamlit as st
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css


st.set_page_config(page_title="Yohanalytics", page_icon="📊", layout="wide")

style_css()
sidebar_navigation() 

st.title(" Sobre o Projeto")
st.markdown("---")

# SOBRE O PORTFÓLIO
st.write("""
Este projeto foi criado com o objetivo de servir como um **portfólio interativo**.  
Aqui, você encontrará uma vitrine dos meus conhecimentos e habilidades em:

- **Análise de Dados**
- **Machine Learning**
- **Desenvolvimento Web com Streamlit**
- **Visualização de Dados**
- **Banco de Dados**

A ideia é apresentar projetos de forma clara, interativa e acessível para recrutadores, colegas de profissão ou qualquer pessoa interessada no meu trabalho.
""")

# SOBRE MIM
st.markdown("###  Sobre Mim")
st.write("""
Sou uma pessoa apaixonada por tecnologia, dados e inovação.  
Estou sempre buscando aprender, criar e compartilhar soluções que tenham impacto positivo.
""")

# CONTATO
st.markdown(" **Contato**: thaysyohanacosta71@exemplo.com")
st.markdown(" [GitHub](https://github.com/Landoftha/DataViz) | [LinkedIn](https://linkedin.com/in/thays-yohana)")
st.markdown("---")

# PROJETOS EM DESTAQUE
st.markdown("## Projetos em Destaque")

st.subheader("Previsão de Aluguel com Machine Learning")
st.write("""
Utilizando **web scraping** em sites como Zap Imóveis e Chaves na Mão, coletei dados de imóveis em Curitiba para treinar um modelo de **machine learning** capaz de prever o valor de aluguel com base em características como localização, metragem, número de quartos, etc.
""")

st.subheader(" Análise de Churn com Geração de Hipóteses")
st.write("""
Análise exploratória de dados de uma empresa de telecomunicações para entender os motivos do cancelamento de clientes (churn).  
Hipóteses foram criadas e testadas com base em variáveis como tipo de contrato, forma de pagamento e adesão a serviços extras, com foco em estratégias de retenção.
""")

st.subheader("Modelagem de Banco de Dados para uma Edtech")
st.write("""
Proposta de modelagem de banco de dados para uma plataforma educacional nos moldes da **Alura**, com foco em escalabilidade, organização dos cursos, usuários, progresso, certificações, entre outros aspectos essenciais de uma edtech.
""")

st.subheader("Mapa de Calor de Segurança Pública")
st.write("""
Com dados públicos de ocorrências policiais, foi criado um **mapa de calor** interativo que mostra as áreas com maior incidência de crimes. Projeto com foco em **visualização geográfica**, análise temporal e insights estratégicos para segurança pública.
""")
