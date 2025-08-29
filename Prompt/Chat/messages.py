from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=1.0, max_completion_tokens=100)

# messages
messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
