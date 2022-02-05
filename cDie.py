
class DieController:

    def __init__(self):
        pass

    def merge_dice(self,
        sink_die,
        source_die):
        if sink_die.dot_count == source_die.dot_count:
            sink_die.die_count = sink_die.die_count + 1
            source_die.dot_count = 0
            return True
        return False
    
    def apply_effect(self,
        affected_die,
        affect):
        affect(affected_die)
