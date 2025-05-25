import streamlit as st

from utils.session import session_control
from utils.create_dir import create_dir
from utils.upload import embed_file

session_control()
create_dir()

st.set_page_config(page_title="100% 오픈모델 RAG")
st.title("100%오픈모델RAG")

with st.sidebar:
    file = st.file_uploader("파일 업로드", type=["pdf"])
    if file:
        file_path = embed_file(file)
