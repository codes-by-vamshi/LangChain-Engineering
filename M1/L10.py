from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model
import logging

def safe_settings(model_string, **settings):
    model = init_chat_model(model=model_string, api_key=settings.get("api_key"))
    model_profile = model.profile or {}
    if 'temperature' in settings and model_profile.get("temperature") is False:
        logging.warning(f"Dropping temperature: {model_string} does not support it")
        settings.pop("temperature")
    return init_chat_model(model=model_string, **settings)

m = safe_settings("openai:gpt-5.4-mini", temperature=1, api_key="sk-x")
print(m.temperature)

m = safe_settings("openai:gpt-5.5", temperature=1, api_key="sk-x")
print(m.temperature)