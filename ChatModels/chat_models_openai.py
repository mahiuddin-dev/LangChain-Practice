from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load env
load_dotenv()

# Model inital
model = ChatOpenAI(model="gpt-4o", temperature=0.5, max_completion_tokens=10)
# Response
response = model.invoke("Write about langchain?")
print(response) #Json data
"""
    content='LangChain is an innovative framework designed specifically for building' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 11, 'total_tokens': 21, .......}
"""
# Actual response
print(response.content)
