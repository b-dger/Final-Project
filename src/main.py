# main.py

from advisor_matcher import inputAdvisors, assignAdvisors
from student_data import inputStudents
from fileio import save_as_csv, save_as_json

def printAssignments(assignments):
    print("\n=== Student–Advisor Assignments ===")
    for name, major, advisor in assignments:
        print(f"• {name:<20} | {major:<17} | {advisor}")
    print()

def main():
    advisorDirectory = inputAdvisors()
    students = inputStudents()
    assignments = assignAdvisors(students, advisorDirectory)
    printAssignments(assignments)
    save_as_csv(assignments)
    save_as_json(assignments)

if __name__ == "__main__":
    main()