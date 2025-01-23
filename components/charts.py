import streamlit as st
import matplotlib.pyplot as plt

def line_chart(data):
    fig, ax = plt.subplots()
    ax.plot(data["date"], data["value"])
    st.pyplot(fig)
