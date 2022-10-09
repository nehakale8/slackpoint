import pytest

from models import Task, Assignment


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy.model._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def mock_my_model():
    my_model = Task(
        task_id="1",
        description="This is Task 1",
        points=10,
        deadline="2022-08-24"
    )
    return my_model


@pytest.fixture
def mock_pending_task_1():
    my_model = Task(
        task_id=1,
        description="This is Task 1",
        points=10,
        deadline="2022-10-24"
    )
    return my_model


@pytest.fixture
def mock_pending_task_2():
    my_model = Task(
        task_id=2,
        description="This is Task 2",
        points=2,
        deadline="2022-10-26"
    )
    return my_model


@pytest.fixture
def mock_completed_task_3():
    my_model = Task(
        task_id=3,
        description="This is Task 3",
        points=5,
        deadline="2022-08-24"
    )
    return my_model


@pytest.fixture
def mock_completed_task_4():
    my_model = Task(
        task_id=4,
        description="This is Task 4",
        points=5,
        deadline="2022-08-26"
    )
    return my_model


@pytest.fixture
def mock_leaderboard_position_1(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "ritwik"
    my_model.total_points = 33
    return my_model


@pytest.fixture
def mock_leaderboard_position_2(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "rishikesh"
    my_model.total_points = 20
    return my_model


@pytest.fixture
def mock_leaderboard_position_3(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "neha"
    my_model.total_points = 10
    return my_model


@pytest.fixture
def mock_leaderboard_position_4(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "vansh"
    my_model.total_points = 9
    return my_model


@pytest.fixture
def mock_leaderboard_position_5(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "mithil"
    my_model.total_points = 5
    return my_model


@pytest.fixture
def mock_leaderboard_position_6(mocker):
    my_model = mocker.Mock()
    my_model.slack_user_id = "dani"
    my_model.total_points = 2
    return my_model
