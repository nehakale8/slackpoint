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


# ===== Test marked for later release ======

# @pytest.fixture
# def mock_done_task_1():
#     my_model = Assignment(
#         user_id=1,
#         assignment_id=1,
#         progress=1.0,
#         assignment_created_on="2022-10-05"
#     )
#     return my_model

# @pytest.fixture
# def mock_done_task_2():
#     my_model = Assignment(
#         user_id=1,
#         assignment_id=1,
#         progress=0.0,
#         assignment_created_on="2022-10-05"
#     )
#     return my_model
# =============================================