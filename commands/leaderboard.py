from copy import deepcopy

from models import *
from sqlalchemy import desc, func


class Leaderboard:
    base_leaderboard_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "{pos}. <@{userid}> has {points} points!"
        }
    }

    def __init__(self, progress: float = 0.0):
        self.progress = progress
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def view_leaderboard(self):
        tasks = []

        tasks_with_progress = Assignment.query.join(Task).join(User). \
            with_entities(User.user_id, User.slack_user_id, func.sum(Task.points).label("total_points")). \
            filter(Assignment.progress == 1). \
            group_by(User.user_id). \
            order_by(desc("total_points"))[:5]
        tasks.extend(tasks_with_progress)
        print(tasks)
        # parse them
        print(tasks)
        count=0
        for task in tasks:
            count+=1
            point = deepcopy(self.base_leaderboard_block_format)
            point["text"]["text"] = point["text"]["text"].format(pos=count, userid=task.slack_user_id,
                                                                 points=task.total_points)
            self.payload["blocks"].append(point)
        if not self.payload["blocks"]:
            self.payload["blocks"].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">Looks like the competition hasn't started yet :("
                }
            })
        return self.payload
