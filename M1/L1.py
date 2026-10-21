from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-5.4-mini")
msg = model.invoke("In one sentence: what does a solid amber LED usually mean on an IoT gateway?")
print(type(msg).__name__)
print(msg.text)