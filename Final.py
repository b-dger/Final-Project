# input map of majors to advisors
def inputAdvisors():
    advisorDirectory = { # I made some default advisors so you wont have to make new ones everytime you run the code if you dont want
        "Computer Science": "Dr. Dang",
        "Physics": "Dr. Upton",
        "Engineering": "Dr. Lee",
        "History": "Dr. Van Wie",
        "Foreign Language": "Profesora Rubio",
        "Mathmatics": "Proffesor Schanker"
    }
    print("Enter advisor names and the majors they advise (leave name blank and press enter when done):")
    while True:
        advisor = input("Advisor Name: ")
        if advisor.lower() == '':
            break
        major = input("Major they advise: ")
        advisorDirectory[major] = advisor
    return advisorDirectory

# Function to input students
def inputStudents():
   students = [ #I made some default people too
    ("Liam Fleck", "Computer Science"),
    ("Robert Wentzel", "Engineering"),
    ("Colby Knorr", "History"),
    ("Karl Marx", "Economics")
    ("Hugh Man", "Humanities")
    ("Emily Autumn", "Music")
   ]
   print("Enter students' full name and their major (leave name blank and press enter when done):")
   while True:
       name = input("Student Name: ")
       if name.lower() == '':
           break
       major = input("Major (case sensitive): ")
       students.append((name, major))
   return students


# Function to assign advisors
def assignAdvisors(students):
   assignments = []
   for name,major in students:
       advisor = advisorDirectory.get(major, "No advisor assigned")
       assignments.append((name, major, advisor))
   return assignments


# Function to display assignments
def printAssignments(assignments):
   print("\nStudent Advisor Assignments:")
   for name, major, advisor in assignments:
       print(f"Student: {name} | Major: {major} | Advisor: {advisor}")


# Main function
if __name__ == "__main__":
    advisorDirectory = inputAdvisors()
    students = inputStudents()
    assignments = assignAdvisors(students)
    printAssignments(assignments)
