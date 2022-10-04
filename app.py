from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from configuration.env_config import Config


app = Flask(__name__)

#instantiating slack client
slack_client = WebClient(Config.SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(
    Config.SLACK_SIGNING_SECRET, "/slack/events", app
)


@app.route('/')
def basic():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
