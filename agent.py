
import asyncio

import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from browser_use import Agent



load_dotenv()



GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

CDP_URL = os.environ.get("CDP_URL", "http://localhost:9222")

TASK = os.environ.get("TASK", "Go to google.com and search for 'browser-use' and summarize the top result.")



async def main():

    print(f"[INFO] Connecting to Chrome via CDP: {CDP_URL}")

    print(f"[INFO] Task: {TASK}")



    llm = ChatGoogleGenerativeAI(

        model="gemini-2.0-flash",

        google_api_key=GEMINI_API_KEY,

        temperature=0.0,

    )



    agent = Agent(

        task=TASK,

        llm=llm,

        browser_context_config={

            "cdp_url": CDP_URL

        }

    )



    print("[INFO] Running agent...")

    result = await agent.run()

    print(f"[RESULT] {result}")



if __name__ == "__main__":

    asyncio.run(main())

