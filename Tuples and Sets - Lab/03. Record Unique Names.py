line = int(input())

unique_names = set()

for _ in range(line):
    unique_names.add(input())
for person in unique_names:
    print(person)
