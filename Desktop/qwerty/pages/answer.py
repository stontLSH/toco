import streamlit as st
if "one" in st.session_state:
    st.write(st.session_state.one)
if "two" in st.session_state:
    st.write(st.session_state.two)
if "three" in st.session_state:
    st.write(st.session_state.three)