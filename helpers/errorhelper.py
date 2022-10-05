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
        self.command_help = Help()
        
    def get_error_payload(self, command):
        error = deepcopy(self.error_payload)
        errorBlock_1 = deepcopy(self.error_block_1)
        errorBlock_2 = self.command_help.help(command_name=command)
        error["blocks"].append(errorBlock_1)
        error["blocks"].extend(errorBlock_2)
        return error