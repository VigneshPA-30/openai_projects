from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()   

embeddings = OpenAIEmbeddings() 


text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 200,
    chunk_overlap = 100
)

loader = TextLoader("facts.txt")
documents = loader.load_and_split(
    text_splitter = text_splitter
)

db = Chroma.from_documents(
    documents,
    embedding = embeddings,
    persist_directory = "emb"
)


results = db.similarity_search_with_score("fact about English language")

for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)