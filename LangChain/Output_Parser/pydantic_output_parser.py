from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import json
load_dotenv()

"""
Why use PaydanticOutputParser
1. Strict schema Enforcement
2. Ensure type safety
3. Easy validation
4. Seamless integration
"""

model = ChatOpenAI(model="gpt-4o")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age : int = Field(gt=18, description="Age of the person")
    city : str = Field(description="City name of the city person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person\n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"place": "Bangladeshi"})

print(result.model_dump())