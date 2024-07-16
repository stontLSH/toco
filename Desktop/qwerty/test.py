import streamlit as st

st.title('이 사이트는 정말 신기하다')
st.markdown('*기울이기*도있고 **굵게하기**도 있으며 ***굵게하고 기울이기***도 있다.')
st.markdown(''':rainbow[무지개색도 삽가능, ] :blue-background[하이라이트 효과]도 있는데다가, ''')

_LOREM_IPSUM = """
이렇게 하면 글자도 겁나 신기하게 하나씩 쫘르륵 나온다. 와 개쩔죠???????????????????
"""
import time
def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.1)

if st.button("Stream data"):
    st.write_stream(stream_data)
st.title('제목')
st.header('부제목')
st.subheader('부부제목?')
st.caption('이건 뭐야 약간 이스터에그 같이 숨겨놓는 역할을 하면 되는 것 같다')

code = '''
    #include <stdio.h>
    int main(){
        printf("Warning");
        printf("u r fat");
    }
'''
st.code(code, language='c')

