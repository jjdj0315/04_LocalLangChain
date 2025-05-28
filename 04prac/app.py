import streamlit as st

from utils.session import session_control
from utils.create_dir import create_dir
session_control()
create_dir()

st.set_page_config(page_title="100% 오픈모델 RAG")