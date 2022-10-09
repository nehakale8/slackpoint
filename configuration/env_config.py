import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_ECHO = True
    # SLACK API key:
    SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")
