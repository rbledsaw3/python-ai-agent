import os
from google import genai
from dotenv import load_dotenv

def print_response(response):
    print("Prompt tokens: {}".format(response.usage_metadata.prompt_token_count))
    print("Response tokens: {}".format(response.usage_metadata.candidates_token_count))
    print("Response:")
    print(response.text)

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print_response(response)

if __name__ == "__main__":
    main()
