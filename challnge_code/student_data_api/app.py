import flask
from flask import request, jsonify
import student_generator_v2 as sg

#create a flask app object
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the list of student dictionaries based on a search key, and a value
Input: search_key - key in the dictionary we want to check the value of
       search_value - the value of the key we need to match
Output: list of student dictionaries that match the search criteria
"""
def search_dictionary_list(search_key, search_value):
    #get the list of student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []

    #loop through the dictionaries
    for student_dict in student_dictionaries:
        #determine if the search value matches the key value we are looking for
        if search_value.lower() == student_dict[search_key].lower():
            #add the student dictionary to the results list
            list_of_results.append(student_dict)
    
    #return the results list
    return list_of_results


#create a route/view for the home page of the application
@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

#create end points for the functions we will create
#create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    #get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

#create a route that returns students in a specific major
# api/majors/{major we are looking for}
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major:str):
    #call the search function to get students with this major
    major_students = search_dictionary_list("major", major)
    return jsonify(major_students)

#create a route that returns students of a specific class (freshman, sophomore,...)
# api/class/{the class we are looking for}
@app.route('/api/class/<string:student_class>', methods=['GET'])
def api_students_by_class(student_class:str):
    #call the search function to get students from that class
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)

#create a route that returns a specific studend by ID
@app.route('/api/student/id/<string:id>', methods=['GET'])
def api_get_student_by_id(id:str):
    student = search_dictionary_list("id", id)
    return jsonify(student)

#create a route to return a list of unique majors
@app.route('/api/majors/all', methods=['GET'])
def get_all_majors():
    #create a list to store the majors
    major_list = []

    #get a list of student dictionaries
    student_dictionaries = sg.get_student_dictionaries()

    #use a for loop to iterate through the student list
    for student in student_dictionaries:
    # add the major to the major list if the major is not already in the list
        if student['major'] not in major_list:
            major_list.append(student['major'])

    #sort the list
    major_list.sort()

    #return the list
    return major_list

#run the application
app.run(debug=True)
