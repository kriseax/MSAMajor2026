from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url:str):
    #make a request
    response = requests.get(url)

    #convert the format to JSON
    response_json = response.json()

    #return the response
    return response_json

#create a route for the website index/root/homepage. Will display all student data
@app.route('/', methods=['GET'])
def index():
    #make a request to the student data api for all students
    url = "http://127.0.0.1:5000/api/students/all"

    #get the student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data=student_data)

#create a route for the majors search page to respond to get requests
@app.route('/majors', methods=['GET'])
def majors_get():
    #get the list of majors
    url = "http://127.0.0.1:5000/api/majors/all"
    major_list = get_student_data(url)

    #send the list of majors to the majors template to populate the menu
    return render_template('majors.html', major_list=major_list)

#create a route for the majors search page to respon to 
# POST requests after the form is submitted


#run the flask app
app.run(port=5001)
