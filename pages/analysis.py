import streamlit as st
import pandas as pd
from data.data_loader import load_data
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css

style_css()
sidebar_navigation() 

st.title("Análise estatística dos dados")

file_path = "D:\Portifolio DATA SCIENCE\DataViz\data\BestAnimes\data_animes_1000+_votes.csv"
 
df = pd.read_csv(file_path) 

st.dataframe(df)

df_nota = df[df['IMDb Rating'] >= 8]

st.dataframe(df_nota[["Title", "IMDb Rating"]])

import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10, 6))
sns.histplot(df["IMDb Rating"], bins=20, kde=True, color="royalblue")

plt.xlabel("Nota IMDb")
plt.ylabel("Quantidade de Animes")
plt.title("Distribuição de Notas IMDb dos Animes")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

st.pyplot(plt)

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["IMDb Rating"], color="royalblue")

plt.xlabel("Nota IMDb")
plt.title("Boxplot das Notas IMDb dos Animes")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

st.pyplot(plt)