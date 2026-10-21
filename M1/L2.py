from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.agents import create_agent

def device_status(device_id: str) -> str:
    """Return the live status of an IoT device by serial ID."""
    return f"{device_id}: offline, LED solid amber, clock drift 412 s"

agent = create_agent(
    model="openai:gpt-5.4-mini",
    tools=[device_status],
    system_prompt="You are an IoT support assistant. Use tools for live device data."
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "What's going on with GW-10-0042?"}]
})

print(result["messages"][-1].text)