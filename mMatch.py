import json


class Match:

    def __init__(self,
        board_1,
        board_2):
        self.board_1 = board_1
        self.board_2 = board_2
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
