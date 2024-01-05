import os

text_input=""
file_path="file_handing//1. Even Lines.txt"

#This is code work like "cat" command in Linux. If you want to stop write- must press Ctrl+D
with open(file_path, "w") as f:
    while True:
        try:
            text_input=input()
        except:
            break
        f.write(text_input+"\n")

with open(file_path,"r") as f:
    text=f.readlines()

symbols= {"-", ",", ".", "!", "?"}
for el in range(0,len(text),2):
    for symbol in symbols:
        text[el]=text[el].replace(symbol, "@")

    print(*text[el].split()[::-1], sep=" ")








