import os

from rag.document_registry import save_document
from rag.pdf_loader import load_pdf, split_docs
from rag.vector_store import create_or_update_vector_store


def process_pdf(pdf_path):

    docs = load_pdf(pdf_path)
    for doc in docs:
        doc.metadata["source"] = os.path.basename(pdf_path)

    chunks = split_docs(docs)

    create_or_update_vector_store(chunks)

    save_document(pdf_path, len(chunks))

    return len(chunks)
