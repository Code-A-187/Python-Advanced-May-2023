import os

comand=input()
while comand!="End":
    comand, *text = comand.split("-")

    if comand=="Create":
        with open(f"file_handing/{text[0]}", "w") as f: pass
            #f.write("")

    elif comand=="Add":
        with open(f"file_handing/{text[0]}", "a") as f:
            f.write(f"{text[1]}\n")

    elif comand=="Replace":
        try:
            with open(f"file_handing/{text[0]}", "r+") as f:
                info = f.read()
                info = info.replace(text[1], text[2])
                f.seek(0)
                f.write(info)

        except FileNotFoundError:
            print(f"An error occurred")


    elif comand=="Delete":
        try:
            os.remove(f"file_handing/{text[0]}")
        except FileNotFoundError:
            print(f"An error occurred")

    comand = input()
