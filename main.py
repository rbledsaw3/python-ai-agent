import os
import sys
from google import genai
from dotenv import load_dotenv

def print_response(response):
    print("Prompt tokens: {}".format(response.usage_metadata.prompt_token_count))
    print("Response tokens: {}".format(response.usage_metadata.candidates_token_count))
    print("Response:")
    print(response.text)

def main():
    load_dotenv()
    if len(sys.argv) != 2:
        print("Usage: python main.py \"<PROMPT>\"")
        sys.exit(1)
    prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt
    )
    print_response(response)

if __name__ == "__main__":
    main()
