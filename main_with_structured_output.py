from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from langchain_tavily import \
    TavilySearch  # TavilySearch 直接被包装为一个可以被LangChain使用的tool
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS

from schemas import AgentResponse

tools = [TavilySearch()]

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
structured_llm = llm.with_structured_output(AgentResponse)

react_prompt = hub.pull("hwchase17/react")

react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=[
        "tools",
        "tool_names",
        "format_instructions",
        "input",
        "agent_scratchpad",
    ],
    partial_variables={"format_instructions": ""},
)

agent = create_react_agent(llm, tools, prompt=react_prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
extract_output = RunnableLambda(lambda x: x["output"])


chain = agent_executor | extract_output | structured_llm


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
