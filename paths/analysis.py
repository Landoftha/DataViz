import streamlit as st
import pandas as pd
from data.data_loader import load_data


def show():
    st.title("Dashboard de Visualização de Dados")

    file_path = "D:\Portifolio DATA SCIENCE\DataViz\data\Best_Animes_Data\data_animes_1000+_votes.csv"
    try:
        df = load_data(file_path)
        st.write("Dados carregados com sucesso!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

