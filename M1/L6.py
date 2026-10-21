from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "openai:gpt-5.4-mini",
    temperature=0,      # deterministic-ish output for support answers
    max_tokens=400,     # cap cost and latency
    timeout=30,         # seconds
    max_retries=2,      # retries on rate limits and transient errors
)
print(model.invoke("Name one cause of Zigbee interference in two words.").text)