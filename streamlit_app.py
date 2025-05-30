import streamlit as st

st.title("간단한 스틀림릿 웹 앱")
user_input = st.text_input("메시지를ㄹ 입력하세요")
if user_input:
    st.write(f"입력하신 메시지: {user_input}")
