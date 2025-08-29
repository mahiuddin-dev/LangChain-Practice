from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('human', "You're a helpful {domain} expert"),
    ('system', "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "time out"
})
print(prompt)
