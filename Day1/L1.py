from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

model = ChatOpenAI()

response = model.invoke("How are you?")

print(type(response))
print("-------------")
print(response)
print("-------------")
print(response.content)