import asyncio
import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

model = ChatOpenAI()

def chat1():
    response = model.invoke("What is 1+2?")
    print(response.content)

def chat2():
    response = model.invoke("What is 2+3?")
    print(response.content)

async def chat1_async():
    response = await model.ainvoke("What is 1+2?")
    print(response.content)

async def chat2_async():
    response = await model.ainvoke("What is 2+3?")
    print(response.content)

print("Synchronous case")
start_time = time.time()
chat1()
chat2()
end_time = time.time()
total_time = end_time - start_time
print(f"Total Time take is: {total_time}")

print("-----------------")
print("Asynchronous case")
start_time = time.time()
async def main():
    await asyncio.gather(
        chat1_async(),
        chat2_async()
    )
asyncio.run(main())
end_time = time.time()
total_time = end_time - start_time
print(f"Total Time take is: {total_time}")