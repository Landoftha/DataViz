import streamlit as st
from components.sidebar.index import sidebar_navigation
from components.sidebar.style import style_css


st.set_page_config(page_title="Yohanalytics", page_icon="📊", layout="wide")

style_css()
sidebar_navigation() 

st.title("Menu")