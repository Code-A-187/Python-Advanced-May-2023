odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    sum_name = sum(map(ord, input())) // row

    if sum_name % 2 == 0:
        even_set.add(sum_name)
    else:
        odd_set.add(sum_name)

if sum(odd_set) == sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.union(even_set))}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.difference(even_set))}")
elif sum(odd_set) < sum(even_set):
    print(f"{', '.join(str(x) for x in odd_set.symmetric_difference(even_set))}")
