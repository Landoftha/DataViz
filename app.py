import streamlit as st
from components.sidebar import sidebar_navigation
from paths import about
from paths import analysis
from paths import home

import streamlit as st

# Oculta o menu superior e o rodapé do Streamlit
st.set_page_config(page_title="Animes Choice Based on Data", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# Load sidebar for navigation
selected_page = sidebar_navigation()

# Dynamic page loading
if selected_page == "Home":
    home.show()
if selected_page == "Analysis":
    analysis.show()
if selected_page == "About":
    about.show()


# Footer
st.markdown("---")
st.text("Built with Streamlit")
