
from Student import Student

def main():
    #Create 2 instances of Student
    list_of_students = []


    #create a file handler
    file = open("students.csv", "r")

    #create variable to keep track of line in file that we are reading
    line_number = 0
    #read file line by line in for loop
    for line_of_data in file:
        line_number += 1
        #skip first line in csv file
        if line_number == 1:
            continue
        
        #split the line of data at the comma
        student_data = line_of_data.split(",")

        #get student data and create a student object for each student
        first_name = student_data[0]
        last_name = student_data[1]
        major = student_data[2]
        credit_hours = int(student_data[3])
        gpa = float(student_data[4])
        student_id = student_data[5].strip()

        new_student = Student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)



    for student in list_of_students:
        student.print_student_data()

main()
