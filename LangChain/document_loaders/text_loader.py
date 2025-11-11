from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOpenAI(model="gpt-4o")
prompt = PromptTemplate(
    template="Write a summary for the following poem \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("./document_loaders/cricket.txt", encoding="utf-8")
docs = loader.load()

# print(docs)
# print(type(docs)) # List
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser
result = chain.invoke({"poem": docs[0].page_content})
print(result)
