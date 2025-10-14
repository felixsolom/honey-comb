import os

def get_files_info(working_directory, directory=".") -> str:
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    content_of_dir = os.listdir(absolute_path)
    files_info = f'Results for {directory}:'
    for _, item in content_of_dir:
        "\n".join(files_info, f'- {item}, file_size={os.path.getsize(item)}, is_dir={os.path.isdir(item)}')
    
    return files_info