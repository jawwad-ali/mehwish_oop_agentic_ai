from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, RunConfig, Agent, Runner
import rich
import requests
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

# Connectivity Starts
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# LLM - Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# 
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

dealership_agent = Agent(
    name="DealerShip Agent",
    instructions=""" 
        You are a dealership agent in toyota, you task is to give details about a car
    """
)

# result = Runner.run_sync(dealership_agent, "What are the features in toyota corolla", run_config=config)

# async def main():
#     result = await Runner.run(dealership_agent, "What are the features in toyota corolla", run_config=config)
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())


async def main():
    result = Runner.run_streamed(dealership_agent, "Write 5 paragraphs on problems of pakistan", run_config=config)
    async for event in result.stream_events():
        print(event)
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())