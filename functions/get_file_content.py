import os
#from config import *

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the first 10000 characters of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file_path is the relative path from the working directory to the file to open.",
                },
            },
        },
    },
}
available_functions = [
    schema_get_file_content
]

def get_file_content(working_directory: str, file_path: str) -> str:
    print(f"----\n - working: {working_directory}\n - file path: {file_path}")
    
    working_dir_abs = (os.path.abspath(working_directory))
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    #print(working_dir_abs)
    #print(target_dir)
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    try:
        if valid_target_dir == False:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        #elif os.path.isdir(target_dir) == False:
            #return (f'Error: "{file_path}" is not a directory')
        if os.path.isfile(working_dir_abs+"/"+file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'


        with open(working_dir_abs+"/"+file_path) as f:
            contents = f.read(10000)
            if f.read(1):
                contents += f'[...File "{file_path}" truncated at {10000} characters]'
        return contents
    except Exception as e:
        return(f'Error: {e}')