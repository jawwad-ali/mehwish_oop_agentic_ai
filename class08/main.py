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

# function calling
@function_tool
def send_email(to: str, by: str, message_body: str, attachments = None):
    return "Email Sent!!!"

@function_tool
def get_weather():
    # API CALL here
    url = requests.get("cryptoURL")
    return "Today is a Rainy day"

email_agent = Agent(
    name = 'Email Agent',
    instructions = """ You are an email agent, your task is to send email to the 
    recepient provided in the user prompt. and answer any user query by your knowledge 
    or calling any tool required """,
    tools = [send_email, get_weather]
)

# Execute your agent
result = Runner.run_sync(
    email_agent, 
    """ 
        Send an email to mehwish@gmail.com from ali@yahoo.com informing her that 
        She has done her assisgnments really nicely, and tell me the weather today
        also please tell me my current location
    """, 
    run_config=config)

rich.print(result.new_items)

print(result.final_output)