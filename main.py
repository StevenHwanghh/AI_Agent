from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_groq import ChatGroq
from langchain_tavily import \
    TavilySearch  # TavilySearch 直接被包装为一个可以被LangChain使用的tool

tools = [TavilySearch()]
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=1)
# llm = ChatOllama(model="gemma3:270m", temperature=1)
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt=react_prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        input={
            "input": "Search for 3 job postings for ai engineer using langchain in the Toronto area and list their details"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
