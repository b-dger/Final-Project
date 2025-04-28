# advisor_matcher.py

def inputAdvisors():
    advisorDirectory = {
        "Computer Science": "Dr. Dang",
        "Physics": "Dr. Upton",
        "Engineering": "Dr. Lee",
        "History": "Dr. Van Wie",
        "Foreign Language": "Profesora Rubio",
        "Mathematics": "Professor Schanker"
    }
    print("Enter advisor names and the majors they advise (leave name blank and press enter when done):")
    while True:
        advisor = input("Advisor Name: ")
        if advisor.lower() == '':
            break
        major = input("Major they advise: ")
        advisorDirectory[major] = advisor
    return advisorDirectory

def assignAdvisors(students, advisorDirectory):
    assignments = []
    for name, major in students:
        advisor = advisorDirectory.get(major, "No advisor assigned")
        assignments.append((name, major, advisor))
    return assignments