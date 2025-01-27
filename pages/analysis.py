import streamlit as st
import pandas as pd
from data.data_loader import load_data
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css

style_css()
sidebar_navigation() 

st.title("Análise estatística dos dados")

file_path = "D:\Portifolio DATA SCIENCE\DataViz\data\BestAnimes\data_animes_1000+_votes.csv"
try:
    df = load_data(file_path)
    st.dataframe(df)
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")

