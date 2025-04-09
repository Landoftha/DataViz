import streamlit as st
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css

style_css()
sidebar_navigation() 

st.title("Machine Learning")
st.write("Bem vindo a pagina!")


st.write("Em breve...")