
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

## Length based Text Splitting

# We upfront decide what will be the size of our chuncks.

loader = PyPDFLoader('../statistics 1001.pdf')              
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)
print(result[2])
