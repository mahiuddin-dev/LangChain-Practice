from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=1.5, max_completion_tokens=100)

template = PromptTemplate(
    template="Great this person in 5 language. The name of the person is {name}",
    input_variables=["names"],
    validate_template=True
)
user_name = input("Enter your name:")

prompt = template.invoke({
    "name": user_name
})

result = model.invoke(prompt)
print(result)
# For text response
print(result.content)
