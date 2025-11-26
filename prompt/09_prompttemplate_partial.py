from langchain_core.prompts import PromptTemplate

# 通过实例创建，input_variables 和 template 参数都是必须的
prompt_template1 = PromptTemplate(
    input_variables=["role", "topic"],
    template="你是一个知识丰富的{role}，请告诉我关于{topic}的更多信息。",
    partial_variables={"role": "AI专家"}             # 参数是一个dict对象，变量名：变量值
)

# 通过format方法生成最终的提示
final_prompt1 = prompt_template1.format(topic="Agent")    # 只需要传入未被部分填充的变量
print(final_prompt1)


# 通过类方法 from_template 创建 PromptTemplate 实例
prompt_template2 = PromptTemplate.from_template(
    template="你是一个知识丰富的{role}，请告诉我关于{topic}的更多信息。",
    partial_variables={"role": "AI专家"}             # 参数是一个dict对象，变量名：变量值
)

# 通过format方法生成最终的提示
final_prompt2 = prompt_template2.format(topic="Agent")

print(final_prompt2)

# 定义提示词文本
prompt_text = """
你是一个专业的{role}，能够解决{topic}的问题。
"""

prompt_template3 = PromptTemplate.from_template(template=prompt_text.strip())
prompt_template4 = prompt_template3.partial(role="Symphony技术支持专家")
final_prompt4 = prompt_template4.format(topic="各种复杂")
print(final_prompt4)


prompt_template5  = PromptTemplate.from_template(template = "tell me a joke about {topic}") + ". make it funny"
final_prompt5 = prompt_template5.format(topic="chickens")
print(final_prompt5)


prompt_template6 = PromptTemplate.from_template(template="你是一个专业的{role}，能够解决{topic}的问题")
final_prompt6 = prompt_template6.invoke(input = {"role": "Symphony技术支持专家", "topic": "各种复杂"})
print(final_prompt6)