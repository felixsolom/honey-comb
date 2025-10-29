from google.genai import types
from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.git_operations import (
    run_git_add,
    run_git_commit,
    run_git_status,
    run_git_diff,
)
from functions.run_python import run_python_file
from functions.web_search import web_search
from config import WORKING_DIR

FUNCTIONS_MAP = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "web_search": web_search,
    "run_git_status": run_git_status,
    "run_git_add": run_git_add,
    "run_git_commit": run_git_commit,
    "run_git_diff": run_git_diff,
}


def call_function(
    function_call_part: types.FunctionCall, verbose=False
) -> types.Content:
    function_name = function_call_part.name

    if function_name is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name="unknown_function",
                    response={"error": "Function call is missing a name."},
                )
            ],
        )

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_name not in FUNCTIONS_MAP:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    function_args = function_call_part.args
    args = dict(function_args or {})

    if function_name != "web_search":
        args["working_directory"] = WORKING_DIR

    function_result = FUNCTIONS_MAP[function_name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
