# student_data.py

def inputStudents():
    """
    Let the user review default students, then add any new ones.
    Press Enter at the 'Student Name' prompt to finish.
    """
    students = [
        ("Liam Fleck", "Computer Science"),
        ("Robert Wentzel", "Engineering"),
        ("Colby Knorr", "History"),
        ("Karl Marx", "Economics"),
        ("Hugh Man", "Humanities"),
        ("Emily Autumn", "Music")
    ]

    # Show defaults
    print("=== Current Default Students ===")
    for name, major in students:
        print(f"  • {name:<20} → {major}")
    print("\nTo add more students, enter their info below.")
    print("When you’re done, just press Enter at the 'Student Name' prompt.\n")

    # Collect new students
    while True:
        name = input("Student Name (blank to finish): ").strip()
        if not name:
            break

        major = input("Major (case sensitive): ").strip()
        if not major:
            print("  [⚠️  Major cannot be blank. Try again.]\n")
            continue

        students.append((name, major))
        print(f"  [✅  Added] {name} majoring in {major}\n")

    return students
