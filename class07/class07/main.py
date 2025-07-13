from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, RunConfig, Agent, Runner

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

# function calling
@function_tool
def get_weather():
    # API/ DB call
    return "Today Current weather is 24 degrees"

# Creating an Agent
weather_agent = Agent(
    name = 'Weather Agent',
    instructions=""" 
        You are a weather agent. Answer the user query to let user know the weather.
        Beyond weather donot answer any query.
    """,
    tools=[get_weather]
)

# Execute your agent
result = Runner.run_sync(weather_agent, "What is the weather today?", run_config=config)
print(result.final_output)