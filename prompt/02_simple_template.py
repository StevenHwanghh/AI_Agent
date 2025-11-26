from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm  = ChatGroq(model="openai/gpt-oss-20b", temperature=1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things in Chinese."),
    ("user", "{question}") 
])

chain = prompt | llm

response = chain.invoke({"question": "什么是大模型"})
print(response)