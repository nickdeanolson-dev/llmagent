import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    absolute_working_dir = os.path.abspath(working_directory)
    absolute_file_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
    absolute_file_directory = os.path.dirname(absolute_file_path)
    valid_target_dir = (os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir)

    try:
        if valid_target_dir == False:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(absolute_file_path) == True:
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
        os.makedirs(absolute_file_directory, exist_ok=True)

        with open(absolute_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return(f'Error: {e}')