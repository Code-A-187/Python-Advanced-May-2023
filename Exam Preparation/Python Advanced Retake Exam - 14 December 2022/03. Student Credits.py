def students_credits(*args):
    exams_dict = {}
    sum_credits = 0
    for el in args:
        course_name, max_credits, max_test_points, diyan_points = [int(x) if x.isnumeric() else x for x in el.split('-')]
        exam_credits = (diyan_points / max_test_points) * max_credits
        sum_credits += exam_credits
        exams_dict[course_name] = exam_credits
    sorted_exams_dict = sorted(exams_dict.items(), key=lambda x: -x[1])
    result = ''
    if sum_credits < 240:
        result += f"Diyan needs {240 - sum_credits:.1f} credits more for a diploma.\n"
    else:
        result += f"Diyan gets a diploma with {sum_credits:.1f} credits.\n"
    for course, credits in sorted_exams_dict:
        result += f"{course} - {credits:.1f}\n"

    return result

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
