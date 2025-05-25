import streamlit as st
from langchain_core.messages import ChatMessage


# 메시지 추가
def add_message(role, content):
    st.session_state.messages.append(ChatMessage(role=role, content=content))
