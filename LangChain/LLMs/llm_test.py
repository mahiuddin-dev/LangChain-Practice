from langchain_openai import OpenAI
from dotenv import load_dotenv

# load env
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
# String input and output will be string
response = llm.invoke("What is the capital of bangladesh?")
print(response)
