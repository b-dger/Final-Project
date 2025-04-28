# main.py

from advisor_matcher import inputAdvisors, assignAdvisors
from student_data import inputStudents

def printAssignments(assignments):
    print("\nStudent Advisor Assignments:")
    for name, major, advisor in assignments:
        print(f"Student: {name} | Major: {major} | Advisor: {advisor}")

def main():
    advisorDirectory = inputAdvisors()
    students = inputStudents()
    assignments = assignAdvisors(students, advisorDirectory)
    printAssignments(assignments)

if __name__ == "__main__":
    main()
