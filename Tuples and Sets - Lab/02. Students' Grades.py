count = int(input())

students_list = {}

for _ in range(count):
    line = tuple(input().split())
    student, grade = line
    if student not in students_list:
        students_list[student] = []
    students_list[student].append(float(grade))

for name, grades in students_list.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {average_grade:.2f})")
