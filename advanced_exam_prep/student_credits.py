def students_credits(*args):
    courses_dict = {}
    final_course_credits = 0
    final_strings = []

    for arg in args:
        course, credit, max_points, diyans_points = arg.split("-")
        courses_dict[course] = 0
        percentage = float(diyans_points) / float(max_points)
        credit = float(credit)
        final_credits = (credit * percentage)
        courses_dict[course] = final_credits
        final_course_credits += final_credits

    if final_course_credits >= 240:
        final_strings.append(f"Diyan gets a diploma with {final_course_credits:.1f} credits.")
    else:
        final_strings.append(f"Diyan needs {240 - final_course_credits:.1f} credits more for a diploma.")

    sorted_courses_dict = sorted(courses_dict.items(), key=lambda x: -x[1])
    for course, points in sorted_courses_dict:
        final_strings.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_strings)








print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
