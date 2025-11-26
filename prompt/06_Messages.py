from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="granite4:latest")

system_msg = SystemMessage(content="You are a helpful assistant.")
human_msg = HumanMessage(content="Tell me what is ollama with a simple explanation")

messages = [system_msg, human_msg]

response = llm.invoke(messages)
print(response.content)