# advisor_matcher.py

def match_advisors_to_students(students):
    """
    Simple logic to assign each student an advisor.
    This function will eventually include matching criteria.
    """
    advisor_list = ["Dr. Smith", "Prof. Lee", "Dr. Gomez"]
    assignments = {}

    for i, student in enumerate(students):
        advisor = advisor_list[i % len(advisor_list)]  # cycle through advisors
        assignments[student] = advisor

    return assignments
