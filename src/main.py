# main.py

from advisor_matcher import match_advisors_to_students
from student_data import get_students

def main():
    students = get_students()
    advisor_assignments = match_advisors_to_students(students)
    
    for student, advisor in advisor_assignments.items():
        print(f"{student} is assigned to {advisor}")

if __name__ == "__main__":
    main()
