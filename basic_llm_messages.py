from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma3:270m", temperature=0)

# 使用提示词模板
# 通过一个messsages列表来创建提示词模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个有帮助的助手。请对我的问题尽量用要点清单方式进行回答"),
        ("user", "请解释一下{topic}。"),
    ]
)

# 1.
# 通过format_messages方法来格式化消息,该方法接受下面的这种可变命名参数列表。
# prompt_value = prompt.format_messages(topic="量子计算")
# response = model.invoke(prompt_value)      # 模型调用方法，invoke方法接受一个list of messages
# print(response.content)

# 2.
# 使用Chain来调用，直接使用LCEL语法顶一个chain
# chain = prompt | model
# response = chain.invoke({"topic": "量子计算"})
# print(response.content)


# 3. 使用输出解析器。这里使用了最简单的string输出解析器
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
chain = prompt | model | output_parser
response = chain.invoke({"topic": "量子计算"})
print(response)  # 因为已经使用了输出解析器，所以response是一个字符串。
