# PyPDF Loader mainly use for text load

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

loader = PyPDFLoader("./document_loaders/dl-curriculum.pdf")
docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)
