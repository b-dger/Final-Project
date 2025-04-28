# student_data.py

def inputStudents():
    students = [
        ("Liam Fleck", "Computer Science"),
        ("Robert Wentzel", "Engineering"),
        ("Colby Knorr", "History"),
        ("Karl Marx", "Economics"),
        ("Hugh Man", "Humanities"),
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
