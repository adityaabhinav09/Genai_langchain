from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain import chains
from dotenv import load_dotenv

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)
parser = JsonOutputParser()
template = PromptTemplate(
    template='Give 5 fact about Sambhaji Maharaj \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result['name'])
# print(type(final_result))

# We can use chains to remove the above commented code

chain = template | model | parser
result = chain.invoke({})
print(result)


###################################### WE CANNOT ENFORCE SCHEMA IN JSONOUTPUTPARSER LIKE IF WE WANT THAT EACH FACT SHOULD BE KEY AND THERE IS A VALUE FOR IT ########## WE NEED TO USE DIFFERNT PARSER FOR ENFORCING SCHEMA ###