import os
import sys

def get_all_py_files(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py') and not filename == os.path.basename(sys.argv[0]):
                files.append(os.path.join(dirpath, filename))
    return files

folder_path = "."
all_files = get_all_py_files(folder_path)

output_string = ""
for file_path in all_files:
    with open(file_path, 'r') as file:
        contents = file.read()
        output_string += f"\n\n\n\n''' {file_path} '''\n{contents}\n'''"

with open("full_code.txt", 'w') as output_file:
    output_file.write(output_string)
