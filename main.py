# test.py
 
from app import app, db
from db_setup import init_db, db_session,engine

from flask import redirect, url_for, request, make_response, Response
from flask import send_from_directory, jsonify, render_template

from models import Class, Assignment, Grade

from sqlalchemy.sql import select

import os

init_db()

#Class.__table__.drop(engine)
#new_class = Class('CS330', "Internet Programming", "Roman Yasinovskyy", "TH 12:45-2:15")
#We should create a txt file that has a list of these objects
#Assignment.__table__.drop(engine)
db.create_all()

db_list = []

# with open('classfile', 'r') as file:
#     for line in file:
#         course_lst = line.strip().split(', ')
#         db_list.append(course_lst)
#     print(db_list)


# for course in db_list:
#     print(course[0])
#     new_class = Class(course[0], course[1], course[2], course[3])
#     db_session.add(new_class)

# db_list2 = []
# with open('assignments', 'r') as file:
#     for line in file:
#         a_list = line.strip().split(', ')
#         db_list2.append(a_list)
#     print(db_list2)


# for assign in db_list2:
#     print(assign[0])
#     new_assign = Assignment(name=assign[0],class_id = assign[1])
#     db_session.add(new_assign)
#res = db_session.query(Class).filter(Class.name=="Internet Programming").first()
#db_session.delete(res)
#res = db_session.query(Class).all()
#for artist in res:
    #print(artist.name)

db_session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    all_classes = db_session.query(Class).all()
    options = []
    db_session.commit()
    for row in all_classes:
        options.append((row.id, row.name))
    
    if request.method == "GET":
        return render_template("index.html", options = options)
    
    if request.form.get("class"):
        course = request.form.get('class')
        return redirect(url_for('search', courseNum = course))


@app.route('/search', methods=['GET'])
def search():
    courseNum = request.args['courseNum']
    all_classes = db_session.query(Class).all()
    options = []
    for row in all_classes:
        options.append((row.id, row.name))

    if request.method == "GET":
        query = db_session.query(Class).filter_by(id=courseNum).first()
        courseInfo = [query.id, query.name, query.professor, query.time]
    
        assignmentQuery = db_session.query(Assignment).filter_by(class_id = courseNum).all()
        all_assignments = []
        for row in assignmentQuery:
            assignment = row.name
            grade = db_session.query(Grade).filter_by(assignment_id = row.id).order_by(Grade.id.desc()).first()
            all_assignments.append([assignment, grade.grade, row.id])
        db_session.commit()
        return render_template('results.html', options = options, course = courseInfo, results = all_assignments)
     
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        course_num = request.args['courseNum']
        return render_template("addAssignment.html", course_num=course_num)
    name = request.form.get('assignment')
    course_num = request.form.get('courseNum')
    newAssignment =Assignment(name=name,class_id=course_num)
    db_session.add(newAssignment)
    db_session.commit()
    db_session.add(Grade(grade=0, assignment_id = newAssignment.id))
    
    return redirect(url_for('search', courseNum=course_num))

@app.route('/delete', methods=['POST'])
def delete():
    courseNum = request.form.get('course')
    assignmentName = request.form.get('assignmentName')
    deleteAssignment = db_session.query(Assignment).filter_by(name=assignmentName, class_id = courseNum).first()
    db_session.delete(deleteAssignment)
    db_session.commit()
    
    return redirect(url_for('search', courseNum=courseNum))

@app.route('/saveGrade', methods=['POST'])
def saveGrade():
    assignId = request.form.get('assignmentId')
    newGrade = request.form.get('newGrade')
    db_session.add(Grade(grade=newGrade, assignment_id = assignId))
    db_session.commit()
    return redirect(url_for('search', courseNum=request.form.get('course')))


'''I Think this is the kind of stuff that we have to do for the ajax stuff??'''

# @app.route('/save', methods=['POST'])
# def save():
#     with open('file.json', 'wb') as outfile:
#         outfile.write(request.data)
#     return "Success"

# @app.route('/get', methods=['GET'])
# def get():
#     if os.path.isfile('file.json'):
#         with open('file.json', 'r') as infile:
#             data = json.load(infile)
#         response = jsonify(data)
#         return response
#     else:
#         data = []
#         response = jsonify(data)
#         return response
 
if __name__ == '__main__':
    app.run()