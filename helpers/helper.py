import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(message):
    """
    This message is used to send a message to our channel

    :param:
    :message: the message object to send
    :return: None
    """
    #print(message)
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    try:
        client.chat_postMessage(
            channel="C04AK8WCY13",
            blocks=message['blocks'],
            text = "Hello!"
        )
    except SlackApiError as e:
        print(f"Error: {e}")