from flask import Flask, request, jsonify
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from commands.viewpoints import ViewPoints
from configuration.env_config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)


@app.route('/')
def basic():
    return 'Hello World'


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


if __name__ == '__main__':
    app.run(debug=True)
