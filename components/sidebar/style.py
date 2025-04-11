import streamlit as st


def style_css():
    st.markdown(
        """
        <style>
           
            [data-testid="stSidebarNav"] ul {
                padding: 10px;
            }
            [data-testid="stSidebarNav"] a {
                color: #ffffff !important;
                font-size: 16px;
                font-weight: bold;
                text-decoration: none;
            }
            [data-testid="stSidebarNav"] a:hover {
                color: #ffcc00 !important;
            }
            [data-testid="stSidebarNav"] { 
                display: none;  /* Esconde o menu padrão */
            }    
        </style>
        """,
        unsafe_allow_html=True
    )