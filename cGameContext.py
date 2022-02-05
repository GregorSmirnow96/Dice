from mBoard import Board
from mDieType import DieType
from mGameContext import GameContext
from mPool import Pool
import mColors as Colors
import mGameContext


def create_game():
    types = [
        DieType("T1-R", None, Colors.RED,   1, lambda: print("T1-R")),
        DieType("T1-G", None, Colors.GREEN, 1, lambda: print("T1-B")),
        DieType("T1-B", None, Colors.BLUE,  1, lambda: print("T1-G")),
        DieType("T2-R", None, Colors.RED,   2, lambda: print("T2-R")),
        DieType("T2-G", None, Colors.GREEN, 2, lambda: print("T2-G")),
        DieType("T2-B", None, Colors.BLUE,  2, lambda: print("T2-B")),
        DieType("T3-R", None, Colors.RED,   3, lambda: print("T3-R")),
        DieType("T3-G", None, Colors.GREEN, 3, lambda: print("T3-G")),
        DieType("T3-B", None, Colors.BLUE,  3, lambda: print("T3-B"))
    ]

    tier_counts = {
        1: 15,
        2: 8,
        3: 3
    }

    augments = []

    pool = Pool(types, tier_counts, augments)

    return GameContext(pool)
