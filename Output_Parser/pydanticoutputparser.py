from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser, PydanticOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema   
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description='Name of the Person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}.',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

f_result = chain.invoke({'place':'Dubai'})

# prompt = template.invoke({'place':'Nepal'})

# result = model.invoke(prompt)

# f_result = parser.parse(result.content)

print(f_result)