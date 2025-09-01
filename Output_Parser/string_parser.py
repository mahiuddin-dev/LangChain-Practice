from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
load_dotenv()

model = ChatOpenAI(model="gpt-4o")


# Detail
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# prompt1 = template1.invoke({'topic': 'black hole'})
# result1 = model.invoke(prompt1)

# print("======================")
# print(result1.content)
# print("======================")

# Summary
template2 = PromptTemplate(
    template="Write a 5 lines summary on the following text. {text}",
    input_variables=["text"]
)
# prompt2 = template2.invoke({'text': result1.content})
# result2 = model.invoke(prompt2)

# print("======================")
# print(result2.content)
# print("======================")

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "Django"})
print(result)
