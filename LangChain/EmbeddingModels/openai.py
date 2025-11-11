from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
response = embedding.embed_query("Tell me something about python")
print("=============== Text ============")
print(response)

print("=============== Str ==========")
print(str(response))


documents = [
    "Python",
    "HTML",
    "JavaScript",
]
response = embedding.embed_documents(documents)
print("=============== Documents ============")
print(response)
print("=============== Str ==========")
print(str(response))
