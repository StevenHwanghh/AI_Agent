from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = JsonOutputParser()

llm  = ChatOllama(model="granite4:latest", max_tokens=256, temperature=0.7)

prompt = PromptTemplate(
    template = "请以JSON格式总结：{text} \n {format_instructions}",
    input_variables = ["text"],
    partial_variables = {"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

result = chain.invoke({"text": "张三是一名软件工程师，今年35岁，喜欢爬山和摄影。"})
print(result)
