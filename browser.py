from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def main():
    # Initialize LLM within the async function's scope.
    # This helps ensure its underlying gRPC resources are managed correctly
    # within the asyncio event loop's lifecycle, preventing the 'POLLER' error. [1]
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.0, google_api_key=os.getenv("GOOGLE_API_KEY"))

    agent = Agent(
        task="got to my google keep note , there is a note titled interviewer , grab text from  the image and send me the text  ",
        llm=llm,
        save_conversation_path="logs/conversation"
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())