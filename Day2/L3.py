from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

configurable_model = init_chat_model()

openai_config = {"configurable": {"model": "openai:gpt-5.4-mini"}}
groq_config = {"configurable": {"model": "groq:openai/gpt-oss-120b"}}

# Can be configurable per call
response1 = configurable_model.invoke("Hey Hi", config=openai_config)
print(response1.text)

response2 = configurable_model.invoke("Hey Hi", config=groq_config)
print(response2.text)
