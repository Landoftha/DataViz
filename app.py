import streamlit as st
from components.sidebar import sidebar_navigation
from paths import about
from paths import analysis
from paths import home

import streamlit as st


st.set_page_config(page_title="Animes Choice Based on Data", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")


selected_page = sidebar_navigation()


if selected_page == "Home":
    home.show()
if selected_page == "Analysis":
    analysis.show()
if selected_page == "About":
    about.show()



st.markdown("---")
st.text("Built with Streamlit")
