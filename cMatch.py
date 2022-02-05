from mMatch import Match


class MatchController:

    def __init__(self):
        pass

    def create_match(self,
        board_1,
        board_2):
        return Match(board_1, board_2)
    
    def simulate_match(self, match):
        print("Implement MatchController.simulate_match()")
        pass
