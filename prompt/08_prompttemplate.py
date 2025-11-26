from langchain_core.prompts import PromptTemplate

# 通过实例创建，input_variables 和 template 参数都是必须的
prompt_template = PromptTemplate(
    input_variables=["role", "topic"],
    template="你是一个知识丰富的{role}，请告诉我关于{topic}的更多信息。"
)

# 通过format方法生成最终的提示
final_prompt = prompt_template.format(role="AI专家", topic="Agent")

print(final_prompt)


# 通过类方法 from_template 创建 PromptTemplate 实例
prompt_template2 = PromptTemplate.from_template(template="你是一个知识丰富的{role}，请告诉我关于{topic}的更多信息。")

# 通过format方法生成最终的提示
final_prompt2 = prompt_template2.format(role="AI专家", topic="Agent")

print(final_prompt2)

# 定义提示词文本
prompt_text = """
你是一个专业的Symphony技术支持专家，能够解决各种复杂的问题。
"""

prompt_template3 = PromptTemplate.from_template(template=prompt_text.strip())
final_prompt3 = prompt_template3.format()
print(final_prompt3)

print(prompt_template3)