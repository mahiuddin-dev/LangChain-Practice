from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
# load chat history
with open('./Prompt/Chat/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

# create prompt
# prompt = chat_template.invoke({
#     "chat_history": chat_history,
#     "query": 'Where is my refund'
# })

model = ChatOpenAI(model="gpt-4o", temperature=1.0, max_completion_tokens=100)
# response = model.invoke(prompt)
# print(response.response_metadata)
# print(response.content)

chain = chat_template | model
chain_response = chain.invoke({
    "chat_history": chat_history,
    "query": 'Where is my refund'
})

print(chain_response.content)
