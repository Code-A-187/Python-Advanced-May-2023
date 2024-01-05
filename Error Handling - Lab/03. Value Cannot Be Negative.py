class ValueCanNotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            raise ValueCanNotBeNegative
    except ValueError:
        print("This is not a valid number. Continue to next one")
