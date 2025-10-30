import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.markdown import Markdown
from system_prompt import SYSTEM_PROMPT
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

    console = Console()

    console.print("[bold green]AI Code Assistant[/bold green]")
    console.print("Enter 'exit' or 'quit' to quit the session")

    messages = []

    while True:
        try:
            user_prompt = console.input("[bold yellow]> [/bold yellow]")
            if user_prompt.lower in ["exit", "quit"]:
                break

            messages.append(
                types.Content(role="user", parts=[types.Part(text=user_prompt)])
            )

            if verbose:
                console.print(f"User prompt: {user_prompt}")

            max_turns = 20
            for turn in range(max_turns):
                try:
                    response_text = generate_content(client, messages, verbose)
                    if response_text:
                        console.print(Markdown(response_text))
                        break
                except Exception as e:
                    console.print(f"[bold red]Error on turn {turn + 1}:[/bold red] {e}")
                    if turn == max_turns - 1:
                        console.print(
                            "[bold red]Max tries reached. Exiting.[/bold red]"
                        )
                    else:
                        console.print("[yellow]Retrying...[/yellow]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
            break


def generate_content(client: genai.Client, messages: list, verbose: bool) -> str | None:
    console = Console()

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )

    if response.candidates and response.candidates[0].content:
        messages.append(response.candidates[0].content)

    if verbose:
        if response.usage_metadata:
            console.print(
                f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
            )
            console.print(
                f"Response tokens: {response.usage_metadata.candidates_token_count}"
            )

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
            console.print(
                f"-> {function_call_result.parts[0].function_response.response}"
            )
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function responses generated. Exiting")

    content = types.Content(role="tool", parts=function_responses)
    messages.append(content)

    return None


if __name__ == "__main__":
    main()
