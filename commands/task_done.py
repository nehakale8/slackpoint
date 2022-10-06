
from models import *
from helpers.errorhelper import ErrorHelper
import select

class TaskDone:
    def __init__(self, data):
        self.data = data
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }
    
    def update_points(self):

        current_task_id = int(self.data.get('text'))
        
        #check if task id exists
        exists = db.session.query(db.exists().where(Task.task_id == current_task_id)).scalar()
    
        helper = ErrorHelper()
        task_progress = Assignment.query.filter_by(assignment_id = current_task_id, progress = 0.0).all()

        if exists == False:
            return helper.get_command_help("no_task_id") 
        
        #check if task is done
        elif exists == True and len(task_progress) == 0:
            return helper.get_command_help("task_already_done")

        #if task is not done
        elif exists == True and task_progress[0].progress == 0.0:
            db.session.query(Assignment).\
                filter(Assignment.assignment_id == current_task_id).\
                update({'progress': 1.0})
            db.session.commit()
            return helper.get_command_help("task_done")
        pass
    