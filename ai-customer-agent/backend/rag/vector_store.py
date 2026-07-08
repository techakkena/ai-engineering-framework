from dotenv import load_dotenv
import os

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("VECTOR STORE KEY FOUND:", bool(OPENAI_API_KEY))

embeddings = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY
)

VECTOR_PATH = "vector_db"


def create_or_update_vector_store(chunks):

    if os.path.exists(VECTOR_PATH):

        db = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_documents(chunks)

    else:

        db = FAISS.from_documents(
            chunks,
            embeddings
        )

    db.save_local(VECTOR_PATH)

    return db


def load_vector_store():

    db = FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db