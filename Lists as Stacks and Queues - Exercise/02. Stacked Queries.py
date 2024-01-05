from collections import deque

numbers = deque()
from collections import deque

numbers = deque()

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    command = number_data[0]

    if command == 1:
        numbers.append(number_data[1])
    elif command == 2:
        if numbers:
            numbers.pop()
    elif command == 3:
        if numbers:
            print(max(numbers))
    elif command == 4:
        if numbers:
            print(min(numbers))

numbers.reverse()
print(*numbers, sep=', ')

# second version
# map_funtions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_funtions[number_data[0]](number_data)
#
# numbers.reverse()
# print(*numbers, sep=', ')