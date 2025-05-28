import os

def create_dir():
    # 캐시 디렉토리 생성
    if not os.path.exists(".cache"):
        os.mkdir(".cache")
    if not os.path.exists(".cache/embeddings"):
        os.mkdir(".cache/embeddings")
    if not os.path.exists(".cache/files"):
        os.mkdir(".cache/files")
