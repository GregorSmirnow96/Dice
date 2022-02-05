import json


class Relic:

    def __init__(self,
        name,
        image,
        logic):
        self.name = name
        self.image = image
        self.logic = logic
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
