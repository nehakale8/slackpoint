from commands.viewpoints import ViewPoints
from tests.mockmodels import (
    mock_pending_task_1,
    mock_pending_task_2,
    mock_get_sqlalchemy,
)


def test_view_pending_2tasks(
    mock_pending_task_1,
    mock_pending_task_2,
    mock_get_sqlalchemy,
):
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.add_columns.return_value.filter.return_value.all.return_value = [
        mock_pending_task_1,
        mock_pending_task_2,
    ]

    # test function
    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">SP-1 (10 SlackPoints) This is Task 1 [Deadline: 2022-10-24]",
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">SP-2 (2 SlackPoints) This is Task 2 [Deadline: 2022-10-26]",
                },
            },
        ],
    }

    assert payload == expected_payload


def test_view_pending_0tasks(
    mock_get_sqlalchemy,
):
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.add_columns.return_value.filter.return_value.all.return_value = (
        []
    )

    # test function
    vp = ViewPoints(progress=0.0)
    payload = vp.get_list()

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">Currently there are no SlackPoints available",
                },
            }
        ],
    }

    assert payload == expected_payload
