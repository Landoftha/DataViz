import streamlit as st
from data.data_loader import load_data
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Hipóteses",
    page_icon="🧠",
    layout="centered"
)

style_css()
sidebar_navigation() 

st.title("Hipóteses")

st.markdown("**Análise Exploratória com Geração de Hipóteses sobre Churn**")
st.markdown("**Objetivo:** Entender os principais fatores que levam clientes de uma empresa de telecomunicações a cancelar seus serviços, por meio da análise de dados e geração de hipóteses.")
st.markdown("**Contexto:** Utilizando o dataset de churn da IBM, que contém informações demográficas, contratuais e de uso dos serviços, este projeto simula um cenário de análise investigativa dentro de uma empresa preocupada com a retenção de clientes.")

telco_df = load_data('.\data\TelcoCustomer\Telco-Customer-Churn.csv')

st.subheader("Esse é o DataFrame a ser utilizado")
st.dataframe((telco_df.head()))

st.subheader("Análise das variáveis numéricas e categóricas")


st.write(telco_df.describe(include='all'))

numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
for col in numeric_cols:
    fig, ax = plt.subplots()
    sns.histplot(telco_df[col], kde=True, ax=ax)
    ax.set_title(f'Distribuição de {col}')
    st.pyplot(fig)

for col in numeric_cols:
    fig, ax = plt.subplots()
    sns.boxplot(data=telco_df, x=col, ax=ax)
    ax.set_title(f'Boxplot de {col}')
    st.pyplot(fig)    

st.subheader("📊 Categóricas por Churn")

categorical_cols = ['Contract', 'InternetService', 'OnlineSecurity',
                    'TechSupport', 'PaperlessBilling', 'PaymentMethod', 'gender']

selected_col = st.selectbox("Escolha a variável para comparar com Churn", categorical_cols)

fig, ax = plt.subplots()
sns.countplot(data=telco_df, x=selected_col, hue='Churn', ax=ax)
ax.set_title(f"Churn por {selected_col}")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.subheader("Identificação de possíveis outliers ou inconsistências")





st.subheader("Visualizações para entender padrões de churn")





st.subheader("Geração de Hipóteses")