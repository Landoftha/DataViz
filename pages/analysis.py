import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from data.data_loader import load_data
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css

style_css()
sidebar_navigation() 

st.title("Análise estatística dos dados")

file_path = "D:\Portifolio DATA SCIENCE\DataViz\data\BestAnimes\data_animes_1000+_votes.csv"
 
df = pd.read_csv(file_path) 

##st.dataframe(df)

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


df_nota_ano = df.groupby('Year')['IMDb Rating'].mean().reset_index()

fig = px.line(df_nota_ano, y='IMDb Rating', x='Year', 
title='Média da Nota do IMDb por ano de lançamento do Anime')
fig.update_traces(line_color='green', line_width=4)
fig.update_layout(width=1000, height=500,
    font_family='Arial',
    font_size=14,
    font_color='grey',
    title_font_size=22,
    xaxis_title='Ano de Lançamento',
    yaxis_title='Média das Notas do IMDb')

st.plotly_chart(fig, use_container_width=True)


df_anime_ano = df.groupby('Year').size().reset_index(name='quantity')


fig = px.line(df_anime_ano, x=df_anime_ano.Year, y=df_anime_ano.columns,
 title='Quantidade de Animes lançados em cada Ano', markers=True)

fig.update_layout(
    xaxis_title='Ano', 
    yaxis_title='Quantidade de Animes'

)

st.plotly_chart(fig, use_container_width=True)
