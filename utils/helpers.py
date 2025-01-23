import streamlit as st

def display_message(text, message_type="info"):
    if message_type == "info":
        st.info(text)
    elif message_type == "success":
        st.success(text)
    elif message_type == "error":
        st.error(text)
