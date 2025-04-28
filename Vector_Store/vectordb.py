from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma

doc1 = Document(
    page_content="Virat Kohli is India batsman who is also known as king kohli and known for his classical batting shots.",
    metadata={"team":"Royal challenger Bangalore"}
)
doc2 = Document(
    page_content="Rohit Sharma is a India batsman known for his big hits.",
    metadata = {"team":"Mumbai Indians"}
)
doc3 = Document(
    page_content="Bumrah is Indian fast bowler known for his death over bowlings and yorkers",
    metadata = {"team": "Pune Warriers"}
)
doc4 = Document(
    page_content="MS Dhoni is a Indian Batsman and a fabulous captain of India team and has lead to win a lot of trophies for Indian team.",
    metadata = {"team":"Chennai Super kings"}
)

docs = [doc1,doc2,doc3,doc4]

# vector_store = Chroma(
#     embedding_function=OpenAIEmbeddings(),
#     collection_metadata='sample',
#     persist_directory='my_chroma_db'
# ) 

# print(vector_store.add_documents(docs))

# # view documents

# print(vector_store.get(include=['embeddings','documents','metadatas']))

print(docs)
































