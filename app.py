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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


# instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)

@app.route('/slack/interactive-endpoint', methods=['POST'])
def interactive_endpoint():
	payload = json.loads(request.form.get('payload'))
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
				for _,val in state_values.items():
					if "create_action_description" in val:
						desc = val["create_action_description"]["value"]
					elif "create_action_deadline" in val:
						deadline = val["create_action_deadline"]["selected_date"]
					elif "create_action_points" in val:
						points = val["create_action_points"]["selected_option"]["value"]
				if desc is None or deadline is None or points is None: 
					error_blocks = helper.get_error_payload("createtask")
					slack_client.chat_postEphemeral(channel=channel_id, user=user_id, blocks=error_blocks)
				else: 
					blocks = ct.create_task(desc=desc, points=points, deadline=deadline)
					slack_client.chat_postEphemeral(channel=channel_id, user=user_id, blocks=blocks)
	return make_response("", 200)

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
	ct = CreateTask()
	blocks = ct.create_task_input_blocks()

	data = request.form
	channel_id = data.get("channel_id")
	user_id = data.get("user_id")
	slack_client.chat_postEphemeral(
		channel=channel_id,
		user=user_id,
		blocks=blocks
	)
	return Response(), 200


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