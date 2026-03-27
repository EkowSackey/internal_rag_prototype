# Internal RAG Prototype

A proof of concept codebase for an internal company knowledge-sharing platform. This prototype leverages [Agentset](https://agentset.com/) as a RAG-as-a-Service platform.

## Setup Instructions

1. **Clone the repository and open the project.**
2. **Navigate to the `agentset_version` directory:**
   ```bash
   cd agentset_version
   ```
3. **Set up a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
4. **Set up the environment variables:**
   - Copy the `.env.example` file to create a `.env` file:
     ```bash
     cp .env.example .env
     ```
   - Make sure to update `.env` with your actual `NAMESPEACE_ID`, `AGENTSET_TOKEN`, and `OPENAI_API_KEY`.

## Usage

The project is split into three main python scripts that demonstrate the full lifecycle of a document within the RAG platform:

1. **Upload Documents (`uploader.py`)**
   Demonstrates how to upload a local PDF file (e.g., `cleancode.pdf`) to Agentset and trigger the ingest job for embedding and indexing.
   ```bash
   python uploader.py
   ```

2. **Search Documents (`search.py`)**
   Executes a semantic search query against the ingested knowledge to retrieve top relevant text chunks.
   ```bash
   python search.py
   ```

3. **Generate Responses (`generate.py`)**
   Combines the Agentset search capability with OpenAI's GPT models. It fetches contextually relevant chunks from the database and uses them as context for the language model to generate an intelligent response.
   ```bash
   python generate.py
   ```