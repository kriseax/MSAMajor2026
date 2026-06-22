
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

        #handle errors in data format. line_of_data should have 6 items
        #if error in format then write to a log file
        try:
            if len(student_data) != 6:
                raise Exception(f"Error on line {line_number} of the file. Data has {len(student_data)} items but should have 6.\n")
        except Exception as error:
            continue

        #get student data and create a student object for each student
        first_name = student_data[0]
        last_name = student_data[1]
        major = student_data[2]
        try:
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
        except:
            print(f"Error on line {line_number} of the file")
            continue
        student_id = student_data[5].strip()

        new_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)

    for student in list_of_students:
        student.print_student_data()

main()