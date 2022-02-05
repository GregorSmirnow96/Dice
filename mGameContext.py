
class GameContext:

    def __init__(self, pool):
        self.pool = pool
        self.players = []
        self.match_history_per_player = {}

    def add_player(self, player):
        self.players.append(player)
