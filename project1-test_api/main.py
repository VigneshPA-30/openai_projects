from langchain.llms import OpenAI
from langchain.chains import  LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task",default="create and print random 10 numbers")
parser.add_argument("--language",default="python")
args = parser.parse_args()



llm = OpenAI()


code_prompt = PromptTemplate(
    template = "Write a program in {language} that will {task}",
    input_variables = ["language","task"],
    
)

test_prompt = PromptTemplate(
    template = "Write a test in {language} for the code \n {code}",
    input_variables = ["language","code"],
    

)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key = "code"
)

test_chain = LLMChain(
    llm=llm,
    prompt = test_prompt,
    output_key = "test_code"
)



chain = SequentialChain(
    chains=[code_chain,test_chain],
    input_variables=["language","task"],
    output_variables=["code","test_code"]
)

result = chain({
    "language":args.language,
    "task":args.task
})
print(">>>>>>>>>>>>>>>>>>>>>>>>>>GENERATED CODE")
print(result["code"])
print(">>>>>>>>>>>>>>>>>>>>>>>>>>TEST CODE")
print(result["test_code"])