from langchain_community.document_loaders import WebBaseLoader

url = "https://signal.nfx.com/investor-lists/top-agtech-series-a-investors"
loader = WebBaseLoader(url)
docs = loader.load()
print(docs)
# print(len(docs))
# print(docs[0].page_content)
