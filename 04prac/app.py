import streamlit as st

from utils.session import session_control
from utils.create_dir import create_dir
<<<<<<< HEAD
session_control()
create_dir()

st.set_page_config(page_title="100% 오픈모델 RAG")
=======
from utils.upload import upload_file
from utils.create_rag_chain import create_rag_chain

session_control()
create_dir()

st.set_page_config(page_title="100% 오픈모델 RAG , made by DJ")
st.title("100% 오픈모델 RAG, by DJ")

with st.slider:
    file = st.file_uploader(
        "파일 업로드",
        type=["pdf"],
    )
    if file:
        file_path = upload_file(file)
        rag_chain = create_rag_chain(file_path)
        st.session_state["chain"] = rag_chain
>>>>>>> b2cdc3c26fa0b2696fd1be571a68332963ac5908
