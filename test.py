import streamlit as st

title = st.text_input('Movie title', '')
if st.button("submit"):
    st.write('The current movie title is', title)
