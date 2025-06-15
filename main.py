import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def print_usage():
    usage = """
Usage: python main.py \"<PROMPT>\" [options...]
Options:
 -h,  --help        Show this help message and exit.
 -v,  --verbose     Enable verbose output.
Example:
  python main.py "How does I shot web?" -v
"""
    print(usage)

def process_options(options):
    # Check for help option
    if "-h" in options or "--help" in options:
        print_usage()
        sys.exit(0)

    # Check for verbose option
    verbose = "-v" in options or "--verbose" in options
    if verbose:
        print("Verbose mode enabled.")

    return verbose

def check_env_variables():
    required_vars = ["GEMINI_API_KEY"]
    for var in required_vars:
        if not os.getenv(var):
            print(f"Error: Environment variable {var} is not set. Please add it to your .env file.")
            sys.exit(1)

def generate_content(client, message, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=message
    )
    if verbose:
        print("User prompt: {}".format(message))
        print("Prompt tokens: {}".format(response.usage_metadata.prompt_token_count))
        print("Response tokens: {}".format(response.usage_metadata.candidates_token_count))
    print("Response:")
    print(response.text)

def main():
    load_dotenv()
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)
    user_prompt = sys.argv[1]
    options = sys.argv[2:]
    verbose = process_options(options)
    check_env_variables()
    api_key = os.getenv("GEMINI_API_KEY")

    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)

    generate_content(client, messages, verbose)

if __name__ == "__main__":
    main()
