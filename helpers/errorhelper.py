from copy import deepcopy
from commands.help import Help

class ErrorHelper:
    error_payload = {
        "response_type": "ephemeral",
        "blocks": []
    }

    error_block_1 = {
        "type": "section",
        "text": {
            "type":"mrkdwn",
            "text": ">Oops! Something went wrong. Please try again with the correct command rules."
        }
    }

    def __init__(self) -> None:
        """
        Constructor to initialize command_help object

        :param: 
        :type: 
        :raise:
        :return: None
        :rtype: None

        """

        self.command_help = Help()
        
    def get_error_payload_blocks(self, command):
        """
        Get compiled error blocks for a particular command

        :param command:  Command name 
        :type command: str
        :raise:
        :return: List of blocks
        :rtype: list[dict[str, Any]]

        """
        error = deepcopy(self.error_payload)
        errorBlock_1 = deepcopy(self.error_block_1)
        errorBlock_2 = self.command_help.help(command_name=command)
        error["blocks"].append(errorBlock_1)
        error["blocks"].extend(errorBlock_2)
        return error["blocks"]

    def get_command_help(self, command):
        """
        Get compiled error blocks for a particular command

        :param command: Command name
        :type command: str 
        :raise:
        :return: Error message for given command name
        :rtype: str

        """
        command_help = ""
        if command == "create":
            command_help = ">To create a task, follow the format: \n*-d* [description of task] *-p* [points of the task] *-ddl* [deadline of the task].\nFor example: */create* *-d* Hey! This is my new task *-p* 100 *-ddl* 15/10/2022"
        elif command == "no_task_id":
            command_help = "The given Task ID does not exist! Please try again..."
        elif command == "task_already_done":
            command_help = "The given Task was already completed!"
        elif command == "task_done":
            command_help = "Congratulations your task is completed now!"
        return command_help
