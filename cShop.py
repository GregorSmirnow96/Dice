from mPool import Pool
from mShop import Shop
import mGameContext as GameContext
import random


def create_shop(
    pool,
    tier,
    shop_size=6):
    odds_per_tier = {}
    if tier == 1:
        odds_per_tier = { 1: 1, 2: 0, 3: 0 }
    elif tier == 2:
        odds_per_tier = { 1: 0, 2: 1, 3: 0 }
    else:
        odds_per_tier = { 1: 0, 2: 0, 3: 1 }

    shop_dice = []
    for _ in range(0, shop_size):
        selected_tier = 0
        roll = random.random()
        for tier in odds_per_tier.keys():
            roll = roll - odds_per_tier[tier]
            if roll < 0:
                selected_tier = tier
                break

        die_set = pool.dice_by_tier[selected_tier]
        max_die_index = len(die_set) - 1
        die_index = random.randint(0, max_die_index)
        die = die_set[die_index]
        die_set.remove(die)
        shop_dice.append(die)

    return Shop(shop_dice)
    
def close_shop(shop):
    for die in shop.dice:
        die_tier = die.die_type.tier
        self.pool.dice_by_tier[die_tier].append(die)
        
    shop.dice.clear()
    
def pop_die_at_index(shop, index):
    die = pool[index]
    pool.remove(die)
    return die
