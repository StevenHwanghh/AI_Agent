from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm  = ChatGroq(model="openai/gpt-oss-20b", temperature=1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things in Chinese."),
    ("user", "{question}") 
])

outputparser = JsonOutputParser()

chain = prompt | llm | outputparser

response = chain.invoke({"question": "什么是大模型? 请用JSON格式回答，问题用question，回到用answer"})
print(response)