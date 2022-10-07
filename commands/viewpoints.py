from copy import deepcopy

from models import Task, Assignment


class ViewPoints:
    base_point_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ">SP-{id} ({points} SlackPoints) {description} [Deadline: {deadline}]"
        }
    }

    def __init__(self, progress: float = 0.0):
        self.progress = progress
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def get_list(self):
        tasks = []
        # db query to get all tasks that have progress = progress
        tasks_with_progress = Task.query.join(Assignment). \
            add_columns(Assignment.progress, Task.task_id,
                        Task.points, Task.description, Task.deadline). \
            filter(Assignment.progress == self.progress). \
            all()
        tasks.extend(tasks_with_progress)
        # parse them
        for task in tasks:
            point = deepcopy(self.base_point_block_format)
            point["text"]["text"] = point["text"]["text"].format(id=task.task_id,
                                                                 points=task.points,
                                                                 description=task.description,
                                                                 deadline=task.deadline)
            self.payload["blocks"].append(point)
        if not self.payload["blocks"]:
            self.payload["blocks"].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">Currently there are no SlackPoints available"
                }
            })
        return self.payload
