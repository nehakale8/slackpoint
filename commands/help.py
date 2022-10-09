from copy import deepcopy

class Help:
    """
    This class handles the Help functionality.
    """
    commands_dictionary = {}

    command_help = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "{command_help}"
        }
    }

    def __init__(self):
        """
        Constructor to initialize command dictionary and payload object

        :param: 
        :type: 
        :raise:
        :return: None
        :rtype: None

        """
        self.commands_dictionary["createtask"] = ["*Create Task*", ">To create a task, just try the command */create-task* and you would receive a message from Slack to fill out the details of the task.\n>Enter the description, deadline and the points of the task.\n>For example:\n>*Description*: Hey! This is my new task\n>*Deadline*: 12/31/2022 (just select a date from the date picker)\n>*Points*: 5 (select a point from 1 to 5)\n>And that's it! You should receive a reply from Slack with the generated *Task ID*."]
        self.commands_dictionary["viewcompleted"] = ["*View Completed Tasks*", ">To view completed tasks, just try the command */view-completed*, and there you go! SlackPoint would show you a list of completed tasks."]
        self.commands_dictionary["viewpending"] = ["*View Pending Task*", ">To view pending tasks, just try the command */view-pending*, and there you go! SlackPoint would show you a list of completed tasks."]
        self.commands_dictionary["leaderboard"] = ["*Leaderboard*", ">To view the leaderboard, just try the command */leaderboard*, and SlackPoint would show you the top five contenders!"]
        self.commands_dictionary["taskdone"] = ["*Complete Task*", ">To mark a task as Completed, just try the command */task-done* <Task ID>, and now you are one step closer at being one of the top five contenders!"]
        self.commands_dictionary["help"] = ["*Help*", ">Well, you are viewing it. You don't need my help in that case :D"]

        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def help_all(self):
        """
        Creates a payload with the help details for all commands

        :param: 
        :type: 
        :raise:
        :return: Payload object containing helper details of all commands
        :rtype: dict[str, Any]

        """
        response_payload = deepcopy(self.payload)
        for name in self.commands_dictionary.keys():
            blocks = self.help(name)
            response_payload["blocks"].extend(blocks)
        return response_payload

    def help(self, command_name):
        """
        Creates a payload blocks for particular command

        :param command_name: Command name
        :type command_name: str
        :raise:
        :return: Blocks list containing details of a particular command provided in parameter
        :rtype: list

        """
        blocks = []
        command_name_block = deepcopy(self.command_help)
        command_help_desc_block = deepcopy(self.command_help)
        command_help = self.commands_dictionary.get(command_name)
        command_name_block["text"]["text"] = command_name_block["text"]["text"].format(command_help=command_help[0])
        command_help_desc_block["text"]["text"] = command_help_desc_block["text"]["text"].format(command_help=command_help[1])
            
        blocks.append(command_name_block)
        blocks.append(command_help_desc_block) 
        return blocks
