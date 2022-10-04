from app import db 
from datetime import datetime

class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text())
    points = db.Column(db.Integer)
    deadline = db.Column(db.DateTime)
    created_on = db.Column(db.DateTime, default = datetime.now())
    updated_on = db.Column(db.DateTime, default = datetime.now())


    def __init__(self, description, points, deadline, created_on, updated_on):
        self.description = description
        self.points = points
        self.deadline = deadline
        self.created_on = created_on
        self.updated_on = updated_on


class Assignment(db.Model):

    __tablename__ = 'assignment'

    id = db.Column(db.Integer, primary_key = True)
    isDone = 
    created_on = 
    updated_on = 


    def __init__(self, ):
        self.isDone = isDone
        self.created_on = created_on
        self.updated_on = updated_on

