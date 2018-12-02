# test.py
 
from app import app, db
from db_setup import init_db, db_session,engine

from flask import redirect, url_for, request, make_response, Response
from flask import send_from_directory, jsonify, render_template

from models import Class, Assignment, Grade

from sqlalchemy.sql import select

init_db()

#Class.__table__.drop(engine)
#new_class = Class('CS330', "Internet Programming", "Roman Yasinovskyy", "TH 12:45-2:15")
#We should create a txt file that has a list of these objects

db.create_all()

# db_list = []

# with open('classfile', 'r') as file:
#     for line in file:
#         course_lst = line.strip().split(',')
#         db_list.append(course_lst)
# print(db_list)


# for course in db_list:
#     print(course[0])
#     new_class = Class(course[0], course[1], course[2], course[3])
#     db_session.add(new_class)



#db_session.add(new_class)
#res = db_session.query(Class).filter(Class.name=="Internet Programming").first()
#db_session.delete(res)
#res = db_session.query(Class).all()
#for artist in res:
    #print(artist.name)

db_session.commit()

rows = []

@app.route('/', methods=['GET', 'POST'])
def index():
    all_classes = db_session.query(Class).all()
    options = []
    for row in all_classes:
        options.append((row.id, row.name))

    if request.form.get("class"):
        course = request.form.get('class')
        query = db_session.query(Class).filter_by(id=course).first()
        name = query.name
        prof = query.professor
        time = query.time
        duedate = request.form.get('dueDate')
        assignment = request.form.get('assignment')

        result = [[name, prof, time, assignment, duedate]]
        rows.append(result)

        return render_template("index.html", options=options, results = rows)

    return render_template("index.html", options=options)

    #Getting information to create table

        # return redirect(url_for("table", results=result))

@app.route('/results', methods=['GET', 'POST'])
def table():
    if request.method == "POST":
        
        return redirect(url_for('index'))


 
 
# @app.route('/')
# def test():
#     return "Welcome to Flask!"
 
if __name__ == '__main__':
    app.run()