from copy import deepcopy

class Help:
    commands_dictionary = {}

    command_help = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "{command_help}"
        }
    }

    def __init__(self):
        self.commands_dictionary["createtask"] = ["*Create Task*", ">To create a task, just try the command *\create-task* and you would receive a message from Slack to fill out the details of the task.\n>Enter the description, deadline and the points of the task.\n>For example:\n>Description: Hey! This is my new task\n>Deadline: 12/31/2022 (just select a date from the date picker)\n>Points: 5 (select a point from 1 to 5)\n>And that's it! You should receive a reply from Slack with the generated Task ID."]
        self.commands_dictionary["viewpoints"] = ["*View Points*", ">To view points, follow the format:"]
        self.commands_dictionary["completetask"] = ["*Complete Task*", ">To complete a task, follow the format:"]
        self.commands_dictionary["leaderboard"] = ["*Leaderboard*", ">To view the leaderboard:"]
        self.commands_dictionary["help"] = ["*Help*", ">Well, you are viewing it. You don't need my help in that case :D"]

        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def help_all(self):
        response_payload = deepcopy(self.payload)
        for name in self.commands_dictionary.keys():
            blocks = self.help(name)
            response_payload["blocks"].extend(blocks)
        return response_payload

    def help(self, command_name):
        blocks = []
        command_name_block = deepcopy(self.command_help)
        command_help_desc_block = deepcopy(self.command_help)
        command_help = self.commands_dictionary.get(command_name)
        command_name_block["text"]["text"] = command_name_block["text"]["text"].format(command_help=command_help[0])
        command_help_desc_block["text"]["text"] = command_help_desc_block["text"]["text"].format(command_help=command_help[1])
            
        blocks.append(command_name_block)
        blocks.append(command_help_desc_block) 
        return blocks
