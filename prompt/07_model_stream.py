from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="granite4:latest", stream=True)   # Add stream=True for streaming responses

system_msg = SystemMessage(content="You are a helpful assistant.")
human_msg = HumanMessage(content="Tell me about LSF in IBM Platform Spectrum computing")

messages = [system_msg, human_msg]

# response = llm.invoke(messages)
# print(response.content)

print("流式输出开始")

for chunk in llm.stream(messages):
    print(chunk.content, end='', flush=True)  # Print each chunk as it arrives

print("流式输出结束")