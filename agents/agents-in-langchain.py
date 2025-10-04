from langchain_openai import ChatOpenAI
from langchain.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv

# load env
load_dotenv()


search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('top news in us today')

# LLM model
llm = ChatOpenAI()

# hub pull from LangChain Hub
prompt = hub.pull("hwchase17/react")

# Create the agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Wrap the agent in an executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# Invoke
response = agent_executor.invoke({"input": "What is the latest news in the US?"})
print(response)
print(response["output"])
