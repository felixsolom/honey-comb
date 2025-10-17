import os
import subprocess

def get_files_info(working_directory, directory=".") -> str:
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        content_of_dir = sorted(os.listdir(absolute_path))
        lines = [f'Results for {directory} directory:']
        for item in content_of_dir:
            if not item.startswith("__"):
                item_path = os.path.join(absolute_path, item)
                lines.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
        
        return '\n'.join(lines)
    except Exception as e:
        return f'Error listing files: {e}'
    
def get_file_content(working_directory: str, file_path: str) -> str:
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(absolute_path, "r") as file:
            file_content_string = file.read(10000)
            extra = file.read(1)
            if extra != "":
                file_content_string += f'...File "{file_path}" truncated at 10000 characters'
                return file_content_string
            return file_content_string

    except Exception as e:
        return f'Error reading file {file_path}: {e}'
    
def write_file(working_directory: str, file_path: str, content: str) -> str:
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    parent_dirs = os.path.dirname(absolute_path)
    if parent_dirs and not os.path.exists(parent_dirs):
        try: 
            os.makedirs(parent_dirs)
        except Exception as e:
            return f'Error: creating file path: {absolute_path}: {e}'
        
    if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
        return f'Error: "{file_path}" is a directory, not a file'
        
    try: 
        with open(absolute_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: could not write {content} to {file_path}: {e}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



