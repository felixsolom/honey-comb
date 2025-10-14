import os

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