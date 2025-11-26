from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

# llm  = ChatOllama(model="granite4:latest", max_tokens=256, temperature=0, verbose=True)
llm  = ChatGroq(model="openai/gpt-oss-20b", temperature=1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You name is StevenAI"),
    ("user", "{question}")
])

while True:
    user_input = input("会话输入('exit' 退出): ")
    if user_input.lower() == 'exit':
        break
    
    chain = prompt | llm
    response = chain.invoke({"question": user_input})
    print(f"模型回复: {response.content}")
    
    prompt.messages.append(HumanMessage(content=user_input))    
    prompt.messages.append(AIMessage(content=response.content))
    
    print(prompt.messages)
    print("---- Start New Turn ----")

    