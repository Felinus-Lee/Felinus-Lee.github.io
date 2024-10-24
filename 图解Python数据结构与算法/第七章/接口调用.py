import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.chains.question_answering import load_qa_chain

os.environ[
    "OPENAI_API_KEY"] = "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"

openai.api_key = os.environ['OPENAI_API_KEY']

graph = Neo4jGraph(
    url="bolt://3.88.133.234:7687",
    username="neo4j",
    password="sheet-rocket-highline")


chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0),
    graph=graph, verbose=True,)


value = input()
print(type(chain.run(f"""{value}""")))