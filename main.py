import streamlit as st

st.title("My First Streamlit Application")

name = st.text_input("Enter your name:")

st.write(f"Hi {name}!")