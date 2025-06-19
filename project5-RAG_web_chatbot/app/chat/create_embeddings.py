from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    """
    Generate and store embeddings for the given pdf

    1. Extract text from the specified PDF.
    2. Divide the extracted text into manageable chunks.
    3. Generate an embedding for each chunk.
    4. Persist the generated embeddings.

    :param pdf_id: The unique identifier for the PDF.
    :param pdf_path: The file path to the PDF.

    Example Usage:

    create_embeddings_for_pdf('123456', '/path/to/pdf')
    """
    try:
        logger.info(f"Starting embedding creation for PDF {pdf_id}")
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        loader = PyPDFLoader(pdf_path)
        docs = loader.load_and_split(text_splitter)
        
        # Add metadata to each document
        for doc in docs:
            doc.metadata.update({
                "pdf_id": pdf_id
            })
        
        logger.info(f"Adding {len(docs)} documents to vector store")
        vector_store.add_documents(docs)
        logger.info(f"Successfully created embeddings for PDF {pdf_id}")
        
    except Exception as e:
        logger.error(f"Error creating embeddings for PDF {pdf_id}: {str(e)}")
        raise



