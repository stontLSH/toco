import streamlit as st
st.markdown('2. 2x2의 값을 구해볼까요?')
st.button("1") 
st.button("2")
st.button("3")
if st.button("4"):
    st.session_state.two = "맞아요~ 답은 4였답니다~!"
else: st.session_state.two = "어린이 친구, 다시 한 번 생각해볼까요~?"
st.button("5")