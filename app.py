import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

load_dotenv()

# Initialize OpenAI LLM
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize embeddings
embeddings = HuggingFaceEmbeddings()

# Load the ChromaDB vector store
vectordb = Chroma(persist_directory="./chroma_store", embedding_function=embeddings)

# Create a RetrievalQA chain
rqa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectordb.as_retriever())

def query_docs(query):
    return rqa.run(query)

if __name__ == "__main__":
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        response = query_docs(query)
        print(f"Response: {response}")

