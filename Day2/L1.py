from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="openai:gpt-5.4-mini",
    max_tokens=200,
    temperature=0
)

response1 = model.invoke("Explain what is AI?")
response2 = model.invoke("Explain what is AI?")

print(response1.content)
print("---------------------")
print(response2.content)