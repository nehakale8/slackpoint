from copy import deepcopy


class ErrorHelper:
    ErrorPayload = {
        "response_type": "ephemeral",
        "blocks": []
    }

    ErrorBlock_1 = {
        "type": "section",
        "text": {
            "type":"mrkdwn",
            "text": ">Oops! Something went wrong. Please try again with the correct command rules."
        }
    }

    ErrorBlock_2 = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "{command_help}"
        }
    }

    def __init__(self) -> None:
        pass
        
    def get_error_payload(self, command):
        error = deepcopy(self.ErrorPayload)
        errorBlock_1 = deepcopy(self.ErrorBlock_1)
        errorBlock_2 = deepcopy(self.ErrorBlock_2)
        errorBlock_2["text"]["text"] = errorBlock_2["text"]["text"].format(command_help=self.get_command_help(command))
        error["blocks"].append(errorBlock_1)
        error["blocks"].append(errorBlock_2)
        return error

    def get_command_help(self, command):
        command_help = ""
        if command == "create":
            command_help = ">To create a task, follow the format: \n*-d* [description of task] *-p* [points of the task] *-ddl* [deadline of the task].\nFor example: */create* *-d* Hey! This is my new task *-p* 100 *-ddl* 15/10/2022"
        elif command == "no_task_id":
            command_help = "The given Task ID does not exist! Please try again..."
        elif command == "task_done":
            command_help = "The given Task was already completed!"
        return command_help
