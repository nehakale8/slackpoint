from commands.taskdone import TaskDone
from commands.leaderboard import Leaderboard
from flask import Flask, request, jsonify, Response
import re
from commands.help import Help
from models import db
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from commands.viewpoints import ViewPoints
from configuration.env_config import Config
from commands.createtask import CreateTask
from helpers.errorhelper import ErrorHelper


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


# instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)


@app.route('/')
def basic():
    return 'Hello World'


@app.route('/viewpending', methods=["POST"])
def vpending():
    data = request.form
    channel_id = data.get('channel_id')
    user_id = data.get('user_id')
    text = data.get('text')

    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    return jsonify(payload)


@app.route('/viewcompleted', methods=["POST"])
def vcompleted():
    data = request.form
    channel_id = data.get('channel_id')
    user_id = data.get('user_id')
    text = data.get('text')

    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()

    return jsonify(payload)


@app.route('/taskdone', methods=["POST"])
def taskdone():
    data = request.form
    td = TaskDone(data)
    payload = td.update_points()
    return jsonify(payload)


@app.route('/create', methods=["POST"])
def create():
    data = request.form
    text = data.get('text')
    helper = ErrorHelper()
    # match regex of command
    pattern = '^(-d .*) (-p .*) (-ddl .*)$'
    # s = '-d this is my new task -p 100 -ddl 10/10/2022'
    if not bool(re.match(pattern, text)):
        payload = helper.get_error_payload("createtask")
        return jsonify(payload)

    # if command regex is correct, parse the text
    args = re.findall(pattern, text)
    if len(args) == 1 and len(args[0]) == 3:
        desc = args[0][0][3:]
        points = args[0][1][3:]
        deadline = args[0][2][5:]
        print("Desc: ", desc, ", Points: ", points, ", Deadline: ", deadline)
        ct = CreateTask()
        payload = ct.create_task(desc=desc, points=points, deadline=deadline)
        print(payload)
    else:
        payload = helper.get_error_payload("createtask")
    return jsonify(payload)


@app.route('/help', methods=["POST"])
def help():
    h = Help()
    payload = h.help_all()
    return jsonify(payload)


@app.route('/leaderboard', methods=["POST"])
def leaderboard():
    l = Leaderboard()
    payload = l.view_leaderboard()
    return jsonify(payload)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
