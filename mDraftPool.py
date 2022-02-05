
class DraftPool:

    def __init__(self, die_set):
        self.dice_by_index = {}

        die_index = 0
        for die in die_set.dice:
            self.dice_by_index[die_index] = die
            die_index = die_index + 1
