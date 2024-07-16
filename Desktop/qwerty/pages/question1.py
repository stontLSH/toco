import streamlit as st
st.markdown('1. 1+1의 값을 구해볼까요?')
st.button("1") 
if st.button("2"):
    st.session_state.one = "맞아요~ 답은 2였답니다~!"
else: st.session_state.one = "어린이 친구, 다시 한 번 생각해볼까요~?"
st.button("3")
st.button("4")
st.button("5")
