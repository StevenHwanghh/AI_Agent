from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("你是一个乐于助人的助手。你的名字叫{name}"),
        HumanMessagePromptTemplate.from_template("我的问题是{question}")
    ]
)

formatted_prompt = chat_prompt.invoke(input={"name": "BOB", "question": "今天天气怎么样？"})
print(formatted_prompt)
print(type(formatted_prompt))