from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from dotenv import load_dotenv
from tools.sql import run_query_tool,list_all_tables
from handler.chat_model_start_handler import ChatModelStartHandler
from tools.report import write_report_tool
import warnings




warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

handler = ChatModelStartHandler()
llm = ChatOpenAI(
    callbacks = [handler]
)

tools =[
    run_query_tool,
    write_report_tool
]

all_tables= list_all_tables()


prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content =f"You are an AI assistant who have access to sqlite3 database"
                           f"Available Tables : {all_tables}"
                           f"Use tool write_report_tool whenver someone asks for report"
                           f"Use PRAGMA query and call the run_query_tool when you don't know the columns in a table. Do not assume anything"),
    MessagesPlaceholder(variable_name="chat_history"),                       
    HumanMessagePromptTemplate.from_template("{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)

agent =  OpenAIFunctionsAgent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_executor=AgentExecutor(
    agent = agent,
    #verbose = True,
    tools=tools,
    memory=memory
)


if __name__ == "__main__":

    result = agent_executor.run("Write a Report on top 5 least used products with their names")
    print(result)
    print("#################################")
    result = agent_executor.run("Write a Report on top 5 most used products with their names")
    print(result)