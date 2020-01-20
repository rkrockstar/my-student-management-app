import sys
import os

# Flask is not a module of google app engine. This line of code will include all the site packages in google app engine.

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'venv/Lib/site-packages'))

# Below are the necessary packages for this application.

from flask import Flask, render_template
from flask import request
from studentmanagement_Database_Code import *
app = Flask(__name__)

# This is the homepage.

@app.route('/')
def home():
    return render_template("index.html")

# This is the dashboard page where all the options are displayed.

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/student')
def student():
    return render_template("student database.html")
    list_student_database()

@app.route('/course')
def course():
    return render_template("course database.html")
    list_course_database()

@app.route('/coursesem')
def coursesem():
    return render_template("course schedule database.html")
    list_department_database()

@app.route('/enrollastudent')
def enrollastudent():
    return render_template("enroll a student.html")
    student_id = request.form.get('Studentid')
    student_name = request.form.get('Student Name')
    student_department = request.form.get('Student Department')
    student_courses = request.form.get('Address')
    student_add = request.form.get('Address')
    student_phone = request.form.get('Phone Number')
    insert_student(student_id, student_name, student_department, student_courses, student_add, student_phone)

@app.route('/dropastudent')
def dropastudent():
    return render_template("drop a student.html")
    student_id = request.form.get('Studentid')
    course_id = request.form.get('courseid')
    course_name = request.form.get('coursename')
    year = request.form.get('year')
    semester = request.form.get('semester')
    delete_student(student_id)

@app.route('/liststudentcourse')
def liststudentcourse():
    return render_template("list courses of a student.html")
    student_id = request.form.get('Studentid')
    list_courses_of_a_student(student_id)

@app.route('/liststudentcourseresults')
def liststudentcourseresults():
    return render_template("list courses of a student - results.html")

@app.route('/liststudentinacourse')
def liststudentinacourse():
    return render_template("list student in a course.html")
    course_id = request.form.get('courseid')
    course_name = request.form.get('coursename')
    year = request.form.get('year')
    semester = request.form.get('semester')
    list_students_in_a_course(course_id, course_name, year, semester)

@app.route('/liststudentinacourseresults')
def liststudentinacourseresults():
    return render_template("list student in a course - results.html")

@app.route('/departmentcourses')
def departmentcourses():
    return render_template("list courses of the department.html")
    department_id = request.form.get('departmentid')
    list_department_courses(department_id)

@app.route('/departmentcoursesresults')
def departmentcoursesresults():
    return render_template("list courses of the department - results.html")

@app.route('/studentinfo')
def studentinfo():
    return render_template("studentinfo.html")
    student_id = request.form.get('Studentid')
    student_name = request.form.get('Student Name')
    student_department = request.form.get('Student Department')
    student_add = request.form.get('Address')
    student_phone = request.form.get('Phone Number')
    insert_student(student_id, student_name, student_department, student_add, sadd, student_phone)

@app.route('/editstudentinfo')
def editstudentinfo():
    return render_template("editstudentinfo.html")
    student_id = request.form.get('Studentid')
    student_name = request.form.get('Student Name')
    student_department = request.form.get('Student Department')
    student_add = request.form.get('Address')
    student_phone = request.form.get('Phone Number')
    edit_student_info(student_id, student_name, student_department, student_add, student_phone)

@app.route('/removestudentinfo')
def removestudentinfo():
    return render_template("removestudentinfo.html")
    student_id = request.form.get('Studentid')
    remove_student_info(student_id)

@app.route('/departmentinfo')
def departmentinfo():
    return render_template("departmentinfo.html")
    list_department_database()

@app.route('/editdepartmentinfo')
def editdepartmentinfo():
    return render_template("editdepartmentinfo.html")
    department_id = request.form.get('Department Id')
    department_name = request.form.get('Department Name')
    department_courses = request.form.get('Courses')
    year = request.form.get('year')
    semester = request.form.get('semester')
    edit_quarter_info(department_id, department_name, department_courses, year, semester)

@app.route('/removedepartmentinfo')
def removedepartmentinfo():
    return render_template("removedepartmentinfo.html")
    department_id = request.form.get('Department Id')
    department_name = request.form.get('Department Name')
    department_courses = request.form.get('Courses')
    year = request.form.get('year')
    semester = request.form.get('semester')
    remove_quarter_info(department_id)

@app.route('/courseinfo')
def courseinfo():
    return render_template("courseinfo.html")
    course_id = request.form.get('courseid')
    department_name = request.form.get('Department')
    course_instructor = request.form.get('Instructor')
    year = request.form.get('year')
    semester = request.form.get('semester')
    list_course_database(course_id, department_name, course_instructor, year, semester)

@app.route('/editcourseinfo')
def editcourseinfo():
    return render_template("editcourseinfo.html")
    course_id = request.form.get('courseid')
    department_name = request.form.get('Department')
    course_instructor = request.form.get('Instructor')
    year = request.form.get('year')
    semester = request.form.get('semester')
    edit_course_info(course_id, department_name, course_instructor, year, semester)

@app.route('/removecourseinfo')
def removecourseinfo():
    return render_template("removecourseinfo.html")
    course_id = request.form.get('courseid')
    remove_course_info(course_id)

if __name__ == '__main__':
    app.run()
