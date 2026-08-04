from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}\nlorem.txt truncated: {'truncated' in result}\n\n")

result = get_file_content("calculator", "main.py")
print(f"main.py length: {len(result)}\nmain.py truncated: {'truncated' in result}\n\n\n")

result = get_file_content("calculator", "pkg/calculator.py")
print(f"pkg/calculator.py length: {len(result)}\npkg/calculator.py truncated: {'truncated' in result}\n\n\n")

result = get_file_content("calculator", "/bin/cat")
print(f"/bin/cat length: {len(result)}\n/bin/cat truncated: {'truncated' in result}\n\n\n")

result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"pkg/does_not_exist.py length: {len(result)}\npkg/does_not_exist.py truncated: {'truncated' in result}\n\n\n")