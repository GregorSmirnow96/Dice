
class DraftPoolController:

    def __init__(self):
        pass

    def create_draft_pool(self):
        pass

    def pop_die_at_index(self, pool, index):
        die = pool[index]
        pool.remove(die)
        return die
