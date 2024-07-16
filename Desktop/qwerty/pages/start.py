import streamlit as st

@st.experimental_dialog("이름과 학번")
def start():
    st.write(f"이름과 학번을 적어주십시오.")
    name = st.text_input("이름")
    num = st.text_input("학번")
    if st.button("Submit"):
        st.session_state.namnum = {"name": name, "num": num}
        st.rerun()
start()