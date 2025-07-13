
import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Function to process and load documents
def ingest_documents():
    # Load documents from the data directory
    documents = []
    for filename in os.listdir("data"):
        filepath = os.path.join("data", filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
            documents.extend(loader.load())
        elif filename.endswith(".txt"):
            loader = TextLoader(filepath)
            documents.extend(loader.load())

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings()

    # Create and persist the ChromaDB vector store
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory="./chroma_store")
    vectordb.persist()

if __name__ == "__main__":
    ingest_documents()
    print("Documents ingested successfully!")


