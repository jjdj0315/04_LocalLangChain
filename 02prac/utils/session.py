import streamlit as st


def session_control():
    # 메시지 초기화
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
