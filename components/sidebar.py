import streamlit as st

def sidebar_navigation():
    st.sidebar.header("Navigation")
    return st.sidebar.radio("Select a page", ["Home", "Analysis", "About"])
