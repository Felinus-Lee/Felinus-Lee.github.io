import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.chains.question_answering import load_qa_chain

os.environ[
    "OPENAI_API_KEY"] = "input your key"

openai.api_key = os.environ['OPENAI_API_KEY']

graph = Neo4jGraph(
    url="input your url",
    username="username",
    password="password")


chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0),
    graph=graph, verbose=True,)

print(chain.run("""给我说一下骨猴外观吧"""))