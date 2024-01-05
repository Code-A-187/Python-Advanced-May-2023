def gather_credits(max_credits, *args):

    courses = []
    enrolled_credits = 0

    for course, credits in args:
        if max_credits <= 0:
            break
        if course not in courses:
            courses.append(course)
            enrolled_credits += credits
            max_credits -= credits

    result = ''
    if max_credits <= 0:
        result += f"Enrollment finished! Maximum credits: {enrolled_credits}.\nCourses: {', '.join(sorted(courses))}"
    else:
        result += f'You need to enroll in more courses! You have to gather {max_credits} credits more.'

    return result

print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    0,
    ("Advanced", 25),
    ("Basics", 15),
    ("Fundamentals", 15),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))



