import json


class DieType:

    def __init__(self,
        name,
        image,
        color,
        tier,
        logic):
        self.name = name
        self.image = image
        self.color = color
        self.tier = tier
        self.logic = logic
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
