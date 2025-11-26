from langchain_ollama import ChatOllama

llm  = ChatOllama(model="granite4:latest"， max_tokens=256, temperature=0.7)

response = llm.invoke("Tell me something about ollama with one sentence.")
print(response.content)