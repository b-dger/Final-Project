# main.py

try:
    from advisor_matcher import inputAdvisors, assignAdvisors
    from student_data import inputStudents
    from fileio import save_as_csv, save_as_json
except ImportError as e:
    print(f"Error importing modules: {e}")
    exit(1)

def printAssignments(assignments):
    print("\n=== Student–Advisor Assignments ===")
    for name, major, advisor in assignments:
        print(f"• {name:<20} | {major:<17} | {advisor}")
    print()

def delete_student(assignments, student_name):
    """
    Deletes a student from the assignments list by name.
    """
    before = len(assignments)
    assignments[:] = [entry for entry in assignments if entry[0] != student_name]
    after = len(assignments)
    if before == after:
        print(f"[❗ Not Found] {student_name}")
    else:
        print(f"[🗑️ Deleted] {student_name}")

def switch_advisor(assignments, student_name, new_advisor):
    """
    Changes a student's assigned advisor.
    """
    for idx, (name, major, advisor) in enumerate(assignments):
        if name == student_name:
            assignments[idx] = (name, major, new_advisor)
            print(f"[🔄 Switched] {student_name}'s advisor to {new_advisor}")
            return
    print(f"[❗ Not Found] {student_name}")

def main():
    advisorDirectory = inputAdvisors()
    students = inputStudents()
    assignments = assignAdvisors(students, advisorDirectory)

    while True:
        printAssignments(assignments)

        action = input("\nAction? (save / delete / switch / quit): ").strip().lower()

        if action == "save":
            save_as_csv(assignments)
            save_as_json(assignments)
        elif action == "delete":
            name = input("Enter student name to delete: ").strip()
            delete_student(assignments, name)
        elif action == "switch":
            name = input("Enter student name to switch advisor: ").strip()
            new_advisor = input("Enter new advisor: ").strip()
            switch_advisor(assignments, name, new_advisor)
        elif action == "quit":
            print("[👋 Exiting]")
            break
        else:
            print("[❓ Unknown action, try again.]")

if __name__ == "__main__":
    main()
