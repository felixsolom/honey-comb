from google.genai import types
from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.run_python import run_python_file

CALLING_FUNCTIONS = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
}


def call_function(function_call_part: types.FunctionCall, verbose=False) -> types.Content:
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    function_args = function_call_part.args 

    if function_name not in CALLING_FUNCTIONS:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
)
    function_to_call = CALLING_FUNCTIONS[function_name]
    function_result = function_to_call("calculator", **function_args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)

    
