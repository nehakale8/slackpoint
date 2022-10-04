from app import db 
from datetime import datetime

class Task(db.Model):

    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    description = db.Column(db.Text())
    points = db.Column(db.Integer)
    deadline = db.Column(db.DateTime)
    created_on = db.Column(db.DateTime, default = datetime.now())
    updated_on = db.Column(db.DateTime)

class Assignment(db.Model):

    __tablename__ = 'assignment'

    assignment_id = db.Column(db.Integer, db.ForeignKey("task.task_id"))
    progress = db.Column(db.Float)
    created_on = db.Column(db.DateTime, db.ForeignKey("task.created_on"), default = datetime.now())
    updated_on = db.Column(db.DateTime, db.ForeignKey("task.updated_on"))

class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_points = db.Column(db.Integer, db.ForeignKey("task.points"))
