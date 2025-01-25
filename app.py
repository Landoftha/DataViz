import streamlit as st
from components.sidebar import sidebar_navigation

import streamlit as st


st.set_page_config(page_title="Animes Choice Based on Data", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")


selected_page = sidebar_navigation()


if selected_page == "Home":
    from pages import home
    home.show()
elif selected_page == "Analysis":
    from pages import analysis
    analysis.show()
elif selected_page == "About":
    from pages import about
    about.show()



st.markdown("---")
st.text("Built with Streamlit")
