from commands.taskdone import TaskDone
from commands.leaderboard import Leaderboard
from flask import Flask, make_response, request, jsonify, Response
import json

from commands.help import Help
from models import db
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from commands.viewpoints import ViewPoints
from configuration.env_config import Config
from commands.createtask import CreateTask
from helpers.errorhelper import ErrorHelper
from json import dumps


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


# instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)


@app.route("/slack/interactive-endpoint", methods=["POST"])
def interactive_endpoint():
    """
    All interactive events like button click, input fields are received in this endpoint. We use this endpoint to handle the click event of 'Add task' button of create-task command.

    :param:
    :type:
    :raise:
    :return: Response object with 200 HTTP status
    :rtype: Response

    """
    payload = json.loads(request.form.get("payload"))
    if payload["type"] == "block_actions":
        actions = payload["actions"]
        if len(actions) > 0:
            if actions[0]["action_id"] == "create_action_button":
                # Create Task - button was clicked
                channel_id = payload["container"]["channel_id"]
                user_id = payload["user"]["id"]
                helper = ErrorHelper()
                ct = CreateTask()
                state_values = payload["state"]["values"]
                desc = None
                deadline = None
                points = None
                for _, val in state_values.items():
                    if "create_action_description" in val:
                        desc = val["create_action_description"]["value"]
                    elif "create_action_deadline" in val:
                        deadline = val["create_action_deadline"]["selected_date"]
                    elif "create_action_points" in val:
                        if val["create_action_points"]["selected_option"] is not None:
                            points = val["create_action_points"]["selected_option"][
                                "value"
                            ]
                        else:
                            points = None
                if desc is None or deadline is None or points is None:
                    error_blocks = helper.get_error_payload_blocks("createtask")
                    slack_client.chat_postEphemeral(
                        channel=channel_id, user=user_id, blocks=error_blocks
                    )
                else:
                    blocks = ct.create_task(desc=desc, points=points, deadline=deadline)
                    slack_client.chat_postEphemeral(
                        channel=channel_id, user=user_id, blocks=blocks
                    )
    return make_response("", 200)


@app.route("/")
def basic():
    """
    Health check endpoint

    :param:
    :type:
    :raise:
    :return: 'Hello World' - the official health check response text
    :rtype: str

    """
    return "Hello World"


@app.route("/viewpending", methods=["POST"])
def vpending():
    """
    Endpoint to view the pending tasks

    :param:
    :type:
    :raise:
    :return: Response object with payload object containing details of pending tasks
    :rtype: Response

    """
    data = request.form
    channel_id = data.get("channel_id")
    user_id = data.get("user_id")
    text = data.get("text")

    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    print(jsonify(payload))
    return jsonify(payload)


@app.route("/viewcompleted", methods=["POST"])
def vcompleted():
    """
    Endpoint to view the completed tasks

    :param:
    :type:
    :raise:
    :return: Response object with payload object containing details of completed tasks
    :rtype: Response

    """

    data = request.form
    channel_id = data.get("channel_id")
    user_id = data.get("user_id")
    text = data.get("text")

    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()

    print(payload)

    return jsonify(payload)


@app.route("/taskdone", methods=["POST"])
def taskdone():
    """
    Endpoint to mark a task as completed

    :param:
    :type:
    :raise:
    :return: Response object with payload containing task completion message
    :rtype: Response

    """

    data = request.form
    td = TaskDone(data)
    payload = td.update_points()
    return jsonify(payload)


@app.route("/create", methods=["POST"])
def create():
    """
    Endpoint to create a new task, this endpoint triggers an ephemeral message for the user to enter task details for creation

    :param:
    :type:
    :raise:
    :return: Response object with 200 HTTP status
    :rtype: Response

    """

    ct = CreateTask()
    blocks = ct.create_task_input_blocks()

    data = request.form
    channel_id = data.get("channel_id")
    user_id = data.get("user_id")
    slack_client.chat_postEphemeral(channel=channel_id, user=user_id, blocks=blocks)
    return Response(), 200


@app.route("/help", methods=["POST"])
def help():
    """
    A helper endpoint to view all commands and how to use them

    :param:
    :type:
    :raise:
    :return: Response object with payload object containing details of all commands and how to use them
    :rtype: Response

    """

    h = Help()
    payload = h.help_all()
    return jsonify(payload)


@app.route("/leaderboard", methods=["POST"])
def leaderboard():
    """
    Endpoint to view the leaderboard

    :param:
    :type:
    :raise:
    :return: Response object with payload object containing details of champions leading the SlackPoint challenge
    :rtype: Response

    """
    payload = Leaderboard().view_leaderboard()
    # print(jsonify(payload))
    return jsonify(payload)

@app.route("/summary", methods=["POST"])
def summary():
    """
    Endpoint to view the pending tasks , completed taks and leaderboard

    :param:
    :type:
    :raise:
    :return: Response object with payload object containing details of champions leading the SlackPoint challenge
    :rtype: Response

    """

    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    print("payload", payload)
    pending_tasks = ''
    for task in payload:
        taskid = task[0]
        points = task[3]
        taskname = task[4]
        taskdate = task[5]

        pending_tasks += """ SP-{taskid} ({pts} SlackPoints) {taskname} [Deadline: {dt}]./n""".format(
            taskid=taskid, pts=points, taskname=taskname, dt=taskdate)

    # leaderboard display
    payload = Leaderboard().view_leaderboard()

    leaderboard_msg = ''
    for block in payload['blocks']:

        leaderboard_msg += str(block['text']['text']) + '/n'


    #completed Tasks
    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()

    completed_tasks = ""

    messages = ['Summary is : ',]

    parent_msg = {"blocks": []}
    child_msg = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Summary is :*"
                }
            }
    parent_msg['blocks'].append(child_msg)
    child_msg = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Pending Tasks are:"
                }
            }
    parent_msg['blocks'].append(child_msg)

    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()
    for task in payload['blocks']:

        child_msg = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": task['text']['text']
            }
        }
        parent_msg['blocks'].append(child_msg)
    # completed tasks
    child_msg = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Completed Tasks are:"
        }
    }
    parent_msg['blocks'].append(child_msg)
    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()
    for task in payload['blocks']:
        child_msg = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": task['text']['text']
            }
        }
        parent_msg['blocks'].append(child_msg)
    # Leaderboard
        child_msg = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Leaderboard Status:"
            }
        }
        parent_msg['blocks'].append(child_msg)
        payload = Leaderboard().view_leaderboard()
        for task in payload['blocks']:
            child_msg = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": task['text']['text']
                }
            }
            parent_msg['blocks'].append(child_msg)

    return jsonify(parent_msg)




if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
