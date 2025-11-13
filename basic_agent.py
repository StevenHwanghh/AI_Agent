from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
# from tavily import TavilyClient           # First version I used to search by myself
from langchain_tavily import TavilySearch   # Second verion that integrates Tavily with LangChain

load_dotenv()  # Load environment variables from a .env file if present

# Below part I used TavilyClient in my search tool
# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """Searches over Internet for weather info.
#      Args:
#          query (str): The search query.
#      Returns:
#          str: The search results.
#      """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)

# This time I use TavilySearch from langchain_tavily directly
search = TavilySearch()

# Built up agent with Groq model and search tool
model = ChatGroq(model="openai/gpt-oss-120b", temperature=1)
tools = [search]
agent = create_agent(model=model, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for AI Engineer job posting in Markham, Ontario")})
    print("Agent Result:", result)
    


if __name__ == "__main__":
    main()
