import json


class Shop:

    def __init__(self, dice):
        self.dice = dice
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
