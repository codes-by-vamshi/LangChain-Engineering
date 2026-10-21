from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

model = init_chat_model(model="openai:gpt-5.4-mini")

print(type(model).__name__)
print(model.profile)