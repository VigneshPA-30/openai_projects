from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from dotenv import load_dotenv
from queue import Queue
from threading import Thread


load_dotenv()


class StreamingHandler(BaseCallbackHandler):

    def __init__(self,queue):
        self.queue = queue
    def on_llm_new_token(self, token, **kwargs):
        self.queue.put(token)

    def on_llm_end(self,response,**kwargs):
        self.queue.put(None)

    def on_llm_error(self,error,**kwargs):
        self.queue.put(None)


llm = ChatOpenAI(streaming=True)

prompt = ChatPromptTemplate.from_messages([
    ("human","{content}")
])


class StreamableChain():
    def stream(self, input:dict[str,str]):

        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self.__call__(input, callbacks =[handler])

        my_thread=Thread(target=task)
        my_thread.start()

        while True:
            token = queue.get()
            if token is None:
                print("\n")
                break 
            yield token


class StreamableChain(StreamingChain,LLMChain):
    pass
    
        

chain = StreamingChain(llm=llm,prompt=prompt)

for output in chain.stream({"content":"Tell me a Joke in 200 words"}):
    print(output,end="")



