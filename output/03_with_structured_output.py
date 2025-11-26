from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

class PersonSummary(BaseModel):
    name: str = Field(..., description="The person's name")
    age: int = Field(..., description="The person's age")
    profession: str = Field(..., description="The person's profession")
    hobbies: list[str] = Field(..., description="A list of the person's hobbies")
    
llm  = ChatOllama(model="granite4:latest", max_tokens=256, temperature=0.7)
structured_llm = llm.with_structured_output(PersonSummary)

result = structured_llm.invoke("张三是一名软件工程师，今年35岁，喜欢爬山和摄影。")
print(result)
print(type(result)) 
