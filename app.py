from commands.task_done import TaskDone
from flask import Flask, request, jsonify, Response
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from datetime import datetime
from commands.viewpoints import ViewPoints
from configuration.env_config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db.init_app(app)


#instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)
                                                
@app.route('/')
def basic():
    return 'Hello World'

# @app.route('/message-length', methods=['GET', 'POST'])
# def message_length():
#     data = request.form
#     channel_id = data.get('channel_id')
#     user_id = data.get('user_id')
#     text = data.get('text')
#     client.chat_postEphemeral(channel=channel_id, user=user_id, text="Length of message: " + str(len(text)))
#     return Response(), 200

# @app.route('/message-count', methods=['POST'])
# def message_count():
#     data = request.form
#     channel_id = data.get('channel_id')
#     user_id = data.get('user_id')
#     text = data.get('text')

    #take user_id
    #text to int

    #fetch points for that task id
    task_points = 0 #points from above fetch

    #update points in user table
    #update operation

    # print("Text: ",text)
    # return Response(), 200

@app.route('/vpending', methods=["POST"])
def vpending():
    data = request.form
    channel_id = data.get('channel_id')
    user_id = data.get('user_id')
    text = data.get('text')

    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    return jsonify(payload)


@app.route('/vcompleted', methods=["POST"])
def vcompleted():
    data = request.form
    channel_id = data.get('channel_id')
    user_id = data.get('user_id')
    text = data.get('text')

    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()

    return jsonify(payload)


@app.route('/task-done', methods=["POST"])
def taskdone():
    data = request.form
    # print(type(data))
    # channel_id = data.get('channel_id')
    # user_id = data.get('user_id')
    # text = data.get('text')
    # print(text)
    td = TaskDone(data)
    td.update_points()
    return Response(), 200



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
