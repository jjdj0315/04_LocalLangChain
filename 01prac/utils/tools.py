import streamlit as st
from langchain_core.messages import ChatMessage
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import load_prompt
from langchain_ollama import OllamaEmbeddings, ChatOllama


# 메시지 출력
def print_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)


# 메시지 추가
def add_message(role, content):
    st.session_state.messages.append(ChatMessage(role=role, content=content))


# 파일 업로드
def embed_file(file):
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    with open(file_path, "wb") as f:
        f.write(file_content)
    return file_path


# 문서 포맷팅
def format_docs(docs):
    return "\n\n".join(
        f"<document><content>{doc.page_content}</content><page>{doc.metadata['page']}</page><source>{doc.metadata['source']}</source></document>"
        for doc in docs
    )
    
    
# RAG 체인 생성
@st.cache_resource(show_spinner="파일을 처리중입니다. 잠시만 기다려주세요.")
def create_rag_chain(file_path):
    # Splitter 설정
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # 문서 로드
    loader = PDFPlumberLoader(file_path)
    docs = loader.load_and_split(text_splitter=text_splitter)

    # 캐싱을 지원하는 임베딩 설정
    cache_dir = LocalFileStore(f".cache/embeddings")
    EMBEDDING_MODEL = "bge-m3"
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
        embeddings, cache_dir, namespace=EMBEDDING_MODEL
    )

    # 벡터 DB 저장
    vectorstore = FAISS.from_documents(docs, embedding=cached_embeddings)

    # 문서 검색기 설정
    retriever = vectorstore.as_retriever()

    # 프롬프트 로드
    prompt = load_prompt("utils/prompts/rag-exaone.yaml", encoding="utf-8")

    # Ollama 모델 지정
    llm = ChatOllama(
        model="mistral",
        temperature=0,
    )

    # 체인 생성
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    add_message("assistant", "준비가 완료되었습니다. 무엇을 도와드릴까요?")
    return chain