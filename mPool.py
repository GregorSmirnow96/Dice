from mDie import Die
import json


class Pool:

    def __init__(self,
        types,
        tier_counts,
        augments):
        self.types = types
        self.tier_counts = tier_counts
        self.augments = augments

        self.dice_by_tier = {}
        self.relics_by_tier = {}

        self._populate_die_pool()
        self._populate_relic_pool()
    
    def _populate_die_pool(self):
        # Add all dice to the pool, one type at a time.
        for die_type in self.types:
            # Initialize tier specific pool if it doesn't exist.
            current_tier = die_type.tier
            if current_tier not in self.dice_by_tier.keys():
                self.dice_by_tier[current_tier] = []

            # Get the number of dice to create for this type.
            die_count = self.tier_counts[current_tier]
            # Create the specified number of dice, adding them to their tier's pool.
            pool_for_current_tier = self.dice_by_tier[current_tier]
            for _ in range(0, die_count):
                new_die = Die(0, die_type) # TODO: Don't hardcode die ID to 0!
                pool_for_current_tier.append(new_die)
    
    def _populate_relic_pool(self):
        print("Implement Pool.populate_relic_pool()")
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
