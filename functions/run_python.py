import os
import docker
from docker.errors import BuildError, ContainerError, DockerException, ImageNotFound
import shlex


def run_python_file(working_directory: str, file_path: str, args: str = "") -> str:
    if not file_path.endswith(".py"):
        return "Error: Only Python files (.py) are allowed"

    try:
        client = docker.from_env()
        client.ping()
    except DockerException as e:
        return f"Error: docker not available - {e}"

    image_tag = "honey-comb-sandbox"

    try:
        client.images.get(image_tag)
    except ImageNotFound:
        return f"Error: Docker image {image_tag} not found. Build it with 'Docker build -t {image_tag} .'"

    try:
        real_working_dir = os.path.realpath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        real_file_path = os.path.realpath(full_path)

        if not real_file_path.startswith(real_working_dir + os.sep):
            return f"Error: Path traversal detected in {file_path}"

        if not os.path.exists(real_file_path):
            return f'Error: File "{file_path}" not found.'
    except (OSError, ValueError) as e:
        return f"Error: Invalid path - {e}"

    cmd = ["python", f"home/appuser/workspace/{file_path}"]
    if args:
        try:
            cmd.extend(shlex.split(args))
        except ValueError as e:
            return f"Error: Invalid argumemts - {e}"
    try:
        container_output = client.containers.run(
            image=image_tag,
            command=cmd,
            working_dir="/home/appuser/workspace",
            volumes={
                os.path.abspath(real_working_dir): {
                    "bind": "/home/appuser/workspace",
                    "mode": "ro",
                }
            },
            remove=True,
            stderr=True,
            stdout=True,
            network_disabled=True,
            mem_limit="512m",
            cpu_quota=50000,
        )
        if isinstance(container_output, bytes):
            return container_output.decode("utf-8")
        return str(container_output)

    except ContainerError as e:
        stderr_output = ""
        if isinstance(e.stderr, bytes):
            stderr_output = e.stderr.decode("utf-8")
        else:
            stderr_output = str(e.stderr)
        return f"An error occurred in the sandbox:\n{stderr_output}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
