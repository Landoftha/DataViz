import streamlit as st
from components.sidebar import sidebar_navigation

# Load sidebar for navigation
selected_page = sidebar_navigation()

# Dynamic page loading
if selected_page == "Home":
    from pages import home
    home.show()
elif selected_page == "Analysis":
    from pages import analysis
    analysis.show()
elif selected_page == "About":
    from pages import about
    about.show()


# Footer
st.markdown("---")
st.text("Built with Streamlit")
