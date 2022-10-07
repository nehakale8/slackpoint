from copy import deepcopy
import random
from models import *

class CreateTask:
    base_create_task_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ">{greeting}! Your task SP-{id} was created successfully."
        }
    }

    greetings = ["Awesome", "Great", "Congratulations", "Well done", "Let's go"]

    def __init__(self):
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def create_task_input_blocks(self):
        block_description = {
            "type": "input",
            "element": {
                "type": "plain_text_input",
                "action_id": "create_action_description"
            },
            "label": {
                "type": "plain_text",
                "text": "Description",
                "emoji": True
            }
        }
        block_deadline = {
            "type": "input",
            "element": {
                "type": "datepicker",
                "initial_date": "2022-01-01",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a date",
                    "emoji": True
                },
                "action_id": "create_action_deadline"
            },
            "label": {
                "type": "plain_text",
                "text": "Deadline",
                "emoji": True
            }
        }
        block_points = {
            "type": "input",
            "element": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "1",
                            "emoji": False
                        },
                        "value": "1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "2",
                            "emoji": False
                        },
                        "value": "2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "3",
                            "emoji": False
                        },
                        "value": "3"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "4",
                            "emoji": False
                        },
                        "value": "4"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "5",
                            "emoji": False
                        },
                        "value": "5"
                    }
                ],
                "action_id": "create_action_points"
            },
            "label": {
                "type": "plain_text",
                "text": "Points",
                "emoji": True
            }
        }
        block_actions_button = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Create task"
            },
            "action_id": "create_action_button"
        }
        block_actions = {
            "type": "actions",
            "elements": []
        }
        block_actions["elements"].append(block_actions_button)

        blocks = []
        blocks.append(block_description)
        blocks.append(block_deadline)
        blocks.append(block_points)
        blocks.append(block_actions)
        return blocks
        
    def create_task(self, desc, points, deadline):
        # DB call to add task, returns id
        task = Task()
        task.description = desc
        task.points = points
        task.deadline = deadline
        db.session.add(task)
        db.session.commit()
        db.session.refresh(task)

        # task id
        id = task.task_id

        # add the task in assignment, without user assignment
        assignment = Assignment()
        assignment.assignment_id = id
        assignment.progress = 0
        db.session.add(assignment)
        db.session.commit()

        response = deepcopy(self.base_create_task_block_format)
        response["text"]["text"] = response["text"]["text"].format(greeting=random.choice(self.greetings), id=id)
        self.payload["blocks"].append(response)
        return self.payload["blocks"]
