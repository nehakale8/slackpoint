from commands.viewpoints import ViewPoints
from tests.mockmodels import (
    mock_completed_task_3,
    mock_completed_task_4,
    mock_get_sqlalchemy,
)


def test_view_completed_2tasks(
    mock_completed_task_3,
    mock_completed_task_4,
    mock_get_sqlalchemy,
):
    """
    Test the view pending command

    :param mock_completed_task_3: Mocked Task object 1
    :type mock_completed_task_3: Task
    :param mock_completed_task_4: Mocked Task object 2
    :type mock_completed_task_4: Task
    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.add_columns.return_value.filter.return_value.all.return_value = [
        mock_completed_task_3,
        mock_completed_task_4,
    ]

    # test function
    vp = ViewPoints(progress=1.0)
    payload = vp.get_list()

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">SP-3 (5 SlackPoints) This is Task 3 [Deadline: 2022-08-24]",
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">SP-4 (5 SlackPoints) This is Task 4 [Deadline: 2022-08-26]",
                },
            },
        ],
    }

    assert payload == expected_payload


def test_view_completed_0tasks(
    mock_get_sqlalchemy,
):
    """
    Test the view pending command

    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.add_columns.return_value.filter.return_value.all.return_value = (
        []
    )

    # test function
    vp = ViewPoints(progress=1.0)
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
