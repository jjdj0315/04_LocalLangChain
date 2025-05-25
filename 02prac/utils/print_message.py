import streamlit as st


# 메시지 출력
def print_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)
