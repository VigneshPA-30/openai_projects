import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

# Initialize Pinecone with error handling
try:
    pinecone_client = pinecone.Pinecone(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV_NAME")
    )
    
    # Get the index name from environment
    index_name = os.getenv("PINECONE_INDEX_NAME")
    if not index_name:
        raise ValueError("PINECONE_INDEX_NAME environment variable is not set")
    
    # Initialize vector store with the index
    vector_store = Pinecone.from_existing_index(
        index_name=index_name,
        embedding=embeddings,
        text_key="text"  # The key that will contain the text in metadata
    )

    def build_retriever(chat_args,k):
        search_kwargs = {
            "filter":{"pdf_id":chat_args.pdf_id},
            "k":k
        }
        return vector_store.as_retriever(
            search_kwargs=search_kwargs
        )
    
except Exception as e:
    print(f"Error initializing Pinecone: {str(e)}")
    raise