import streamlit as st
import pandas as pd
from utils.processing import load_data

def show():
    st.title("Data Analysis")
    
    # Load data
    df = load_data()
    st.dataframe(df)
    
    # Simple chart
    st.bar_chart(df["value"])
