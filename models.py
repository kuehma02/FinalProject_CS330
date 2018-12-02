from app import db


class Class(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String, nullable=False)
    professor = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)

    def __init__(self, id, name, professor, time):
        self.id=id
        self.name=name
        self.professor=professor
        self.time=time
    def __repr__(self):
        return "Course Num: {}, Course Name: {}, Professor: {}, Time: {}".format(self.id, self.name, self.professor, self.time)

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    due_date = db.Column(db.DateTime)
 
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))
    course = db.relationship("Class", backref=db.backref(
        "coursename", order_by=id))
        

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer)

    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
    assignment = db.relationship('Assignment', backref=db.backref('grade', uselist=False))