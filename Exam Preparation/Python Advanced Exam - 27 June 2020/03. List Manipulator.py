def list_manipulator (list_, *args):
    numbers_list = []
    command = args[0] + ' ' + args[1]
    for el in args:
        if str(el).isdigit():
            numbers_list.append(el)
    if command == 'add beginning':
        list_ = numbers_list + list_
    elif command == 'add end':
        list_.extend(numbers_list)
    elif command == "remove beginning":
        if numbers_list:
            list_ = list_[numbers_list[0]:]
        else:
            list_.pop(0)
    elif command == "remove end":
        if numbers_list:
            del list_[len(list_) -numbers_list[0]:]
        else:
            list_.pop()

    return list_


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
