chars = input()

for el in sorted(set(chars)):
    print(f"{el}: {chars.count(el)} time/s")
