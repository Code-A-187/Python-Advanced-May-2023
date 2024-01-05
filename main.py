import os
from datetime import datetime
file_path = "files/example.txt"

with open(file_path, "w") as file:
    file.write("maybe not that cool")

with open(file_path, "a") as file:
    file.write("just joking\n")
    file.write("just joking for real")

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "r") as file:
    print(file.readlines())

file_info = os.stat(file_path)

print(f"file size: {file_info.st_size} bytes")
print(f"last modified: {datetime.fromtimestamp(int(file_info.st_mtime))} bytes")

os.rename(file_path, "files/new_name.txt")
