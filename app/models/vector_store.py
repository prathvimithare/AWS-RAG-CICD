import chromadb
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

class VectorStore:
    def __init__(self, path, ollama_host: str):
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url=ollama_host
        )
        self.vector_store = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)