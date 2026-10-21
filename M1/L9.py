from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model
import os

def getModel():
    chat_model = os.getenv("CHAT_MODEL", "openai:gpt-5.4-mini")
    arguments = {
        "timeout": 30,
        "max_retries": 2
    }
    temp = os.getenv("CHAT_TEMPERATURE")
    if temp is not None:
        arguments["temperature"] = float(temp)
    model = init_chat_model(
        model=chat_model,
        **arguments
    )
    return model
model = getModel()