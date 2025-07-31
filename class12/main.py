from agents import (
    Agent,
    Runner,
    function_tool,
    trace
)
from pydantic import BaseModel
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()

@function_tool
def current_weather():
    return "Sunny :-) "

@function_tool
def current_location():
    return "Karachi"

automobile_agent = Agent(
    name = "Automobile Agent",
    instructions = """ 
        You are a manager a toyota dealership, you task us to answer queries related to toyota cars.
    """
)

main_agent = Agent(  
    name="Main Agent",
    instructions=""" 
    You are a agent you can call tool by yourself. Donot makeup responses 
    if you donot know the user asnswer. you the tools instead.
    In the case of handoffs delegate the user query to the appropriate sub-agent. Donot make response by 
    yourself
    """,
    tools=[current_location, current_weather],
    handoffs=[automobile_agent]
)

async def main():
    # This should trip the guardrail
    # result = await Runner.run(main_agent, "What is the weather and what is my location?", run_config=config)
    with trace("Class 12"):
        result = await Runner.run(main_agent, 
        """
            give some details about toyota corolla
            what is the weather?
            what is my location?
        """
        , run_config=config)
        print(result)

if __name__ == "__main__":
    asyncio.run(main())