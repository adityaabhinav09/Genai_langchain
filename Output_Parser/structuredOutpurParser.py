from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema   
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = 'fact1',description='Fact 1 about the topic'),
    ResponseSchema(name = 'fact2',description='Fact 2 about the topic'),
    ResponseSchema(name = 'fact3',description='Fact 3 about the topic'),
    ResponseSchema(name = 'fact4',description='Fact 4 about the topic'),
    ResponseSchema(name = 'fact5',description='Fact 5 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template= "You are a helpful assistant. Please provide 5 facts about {topic} in the following JSON format:\n {format_instruction}\n Make sure the JSON is valid and does not include any extra text.",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'India'})

print(result)