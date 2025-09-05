from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template="Give 3 fact about the {topic}\n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)


chain = template | model | parser
result = chain.invoke({"topic": "Black hole"})
print(result)


# Disadvantage
"""
    1. Data Validation 
"""