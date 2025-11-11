from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictonal person\n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# Without chain

prompt = template.format()
result = model.invoke(prompt)
print(result)
print("=" * 30)
final_result = parser.parse(result.content)
print(final_result)
print("=" * 30)
print(type(final_result))

# With Chain
chain = template | model | parser
result = chain.invoke({})
print(result)


# Disadvantage
"""
    1. Structured output
"""