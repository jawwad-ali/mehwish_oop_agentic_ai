from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, RunConfig, Agent, Runner
# uv add rich
import rich
import requests

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
# Connectivity ends here

arabic_agent = Agent(
    name = "Arabic agent",
    instructions='You are a arabic agent, You job is to answer user query in arabic or talk with the user in arabic'
)
spanish_agent = Agent(
    name = 'Spanish Agent',
    instructions='You are a spanish agent, You job is to answer user query in spanish or talk with the user in spanish'
)
# Main
triage_agent = Agent(
    name = 'Triage Agent',
    instructions = """ 
        You are a helpful assistant
        Your Routine is:
        1. Handoffs to spanish agent when user asks or directly talks in spanish
        2. Handoffs to arabic agent when user asks or directly talks in arabic
        3. Any other language then spanish or arabic or keep the query only to yourself 
    """,
    handoffs = [spanish_agent, arabic_agent]
)

# Execute your agent
result = Runner.run_sync(
    triage_agent, 
    """ 
        Let's talk in sunskrit.
    """, 
    run_config=config)

rich.print(result.last_agent.name)
print(result.final_output)
rich.print(result.new_items)