from langchain_ollama import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

embeddings  = OllamaEmbeddings(model="granite-embedding:30m")

texts = [
    "Ollama is running locally on my machine.",
    "LangChain makes it easy to swap LLM backends."
]

# Get embeddings for multiple texts
vectors = embeddings.embed_documents(texts)

print(len(vectors), "vectors")      # 2
print(len(vectors[0]), "dims")      # embedding dimension