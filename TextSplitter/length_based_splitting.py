from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

model = ChatAnthropic(model_name="claude-3-5-sonnet-20241022")
parser = StrOutputParser()

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(result)
