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

def list_students(assignments):
    print("\nAvailable Students:")
    for name, _, _ in assignments:
        print(f" - {name}")

def list_advisors(advisorDirectory):
    print("\nAvailable Advisors:")
    for advisor in advisorDirectory:
        print(f" - {advisor}")

def auto_save(assignments):
    """
    Automatically save current assignments to CSV and JSON.
    """
    save_as_csv(assignments)
    save_as_json(assignments)
    print("[💾 Auto-Saved]")

def delete_student(assignments, student_name):
    """
    Deletes a student from the assignments list by name, with confirmation.
    """
    matching_students = [entry for entry in assignments if entry[0] == student_name]
    if not matching_students:
        print(f"[❗ Not Found] {student_name}")
        return

    confirm = input(f"Are you sure you want to delete {student_name}? (yes/no): ").strip().lower()
    if confirm == "yes":
        assignments[:] = [entry for entry in assignments if entry[0] != student_name]
        print(f"[🗑️ Deleted] {student_name}")
        auto_save(assignments)
    else:
        print(f"[❎ Cancelled] {student_name} was not deleted.")

def switch_advisor(assignments, student_name, new_advisor):
    """
    Changes a student's assigned advisor.
    """
    for idx, (name, major, advisor) in enumerate(assignments):
        if name == student_name:
            assignments[idx] = (name, major, new_advisor)
            print(f"[🔄 Switched] {student_name}'s advisor to {new_advisor}")
            auto_save(assignments)
            return
    print(f"[❗ Not Found] {student_name}")

def switch_major(assignments, student_name, new_major):
    """
    Changes a student's major.
    """
    for idx, (name, major, advisor) in enumerate(assignments):
        if name == student_name:
            assignments[idx] = (name, new_major, advisor)
            print(f"[🔄 Switched] {student_name}'s major to {new_major}")
            auto_save(assignments)
            return
    print(f"[❗ Not Found] {student_name}")

def main():
    advisorDirectory = inputAdvisors()
    students = inputStudents()
    assignments = assignAdvisors(students, advisorDirectory)

    while True:
        printAssignments(assignments)

        action = input("\nAction? (save / delete / switch advisor / switch major / quit): ").strip().lower()

        if action == "save":
            save_as_csv(assignments)
            save_as_json(assignments)
            print("[💾 Saved manually]")

        elif action == "delete":
            list_students(assignments)
            name = input("Enter student name to delete: ").strip()
            delete_student(assignments, name)

        elif action == "switch advisor":
            list_students(assignments)
            name = input("Enter student name to switch advisor: ").strip()
            list_advisors(advisorDirectory)
            new_advisor = input("Enter new advisor: ").strip()
            switch_advisor(assignments, name, new_advisor)

        elif action == "switch major":
            list_students(assignments)
            name = input("Enter student name to switch major: ").strip()
            new_major = input("Enter new major: ").strip()
            switch_major(assignments, name, new_major)

        elif action == "quit":
            print("[👋 Exiting]")
            break

        else:
            print("[❓ Unknown action, try again.]")

if __name__ == "__main__":
    main()
