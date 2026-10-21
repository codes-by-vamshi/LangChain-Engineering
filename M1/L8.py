from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model
configurable = init_chat_model(temperature=0)

cheap = {"configurable": {"model": "openai:gpt-5-nano"}}
strong = {"configurable": {"model": "openai:gpt-5.4-mini"}}

response_cheap = configurable.invoke("Say OK.", config=cheap)
response_strong = configurable.invoke("Say OK.", config=strong)

print(response_cheap.text)
print(response_strong.text)