import streamlit as st
from components.sidebar import sidebar_navigation

import streamlit as st


st.set_page_config(page_title="Animes Choice Based on Data", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")


selected_page = sidebar_navigation()


if selected_page == "Home":
    from paths import home
    home.show()
if selected_page == "Analysis":
    from paths import analysis
    analysis.show()
if selected_page == "About":
    from paths import about
    about.show()



st.markdown("---")
st.text("Built with Streamlit")
