from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory
from langchain.prompts import MessagesPlaceholder,HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="message",
    return_messages=True
    )


prompt = ChatPromptTemplate(
    input_variables = ["content","message"],
    messages=[
        MessagesPlaceholder(variable_name="message"),
        HumanMessagePromptTemplate.from_template("{content}")]
)

chain = LLMChain(
    llm=llm,
    prompt = prompt,
    memory=memory
)

while True:
    user_input = input(">>  ")
    result = chain({"content":user_input})
    print(result["text"])

