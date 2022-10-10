from commands.leaderboard import Leaderboard
from commands.viewpoints import ViewPoints
from tests.mockmodels import (
    mock_get_sqlalchemy,
    mock_leaderboard_position_1,
    mock_leaderboard_position_2,
    mock_leaderboard_position_3,
    mock_leaderboard_position_4,
    mock_leaderboard_position_5,
    mock_leaderboard_position_6,
)


def test_leaderboard_no_param(
    mock_leaderboard_position_1,
    mock_leaderboard_position_2,
    mock_leaderboard_position_3,
    mock_leaderboard_position_4,
    mock_leaderboard_position_5,
    mock_leaderboard_position_6,
    mock_get_sqlalchemy,
):
    """
    Test the view pending command

    :param mock_leaderboard_position_1: Mocked Leadership object
    :type mock_leaderboard_position_1: Any
    :param mock_leaderboard_position_2: Mocked Leadership object
    :type mock_leaderboard_position_2: Any
    :param mock_leaderboard_position_3: Mocked Leadership object
    :type mock_leaderboard_position_3: Any
    :param mock_leaderboard_position_4: Mocked Leadership object
    :type mock_leaderboard_position_4: Any
    :param mock_leaderboard_position_5: Mocked Leadership object
    :type mock_leaderboard_position_5: Any
    :param mock_leaderboard_position_6: Mocked Leadership object
    :type mock_leaderboard_position_6: Any
    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.join.return_value.with_entities.return_value.filter.return_value.group_by.return_value.order_by.return_value = [
        mock_leaderboard_position_1,
        mock_leaderboard_position_2,
        mock_leaderboard_position_3,
        mock_leaderboard_position_4,
        mock_leaderboard_position_5,
        mock_leaderboard_position_6,
    ]

    # test function
    lb = Leaderboard()
    payload = lb.view_leaderboard()

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "1. <@ritwik> has 33 points!"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "2. <@rishikesh> has 20 points!"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "3. <@neha> has 10 points!"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "4. <@vansh> has 9 points!"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "5. <@mithil> has 5 points!"},
            },
        ],
    }
    assert payload == expected_payload, payload


def test_leaderboard_top_2(
    mock_leaderboard_position_1,
    mock_leaderboard_position_2,
    mock_leaderboard_position_3,
    mock_leaderboard_position_4,
    mock_leaderboard_position_5,
    mock_leaderboard_position_6,
    mock_get_sqlalchemy,
):
    """
    Test the view pending command

    :param mock_leaderboard_position_1: Mocked Leadership object
    :type mock_leaderboard_position_1: Any
    :param mock_leaderboard_position_2: Mocked Leadership object
    :type mock_leaderboard_position_2: Any
    :param mock_leaderboard_position_3: Mocked Leadership object
    :type mock_leaderboard_position_3: Any
    :param mock_leaderboard_position_4: Mocked Leadership object
    :type mock_leaderboard_position_4: Any
    :param mock_leaderboard_position_5: Mocked Leadership object
    :type mock_leaderboard_position_5: Any
    :param mock_leaderboard_position_6: Mocked Leadership object
    :type mock_leaderboard_position_6: Any
    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.join.return_value.with_entities.return_value.filter.return_value.group_by.return_value.order_by.return_value = [
        mock_leaderboard_position_1,
        mock_leaderboard_position_2,
        mock_leaderboard_position_3,
        mock_leaderboard_position_4,
        mock_leaderboard_position_5,
        mock_leaderboard_position_6,
    ]

    # test function
    lb = Leaderboard()
    payload = lb.view_leaderboard(top_k=2)

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "1. <@ritwik> has 33 points!"},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "2. <@rishikesh> has 20 points!"},
            },
        ],
    }
    assert payload == expected_payload, payload


def test_leaderboard_no_completed_task(
    mock_leaderboard_position_1,
    mock_leaderboard_position_2,
    mock_leaderboard_position_3,
    mock_leaderboard_position_4,
    mock_leaderboard_position_5,
    mock_leaderboard_position_6,
    mock_get_sqlalchemy,
):
    """
    Test the view pending command

    :param mock_leaderboard_position_1: Mocked Leadership object
    :type mock_leaderboard_position_1: Any
    :param mock_leaderboard_position_2: Mocked Leadership object
    :type mock_leaderboard_position_2: Any
    :param mock_leaderboard_position_3: Mocked Leadership object
    :type mock_leaderboard_position_3: Any
    :param mock_leaderboard_position_4: Mocked Leadership object
    :type mock_leaderboard_position_4: Any
    :param mock_leaderboard_position_5: Mocked Leadership object
    :type mock_leaderboard_position_5: Any
    :param mock_leaderboard_position_6: Mocked Leadership object
    :type mock_leaderboard_position_6: Any
    :param mock_get_sqlalchemy: Mocked SQL Alchemy object
    :type mock_get_sqlalchemy: Any
    :raise:
    :return: Assert if test case executed successfully
    :rtype: bool

    """
    # Mocking DB call
    mock_get_sqlalchemy.join.return_value.join.return_value.with_entities.return_value.filter.return_value.group_by.return_value.order_by.return_value = (
        []
    )

    # test function
    lb = Leaderboard()
    payload = lb.view_leaderboard()

    # expectation
    expected_payload = {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ">Looks like the competition hasn't started yet :(",
                },
            }
        ],
    }
    assert payload == expected_payload, payload
