import streamlit as st
from components.sidebar import sidebar_navigation


import streamlit as st

# Oculta o menu superior e o rodapé do Streamlit
st.set_page_config(page_title="Animes Choice Based on Data", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Load sidebar for navigation
selected_page = sidebar_navigation()

# Dynamic page loading
if selected_page == "Home":
    from paths import home
    home.show()
elif selected_page == "Analysis":
    from paths import analysis
    analysis.show()
elif selected_page == "About":
    from paths import about
    about.show()


# Footer
st.markdown("---")
st.text("Built with Streamlit")
