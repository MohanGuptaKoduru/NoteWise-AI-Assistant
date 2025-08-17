from smolagents import tool
from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.llms.mistralai import MistralAI
import os
from keys import RunningApiKey

def Loading():
    reader = SimpleDirectoryReader(input_files=['mynotes.md'])
    documents = reader.load_data()
    return documents

def Storing():
    db = chromadb.PersistentClient(path="./vector_embeddings")
    chroma_collection = db.get_or_create_collection("notes")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    return vector_store

def Transformations(documents, vector_store):
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_overlap=0),
            HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        ],
        vector_store=vector_store
    )
    pipeline.run(documents=documents)
    return vector_store

def Indexing(vector_store):
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)
    return index

print("Loading your notes...")
embeddings = Loading()
vectorstore = Storing()
propvect = Transformations(embeddings, vectorstore)
index = Indexing(propvect)
print("Notes loaded!")

@tool
def search_my_notes(query: str) -> str:
    """
    Search through my personal notes to find relevant information about a topic.

    Args:
        query (str): The search query used to find relevant information from your notes.

    Returns:
        str: A string containing the summarized relevant information from your notes.
    """
    RunningApiKey()
    llm = MistralAI(
        api_key=os.environ["MISTRAL_API_KEY"],
        model="mistral-large-latest"
    )
    query_engine = index.as_query_engine(
        llm=llm,
        response_mode="tree_summarize"
    )
    response = query_engine.query(query)
    return str(response)
