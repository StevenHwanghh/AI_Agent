from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

def main():
    
    information = """
    IBM Cloud Pak for Data is a set of services on IBM Software Hub that accomplishes all your data governance, data engineering, data analysis, and AI lifecycle tasks. Cloud Pak for Data implements a data fabric solution so that you can provide instant and secure access to trusted data to your organization, automate processes and compliance, and deliver trustworthy AI in your applications.
    A data fabric architecture implements active metadata management to automate metadata processing with AI. The outcomes of the metadata analysis facilitate automated data discovery, improve confidence in data, and enable data protection and data governance at scale.
    Cloud Pak for Data provides integrated tools for your organization to work with your data to improve your business. Your data engineers need tools to manage, prepare, integrate, and virtualize data. Your data quality analysts need tools to measure the quality of the data. Your governance team needs tools to control, protect, and enrich your data. Your data consumers, such as business analysts and data scientists, need tools to collaboratively develop insights and models.
    """
    
    summary_template = """
    Give the information {information} about the IBM Cloud Pak for Data, I want you to provide a concise summary:
    1. A short summary of the main points.
    2. Key features and benefits.
    """

    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)

    chat = ChatOllama(model="gemma3:270m", temperature=0)

    parser = StrOutputParser()

    chain = summary_prompt | chat | parser

    response = chain.invoke(input={"information": information})
    
    print(response)


if __name__ == "__main__":
    main()
