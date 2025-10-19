import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.schema import available_functions
from functions.call_functions import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv

    print('AI Code Assistant')
    print("Enter '/quit' to quit the session")

    messages = []

    while True:
        try: 
            user_prompt = input("> ")
            if user_prompt.lower  == "/quit":
                break
            
            messages.append(
                types.Content(
                    role="user",
                    parts=[types.Part(text=user_prompt)]
                )
            )

            if verbose:
                print(f"User prompt: {user_prompt}")

            max_turns = 20
            for turn in range(max_turns):
                try: 
                    response_text = generate_content(client, messages, verbose)
                    if response_text:
                        print(f"AI: {response_text}")
                        break
                except Exception as e:
                    print(f"Error on turn {turn + 1}: {e}")
                    if turn == max_turns - 1:
                        print("Max tries reached. Exiting.")
                    else:
                        print("Retrying...")
        except KeyboardInterrupt:
            print("\nExiting...")
            break 
        


def generate_content(client: genai.Client, messages: list, verbose: bool) -> str | None:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=SYSTEM_PROMPT
        )
    )

    if response.candidates and response.candidates[0].content:
        messages.append(response.candidates[0].content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return response.text 

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function responses generated. Exiting")
    
    content = types.Content(
        role="tool",
        parts=function_responses
    )
    messages.append(content)

    return None

if __name__ == "__main__":
    main()

