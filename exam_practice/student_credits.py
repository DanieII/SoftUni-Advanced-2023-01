def students_credits(*args):
    NEEDED = 240
    collected = 0
    courses = {}
    output = []

    def calculate_credits(credits, max, current):
        percentage = int(current) / int(max) * 100
        result = int(credits) * percentage / 100
        return result

    for elements in args:
        course_name, course_credits, max_points, current_points = elements.split("-")
        current_credits = calculate_credits(course_credits, max_points, current_points)
        collected += current_credits
        courses[course_name] = current_credits
    sorted_courses = dict(sorted(courses.items(), key=lambda x: -x[1]))
    if collected >= NEEDED:
        output.append(f"Diyan gets a diploma with {collected:.1f} credits.")
    else:
        output.append(f"Diyan needs {NEEDED - collected:.1f} credits more for a diploma.")
    for k, v in sorted_courses.items():
        message = f"{k} - {v:.1f}"
        output.append(message)
    return "\n".join(output)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

