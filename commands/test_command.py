from app import slack_client, slack_events_adapter


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    pass
