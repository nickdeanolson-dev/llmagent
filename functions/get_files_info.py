import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        #print("--------")
        print(f"----\n - working: {working_directory}\n - directory: {directory}")
        #print(directory)

        file_description = ""
        if directory == ".":
            file_description += "Result for current directory:\n"
        else:
            file_description += f"Result for '{directory}' directory:\n"
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir == False:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        elif os.path.isdir(target_dir) == False:
            return (f'Error: "{directory}" is not a directory')
        else:

            #print(target_dir)
            files = os.listdir(target_dir)
            #print(files)
            try:
                for f in files:
                    file_description += f"- {f}: file_size={os.path.getsize(target_dir+"/"+f)}, is_dir={os.path.isdir(target_dir+"/"+f)}\n"
                    #print(file_description)
                    if os.path.isdir(target_dir+"/"+f) == True:
                        #print(f"** call ** {target_dir+"/"+f}")
                        #print(target_dir+"/"+f)
                        file_description += get_files_info(target_dir, f)
                file_description = file_description[:-1]
                return file_description
            except Exception as e:
                return(f'Error: {e}')
            return (f'Success: "{directory}" is within the working directory')
    except Exception as e:
        return(f'Error: {e}')

    