numbers = [int(x) for x in input().split()]
sum_ = int(input())

nums = set()

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == sum_:
            nums.add(f"{numbers[i]} + {numbers[j]} = {sum_}")

for num in sorted(nums):
    print(num)
