from langchain_core.prompts import ChatPromptTemplate

# 通过实例化对象的方式创建
chat_prompt = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant, you name is {name}"),
        ("user", "How are you today? {user_input}")
    ],
    input_variables=["name", "user_input"]     # 1.0版本中该参数为可选
)

final_chat_prompt = chat_prompt.invoke(input={
    "name": "Bob",
    "user_input": "What's your name?"
})

final_chat_prompt = chat_prompt.format(name="Bob",user_input="What's your name?")

final_chat_prompt = chat_prompt.format_messages(name="Bob",user_input="What's your name?")

final_chat_prompt = chat_prompt.format_prompt(name="Bob",user_input="What's your name?")


print(final_chat_prompt)
print(type(final_chat_prompt))

# 通可以简化如下
chat_prompt1 = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant, you name is {name}"),
        ("user", "How are you today? {user_input}")
    ]
)

final_chat_prompt1 = chat_prompt1.invoke({
    "name": "Bob",
    "user_input": "What's your name?"
})

print(final_chat_prompt1)
print(type(final_chat_prompt1))

# 通过类方法from_messages来创建ChatPromptTemplat对象
chat_prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, you name is {name}"),
        ("user", "How are you today? {user_input}")
    ]
)

final_chat_prompt2 = chat_prompt2.invoke({
    "name": "Bob",
    "user_input": "What's your name?"
})

final_chat_prompt3 = final_chat_prompt2.to_messages()
print(final_chat_prompt3)
print(type(final_chat_prompt3))

final_chat_prompt4 = final_chat_prompt2.to_string()
print(final_chat_prompt4)
print(type(final_chat_prompt4))