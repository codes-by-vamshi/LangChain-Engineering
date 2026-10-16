from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

def device_status(device_id: str) -> str:
    """Return the live status of an IoT device by serial ID."""
    return f"{device_id}: offline, LED solid amber, clock drift 412 s"

agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    tools=[device_status],
    system_prompt="You're a helpful assitant"
)

result = agent.invoke({
    "messages": [
        HumanMessage("Hey, What's going on with GW-10-0042?")
    ]
})

for msg in result["messages"]:
    print(f"{type(msg)}: {msg.text}")