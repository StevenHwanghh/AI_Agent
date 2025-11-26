from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

llm  = ChatGroq(model="openai/gpt-oss-20b", temperature=1)

response = llm.invoke("什么是大模型")
print(type(response))

parser = StrOutputParser()
output = parser.invoke(response)
print(type(output))
print(output)