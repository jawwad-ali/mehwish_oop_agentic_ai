from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner

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

# Creating an Agent
writer = Agent(
    name = 'Writer Agent',
    instructions=""" 
        You are a writer agent. Write whatever user wants to make your write.
    """
)


# Execute your agent
result = Runner.run_sync(writer, "Write an essay on Noise Pollution. Write one paragraph only", run_config=config)
print(result.final_output)
