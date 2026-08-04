import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    print(f"----\nworking_directory: {working_directory}\nfile_path: {file_path}\nargs: {args}")
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_file_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
    absolute_file_directory = os.path.dirname(absolute_file_path)
    valid_target_dir = (os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir)

    try:
        if not valid_target_dir:
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not file_path.endswith(".py"):
            return (f'Error: "{file_path}" is not a Python file')
        if not os.path.isfile(absolute_file_path):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        command = ["python", absolute_file_path]
        if args is None:
            args = []
        command.extend(args)

        completed = subprocess.run(command, capture_output=True, text=True, cwd = absolute_working_dir, timeout=30)


        results = ""
        if completed.returncode != 0:
            results += f"Process exited with code {completed.returncode}\n"
        if not completed.stdout and not completed.stderr:
            results += "No output produced\n"
        else:
            results +=f"STDOUT: {completed.stdout}\nSTDERR: {completed.stderr}"

        return results
        
    except Exception as e:
        return(f"Error: executing Python file: {e}")