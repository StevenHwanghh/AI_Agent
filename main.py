from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

def main():
    print("Hello from langchain-course!")
    
    prompt = PromptTemplate.from_template("Say hello to {name}!")
    
    chat = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

    parser = StrOutputParser()

    chain = prompt | chat | parser

    response = chain.invoke({"name": "LangChain"})
    
    print(response)


if __name__ == "__main__":
    main()
