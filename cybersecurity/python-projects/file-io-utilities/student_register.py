import os

folder = os.path.dirname (os.path.abspath(__file__))
file_path = os.path.join (folder, 'reg_form.txt')

num_students = int(input("Enter the number of students registering: "))

with open (file_path, 'w') as file:
    for i in range(num_students):
        student_id = input("Enter student ID for student: ") 
        file.write (student_id + "\n")
        file.write (".............................................................................................\n")
