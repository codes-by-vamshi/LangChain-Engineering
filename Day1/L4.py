from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="groq:openai/gpt-oss-120b",
)

response = model.invoke("Hello, How are you")
print(response.content)