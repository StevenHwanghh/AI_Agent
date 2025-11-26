from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个乐于助人的助手。你的名字叫{name}"),
        MessagesPlaceholder(variable_name="messages"),
        ("user", "我的问题是{question}")
    ]
)

formatted_prompt = chat_prompt.invoke(input={
    "name": "BOB", 
    "messages": [("user", "今天天气怎么样？")],
    "question": "今天天气怎么样？"
    })
print(formatted_prompt)
print(type(formatted_prompt))