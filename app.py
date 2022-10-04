from slack import WebClient
from configuration.env_config import Config
from flask_sqlalchemy import SQLAlchemy
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vansh@localhost/slackpoint"
# db = SQLAlchemy(app)

#instantiating slack client
slack_client = WebClient(os.environ['SLACK_BOT_TOKEN']) #!changed
# slack_events_adapter = SlackEventAdapter(
#     os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app #!changed
# )


# @app.route('/')
# def basic():
#     return 'Hello World'

# @app.route('/message-length', methods=['GET', 'POST'])
# def message_length():
#     data = request.form
#     channel_id = data.get('channel_id')
#     user_id = data.get('user_id')
#     text = data.get('text')
#     client.chat_postEphemeral(channel=channel_id, user=user_id, text="Length of message: " + str(len(text)))
#     return Response(), 200

@app.route('/message-count', methods=['POST'])
def message_count():
    return Response(), 200

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
