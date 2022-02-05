import json


class Die:

    def __init__(self,
        id,
        die_type):
        self.id = id
        self.die_type = die_type
        self.dot_count = 1
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
