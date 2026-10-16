from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

model = ChatOpenAI()

for _ in model.stream("Explain AI?"):
    print(_.content, end="", flush=True)