from models import general_llm, chat_openai, chat_groq
response = general_llm.invoke("用三句话解释什么是大模型")
print(response.content)