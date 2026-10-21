from importlib.metadata import version

for pkg in ["langchain", "langchain-core", "langchain-openai", "langgraph", "langsmith"]:
    print(f"{pkg:18} {version(pkg)}")

from langchain.agents import create_agent
graph_type = create_agent.__annotations__["return"]
print("create_agent returns:", graph_type.split("[")[0])