
from models import *


class TaskDone:
    base_point_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ">User {user_id} completed task {task_id}... Now stands on {points} - SP"
        }
    }
    def __init__(self, data):
        self.data = data
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }
    

    def get_task_points():
        

        #parse task_id
        pass
    
    #get points for corresponding task
    # def get_points(self):
    #     #query db for points of corresponding task
    #     pass

    def update_points(self):

        #check if task id exists
        task = Task()
        current_task_id = self.data.get('text')
        current_task_id = int(current_task_id)
        exists = db.session.query(db.exists().where(Task.task_id == current_task_id)).scalar()
        # if not exists:
        if exists == False:
            return Response()
        #check if task is not done

        # points = self.get_task_points()

        # channel_id = data.get('channel_id')
        # user_id = data.get('user_id')
        # text = data.get('text')


        # message = "User x completed task y successfully! current points: "
        pass
    