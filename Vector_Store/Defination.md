# A vector store is a system designed to store and retrieve data represented as numerical vectors.

## Key Features:

Storage: Ensures that vectors and their associated metadata are retained, whether in memory for quick lookups or on disk for durability and large scale use.
Similarity Search : Helps retrives the vectors most similar to a query vector.
Indexing: Provide a data structure or method that enables fast similarity searches on high dimensional vectors.(e.g. approximate nearest neighobor lookups).
CRUD: Manage the lifecycle of data- adding new vector, reading them, updating existing entries, removing outdated vectors.

Use Case:

Semantic search
RAG
Recommender Systems
Image/Multimedia search



### Vector store vs Vector Database

# Vector Store:

Vector store is a system which gives us storage option and retrival service. Eg the library of facebook(FAISS)

# Vector Database

Apart from all the facilities of vector store it also provides advanced features like indexing, querying, filtering, and analyzing vectors efficiently. Eg. Pinecone,Milvus

*** All vector database is a vector store but vice versa is not true.

## Chroma is a light weight, open-source vector database that is especially friendly for local development and small to medium scale production needs.

