from copy import deepcopy


class ViewPoints:
    base_point_block_format = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ">{id} ({points} SP) {description}"
        }
    }

    def __init__(self, progress: float = 0.0):
        self.progress = progress
        self.payload = {
            "response_type": "ephemeral",
            "blocks": []
        }

    def get_list(self):
        # db query to get all tasks that have progress = progress
        # parse them
        for i in [2, 3]:
            point = deepcopy(self.base_point_block_format)
            point["text"]["text"] = point["text"]["text"].format(id=i, points=i*3, description=f"This is task {i}")
            self.payload["blocks"].append(point)

        return self.payload
