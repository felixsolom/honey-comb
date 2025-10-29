from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists files content truncated to 10000 characters in the specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes given content to a specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file path, relative to the working directory.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs Python file in the specified file path with provided args, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a Python file to be run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Args provided after the Python file and needed by the Python file to run with as commands",
            ),
        },
    ),
)

schema_web_search = types.FunctionDeclaration(
    name="web_search",
    description="Performs a web search using a search engine and returns the results",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description="The search query",
            ),
        },
    ),
)

schema_git_status = types.FunctionDeclaration(
    name="run_git_status",
    description="Runs git status and returns the output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={},
    ),
)

schema_git_diff = types.FunctionDeclaration(
    name="run_git_diff",
    description="Runs 'git diff' on a specific file or an entire project.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to run diff. If not provided, shows all changes",
            ),
        },
    ),
)

schema_git_commit = types.FunctionDeclaration(
    name="run_git_commit",
    description="Runs 'git commit' with the given message.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "message": types.Schema(
                type=types.Type.STRING,
                description="The commit message",
            ),
        },
    ),
)


schema_git_add = types.FunctionDeclaration(
    name="run_git_add",
    description="Runs 'git add' command on a specific file to stage it to a commit",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to add",
            ),
        },
    ),
)
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
        schema_web_search,
        schema_git_status,
        schema_git_diff,
        schema_git_add,
        schema_git_status,
    ]
)
