from copy import deepcopy

from models import *
from sqlalchemy import desc, func


class Leaderboard:
    """
    This class handles the Create Leaderboard functionality.
    """

    base_leaderboard_block_format = {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "{pos}. <@{userid}> has {points} points!"},
    }

    def __init__(self):
        """
        Constructor to initialize payload object

        :param:
        :type:
        :raise:
        :return: None
        :rtype: None

        """
        self.payload = {"response_type": "ephemeral", "blocks": []}

    def view_leaderboard(self, top_k: int = 5) -> dict:
        """
        Generates leaderboard according to the highest points scorers, returns top five contenders from DB

        :param top_k: Provision to generate top k contenders in leaderboard, default value: 5
        :type top_k: int
        :raise:
        :return: Payload object containing details about the top 5 contenders of SlackPoint
        :rtype: dict[str, Any]

        """
        top_5_leaderboard = (
            Assignment.query.join(Task)
            .join(User)
            .with_entities(
                User.user_id,
                User.slack_user_id,
                func.sum(Task.points).label("total_points"),
            )
            .filter(Assignment.progress == 1)
            .group_by(User.user_id)
            .order_by(desc("total_points"))[:top_k]
        )

        # parse them
        count = 0
        for user in top_5_leaderboard:
            count += 1
            point = deepcopy(self.base_leaderboard_block_format)
            point["text"]["text"] = point["text"]["text"].format(
                pos=count, userid=user.slack_user_id, points=user.total_points
            )
            self.payload["blocks"].append(point)
        if not self.payload["blocks"]:
            self.payload["blocks"].append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">Looks like the competition hasn't started yet :(",
                    },
                }
            )
        return self.payload
