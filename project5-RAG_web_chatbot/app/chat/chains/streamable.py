from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler
from flask import current_app


class StreamableChain():
    def stream(self, input:dict[str,str]):

        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self.__call__(input, callbacks =[handler])

        my_thread=Thread(target=task, args = [current_app.app_context()])
        my_thread.start()

        while True:
            token = queue.get()
            if token is None:
                print("\n")
                break 
            yield token

