from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = init_chat_model("openai:gpt-5.4-mini")
chain = ChatPromptTemplate.from_template("Summarise: {ticket}") | model | StrOutputParser()

response = chain.invoke({"ticket": "Gateway GW-10 shows solid amber after firewall change."})
print(response)