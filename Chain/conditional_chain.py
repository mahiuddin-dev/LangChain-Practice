from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()


model = ChatAnthropic(model_name="claude-3-5-sonnet-20241022")
# model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Feedback sentiment.")

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative\n {text}\n {format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": pydantic_parser.get_format_instructions()}
)


classification_chain = prompt1 | model | pydantic_parser


prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback. Don't write any over. Just response customer feedback. \n {feedback}",
    input_variables=["feedback"]
)


# RunnableBranch for if else condition
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)


chain = classification_chain | branch_chain
result = chain.invoke({"text": "this is a good phone"})
print(result)
