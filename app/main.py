from openai import OpenAI
from dotenv import load_dotenv
from scraper import web_scraper
import os
import openai


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found in environment variables")
    exit(1)


def llm_helper(prompt):
    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    system_prompt = "You are an skillful AI assitant who is skilled in summarising any content. You provide short and concise summarisation while keeping all the main point intact. The content you provide is meaningful and well structured"

    user_prompt = web_scraper(prompt)
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"Hello, can you summarise this {user_prompt}",
                },
            ],
            extra_body={"reasoning": {"enabled": True}},
        )
        return response.choices[0].message.content

    except openai.AuthenticationError as e:
        print(f"Authentication failed: {e}")
    except openai.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
    except openai.APIConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
