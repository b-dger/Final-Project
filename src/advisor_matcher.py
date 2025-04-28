# advisor_matcher.py

def inputAdvisors():
    """
    Let the user review default advisors, then add any new ones.
    Press Enter at the 'Advisor Name' prompt to finish.
    """
    advisorDirectory = {
        "Computer Science": "Dr. Dang",
        "Physics": "Dr. Upton",
        "Engineering": "Dr. Lee",
        "History": "Dr. Van Wie",
        "Foreign Language": "Profesora Rubio",
        "Mathematics": "Professor Schanker"
    }

    # Show defaults
    print("=== Current Default Advisors ===")
    for major, advisor in advisorDirectory.items():
        print(f"  • {major:<17} → {advisor}")
    print("\nTo add more advisors, enter their info below.")
    print("When you’re done, just press Enter at the 'Advisor Name' prompt.\n")

    # Collect new advisors
    while True:
        advisor = input("Advisor Name (blank to finish): ").strip()
        if not advisor:
            break

        major = input("Major they advise: ").strip()
        if not major:
            print("  [⚠️  Major cannot be blank. Try again.]\n")
            continue

        advisorDirectory[major] = advisor
        print(f"  [✅  Added] {major} will now be advised by {advisor}\n")

    return advisorDirectory

def assignAdvisors(students, advisorDirectory):
    """
    Assign each (name, major) to an advisor.
    Returns a sorted list of (name, major, advisor).
    """
    # sort students alphabetically by name
    students_sorted = sorted(students, key=lambda s: s[0])
    assignments = []
    for name, major in students_sorted:
        advisor = advisorDirectory.get(major, "No advisor assigned")
        assignments.append((name, major, advisor))
    return assignments