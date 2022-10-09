from datetime import datetime
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    """
    This class is a database model for the Task entity.
    """
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    description = db.Column(db.Text())
    points = db.Column(db.Integer)
    deadline = db.Column(db.Date)
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('task_id'),
    )


class Assignment(db.Model):
    """
    This class is a database model for the Assignment entity.
    """
    __tablename__ = 'assignment'
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'))
    assignment_id = db.Column(db.Integer, ForeignKey("task.task_id"), primary_key=True)
    progress = db.Column(db.Float)
    assignment_created_on = db.Column(db.DateTime, default=datetime.now())
    assignment_updated_on = db.Column(db.DateTime)


class User(db.Model):
    """
    This class is a database model for the User entity.
    """
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slack_user_id = db.Column(db.String, unique=True)

    __table_args__ = (
        db.UniqueConstraint('user_id'), 
    )
