
# Risk Whisperer

A Python-based application that uses LangChain, ChromaDB, and a Large Language Model (LLM) to answer questions about your risk documents.

## Architecture

![Architecture Diagram](https://private-us-east-1.manuscdn.com/sessionFile/VH2NyIlOQb46o11Gt8nYsT/sandbox/z9a1W8IHiELSMvDEUqg0Cd-images_1752441024469_na1fn_L2hvbWUvdWJ1bnR1L3Jpc2tfd2hpc3BlcmVyL2FyY2hpdGVjdHVyZV9kaWFncmFt.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvVkgyTnlJbE9RYjQ2bzExR3Q4bllzVC9zYW5kYm94L3o5YTFXOElIaUVMU012REVVcWcwQ2QtaW1hZ2VzXzE3NTI0NDEwMjQ0NjlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSnBjMnRmZDJocGMzQmxjbVZ5TDJGeVkyaHBkR1ZqZEhWeVpWOWthV0ZuY21GdC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=nI9LtVaXGYnarZLB-RjpBbcJHiHRkPVatwGSE3IjAMiofonHVUAh4YxTvVkUAW8nsZlR1LOwaWtJDXOoZdVc6Eq1ourpe-2NPm2mmVHw5umpZ0yFUay4ptktfWRWQUs4xnCE2F12fcDx-vTJA-JyfwYIsM~U98N3vOuMnxGlB~yPzOyS3UTWDw48CaqVym1yswHvba3eGy9ITug2u~UzJ~Zxu559oYs94Bn3cAYvvDhJtCSgT8EIXrYEsv7u2y~oO30m78Yswp8xvySf6XZu60fbFN9xt8N-Rox1q50cbTn6GO9o8Wihtc~5jiOd~FulVVtn9fA0UxEo0pOCfqZqiA__)

## Features

*   **Document Ingestion:** Supports both PDF and TXT file formats.
*   **Vector Store:** Uses ChromaDB to store document embeddings.
*   **LLM Integration:** Leverages a Large Language Model (LLM) to provide answers to your questions.
*   **User Interface:** Includes both a command-line interface (CLI) and a Gradio-based web interface.

## Getting Started

### Prerequisites

*   Python 3.7+
*   An OpenAI API key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd risk_whisperer
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**

    Create a `.env` file in the root of the project and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your-openai-api-key"
    ```

### Usage

1.  **Add your risk documents:**

    Place your PDF and TXT files in the `data` directory.

2.  **Ingest the documents:**

    ```bash
    python ingest_docs.py
    ```

3.  **Run the application:**

    *   **CLI:**
        ```bash
        python app.py
        ```
    *   **Gradio Web UI:**
        ```bash
        python app_gradio.py
        ```

## How it Works

1.  **Document Ingestion:** The `ingest_docs.py` script reads your documents, splits them into chunks, and creates embeddings for each chunk using a Hugging Face sentence transformer.
2.  **Vector Store:** The embeddings are stored in a ChromaDB vector store, which allows for efficient similarity searches.
3.  **Querying:** When you ask a question, the application retrieves the most relevant document chunks from the vector store and passes them to the LLM, along with your question.
4.  **Response:** The LLM generates a response based on the provided context, which is then displayed to you.


