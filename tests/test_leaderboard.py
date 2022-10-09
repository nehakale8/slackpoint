from commands.leaderboard import Leaderboard
from tests.mockmodels import mock_leaderboard_task_5, mock_leaderboard_task_6, mock_get_sqlalchemy

def test_view_leadership_2tasks(
    mock_leaderboard_task_5,
    mock_leaderboard_task_6,
    mock_get_sqlalchemy,
):
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.join.return_value.\
        with_entities.return_value.\
        filter.return_value.\
        group_by.return_value.\
        order_by.return_value = [mock_leaderboard_task_5, mock_leaderboard_task_6]

    # test function
    lb = Leaderboard(slack_user_id="nkale2")
    payload = lb.view_leaderboard()

    # expectation
    expected_payload = {
        'response_type': 'ephemeral',
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '1. <@nkale2> has 18 points!'
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': '2. <@vpmehta> has 12 points!'
                }
            }
        ]
    }

    assert payload == expected_payload


def test_view_leadership_0tasks(
    mock_get_sqlalchemy,
):
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.join.return_value.\
        with_entities.return_value.\
        filter.return_value.\
        group_by.return_value.\
        order_by.return_value = []

    # test function
    lb = Leaderboard(progress=0.0)
    payload = lb.view_leaderboard()

    # expectation
    expected_payload = {
        'response_type': 'ephemeral',
        'blocks': [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">Looks like the competition hasn't started yet :("
                }
            }
        ]
    }

    assert payload == expected_payload
