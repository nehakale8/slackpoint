
from models import *
from helpers.errorhelper import ErrorHelper


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
        
        query = Task.query.outerjoin(Assignment). \
            add_columns(Assignment.assignment_id, Assignment.progress, Task.task_id,
                        Task.points ,Task.description, Task.deadline). \
                            all()
        # print("query: ",query)
        helper = ErrorHelper()

        progess = query[0].progress

        # if not exists:
        if exists == False:
            return helper.get_command_help("no_task_id") 
        #check if task is done
        elif exists == True and progess == 1.0:
            return helper.get_command_help("task_done")
        # print(query[0].task_id)
        # points = self.get_task_points()

        # channel_id = data.get('channel_id')
        # user_id = data.get('user_id')
        # text = data.get('text')


        # message = "User x completed task y successfully! current points: "
        pass
    