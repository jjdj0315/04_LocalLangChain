import os

<<<<<<< HEAD
def create_dir():
    # 캐시 디렉토리 생성
    if not os.path.exists(".cache"):
        os.mkdir(".cache")
    if not os.path.exists(".cache/embeddings"):
        os.mkdir(".cache/embeddings")
=======

def create_dir():
    if not os.path.exists(".cache"):
        os.mkdir(".cache")

    if not os.path.exists(".cache/embeddings"):
        os.mkdir(".cache/embeddings")

>>>>>>> b2cdc3c26fa0b2696fd1be571a68332963ac5908
    if not os.path.exists(".cache/files"):
        os.mkdir(".cache/files")
