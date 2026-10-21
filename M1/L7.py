from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-5.4-mini", api_key="sk-not-a-real-key", timeout=30, max_retries=2)
print(type(model).__module__, type(model).__name__)
print("model_name:", model.model_name, "| timeout:", model.request_timeout, "| retries:", model.max_retries)

for name in ["gpt-5.4-mini", "gpt-5.5"]:
    p = init_chat_model(f"openai:{name}", api_key="sk-x").profile
    print(f"{name:13} context={p['max_input_tokens']:>9,} tools={p['tool_calling']} temperature={p['temperature']}")