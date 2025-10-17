import os
import subprocess


def run_python_file(working_directory: str , file_path: str, args=[]) -> str:
    absolute_working_dir = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = ['uv', 'run', absolute_path] + args 
        completed_process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=absolute_working_dir
        )

        output = []
        if completed_process.stdout:
            output.append(f'STDOUT:\n {completed_process.stdout}')

        if completed_process.stderr:
            output.append(f'STDERR:\n {completed_process.stderr}')

        if completed_process.returncode != 0:
            output.append(f'Process exited with code: {completed_process.returncode}')

        return '/n'.join(output) if output else 'No output produced'
    except Exception as e:
        return f'Error: executing Python file: {e}'
    

    



