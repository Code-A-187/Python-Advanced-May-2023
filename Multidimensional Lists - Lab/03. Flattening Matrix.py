row = int(input())


flatten = []
for row_index in range(row):
    inner_list = [int(el) for el in input().split(", ")]
    flatten.extend(inner_list)

print(flatten)
