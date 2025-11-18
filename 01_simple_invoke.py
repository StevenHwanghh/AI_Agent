from langchain_groq import ChatGroq

llm  = ChatGroq(model="openai/gpt-oss-20b", temperature=1)

response = llm.invoke("什么是大模型")
print(response)