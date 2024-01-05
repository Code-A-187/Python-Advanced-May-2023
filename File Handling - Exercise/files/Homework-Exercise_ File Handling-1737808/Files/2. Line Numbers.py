import string
path = "file_handing//2. Line Numbers.txt"
with open(path, "r") as f:
    text = f.readlines()

letters = 0
punctuation = 0
for idx in range(len(text)):
    for symbol in text[idx]:
        if symbol.isalpha():
            letters += 1
        elif symbol.isspace() == False and symbol.isalpha() == False:
            punctuation += 1
    i = idx+1
    print(f"Line {i}: {text[idx]} ({letters})({punctuation})")
    letters = 0
    punctuation = 0

