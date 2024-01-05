def print_numbers(positive, negative):
    print(sum(negative))
    print(sum(positive))

    if sum(positive) > abs(sum(negative)):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = [int(x) for x in input().split()]

positive_nums = []
negative_nums = []

for number in numbers:
    if number > 0:
        positive_nums.append(number)
    else:
        negative_nums.append(number)

print_numbers(positive_nums, negative_nums)
