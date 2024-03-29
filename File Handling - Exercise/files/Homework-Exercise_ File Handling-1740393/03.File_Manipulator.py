import os

command_args = input()

while command_args != "End":
    command, *info = command_args.split("-")

    if command == "Create":
        with open(f"files/{info[0]}", "w"):
            pass
    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred")

    command_args = input()

# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
