from dotenv import load_dotenv
load_dotenv()  # Load envionment variable so LangSmit can trace it

from langchain_groq import ChatGroq
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# 直接提供字符串作为输入
response = model.invoke("你使用的是什么模型？")
print(response)
print(response.content)