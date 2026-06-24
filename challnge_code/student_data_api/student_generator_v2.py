
from Student import Student

"""
Function to return a list of student objects
Input: none
Output: list of student objects
"""
def load_students() -> list[Student]:
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
    
    return list_of_students

"""
Function to convert student objects into student dictionaries
Input: lisst of student objects
Output: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create an empty list to store the dictionaries
    student_dictionary_list = []

    #loop through the list of students and write each students data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        student_dictionary = {}

        #make entries into the dictionary using the student properties
        #firstname, last name, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_ID()

        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)

    #return the list of dictionaries
    return student_dictionary_list

"""
Function to get student dictionaries
Input: None
Output: a list of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries


