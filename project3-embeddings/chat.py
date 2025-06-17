from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
import warnings
import langchain

langchain.debug=True


warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

llm = ChatOpenAI()

embeddings = OpenAIEmbeddings()
db = Chroma(
    embedding_function = embeddings,
    persist_directory = "emb"
)

retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm = llm,
    retriever = retriever,
    chain_type = "stuff"
)

result = chain.run("2 interesting facsts about English")

print(result)


