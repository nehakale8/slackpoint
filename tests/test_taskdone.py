# ===== Test marked for later release =====

# from commands.taskdone import TaskDone
# from tests.mockmodels import mock_done_task_1, mock_get_sqlalchemy
# from werkzeug.datastructures import MultiDict
# def test_task_done(mock_get_sqlalchemy, mock_done_task_1):

#     #mocking db call
#     mock_get_sqlalchemy.filter_by.return_value.\
#         all.return_value = [mock_done_task_1]
#     data = MultiDict([
#         ('token', 'ZyiJlmN6ajbgbZP00Bm28ZQ2'), ('team_id', 'T044Z9WJTA6'), ('team_domain', 'slackpoint-test'),
#         ('channel_id', 'C044WG4RZ1T'), ('channel_name', 'test-bot'),
#         ('user_id', 'U045BUHTAUR'), ('user_name', 'vaidyaritwik'),
#         ('command', '/taskdone'), ('text', '1'), ('api_app_id', 'A044ZDK3ZUK'),
#         ('is_enterprise_install', 'false'), ('response_url', 'https://hooks.slack.com/commands/T044Z9WJTA6/4192198014949/aY2DUeIEJwcEGggGTIJNbLy5'),
#         ('trigger_id', '4188537755750.4169336639346.83fc3218e71865c9b613c99cfc8064ca')
#         ])
#     td = TaskDone(data)
#     payload = td.update_points()

#     expected_payload = "The given Task was already completed!"

#     assert payload == expected_payload
