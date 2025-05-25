import os

import streamlit as st

from utils import tools

# 캐시 디렉토리 생성
if not os.path.exists(".cache"):
    os.mkdir(".cache")
if not os.path.exists(".cache/embeddings"):
    os.mkdir(".cache/embeddings")
if not os.path.exists(".cache/files"):
    os.mkdir(".cache/files")

# 메시지 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# 페이지 설정
st.set_page_config(page_title="100% 오픈모델 RAG", page_icon="💬")
st.title("100% 오픈모델 RAG")


with st.sidebar:
    file = st.file_uploader(
        "파일 업로드",
        type=["pdf"],
    )
    if file:
        file_path = tools.embed_file(file)
        rag_chain = tools.create_rag_chain(file_path)
        st.session_state["chain"] = rag_chain

# 메시지 출력
tools.print_messages()


if user_input := st.chat_input():

    if "chain" in st.session_state and st.session_state["chain"] is not None:
        chain = st.session_state["chain"]
        # 사용자의 입력
        st.chat_message("user").write(user_input)

        # 스트리밍 호출
        response = chain.stream(user_input)
        with st.chat_message("assistant"):
            # 빈 공간(컨테이너)을 만들어서, 여기에 토큰을 스트리밍 출력한다.
            container = st.empty()

            ai_answer = ""
            for token in response:
                ai_answer += token
                container.markdown(ai_answer)

        # 대화기록을 저장한다.
        tools.add_message("user", user_input)
        tools.add_message("assistant", ai_answer)
    else:
        st.write("파일을 업로드해주세요.")
