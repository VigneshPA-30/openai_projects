from app.chat.models import ChatArgs
from app.chat.vector_stores import retriever_map
from app.chat.llms import llm_map
from langchain.chat_models import ChatOpenAI
from app.chat.memories import memory_map
from app.chat.score import random_component_by_score
import random
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from app.web.api import (
    get_conversation_components,
    set_conversation_components
)



def select_components(
    component_type, component_map, chat_args):

    components = get_conversation_components(
        chat_args.conversation_id
    )

    previous_component = components[component_type]

    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else:
        random_name = random_component_by_score(component_type,component_map)
        builder = component_map[random_name]
        return random_name, builder(chat_args)



def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """

    retriever_name, retriever = select_components(
        "retriever",
        retriever_map,
        chat_args
    )

    llm_name, llm = select_components(
        "llm",
        llm_map,
        chat_args
    )

    memory_name, memory = select_components(
        "memory",
        memory_map,
        chat_args
    )

    print(
        f"Running chain with Memory - {memory_name}, Retriever - {retriever_name}, LLM name - {llm_name}"
    )

    set_conversation_components(
        chat_args.conversation_id,
        retriever=retriever_name,
        llm=llm_name,
        memory=memory_name
    )
  
    condensed_llm = ChatOpenAI(streaming=False)  # Fixed typo in streaming


    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        condense_question_llm=condensed_llm,
        metadata = chat_args.metadata
    )


