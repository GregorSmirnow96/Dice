import cGameContext as GameContextController
import cShop as ShopController
from mDraftPool import DraftPool
from mGameContext import GameContext
import random
import time


class Game:

    def __init__(self, players):
        self.players = players
        self.game_context = GameContextController.create_game()

        for player in players:
            self.game_context.add_player(player)

    def start(self):
        stage_cycle = [
            self.draft,
            self.build,
            self.fight,
            self.build,
            self.fight,
            self.build,
            self.fight
        ]
        next_stage_index = 0
        while self.get_living_player_count() > 1:
            next_stage = stage_cycle[next_stage_index]
            next_stage()
            next_stage_index = (next_stage_index + 1) % len(stage_cycle)
    
    def draft(self):
        duration_per_player = 5

        # Implement Draft phase:
        stage_alert = 'Draft your dice.'
        self.push_down_message(stage_alert)

        die_set = ShopController.create_shop(
            self.game_context.pool,
            1,
            shop_size=8) # TODO: Don't harcode tier.
        draft = DraftPool(die_set)
        for player in self.players:
            player.session.send_message('DRAFT:TAKE_TURN')
            selected_index = player.session.get_message(
                prefix='DRAFT:TAKE_TURN',
                max_wait=duration_per_player)
            if selected_index:
                selected_index = int(selected_index.lstrip('DRAFT:TAKE_TURN'))
            else:
                draft_indices = [index for index in draft.dice_by_index.keys()]
                selected_index = random.randint(0, len(draft_indices) - 1)
            selected_die = draft.dice_by_index[selected_index]
            draft.dice_by_index[selected_index] = None
            player.board.add_die_to_bench(selected_die)
        
        for player_index in range(len(self.players) - 1, -1, -1):
            player = self.players[player_index]
            player.session.send_message('DRAFT:TAKE_TURN')
            selected_index = player.session.get_message(
                prefix='DRAFT:TAKE_TURN',
                max_wait=duration_per_player)
            if selected_index:
                selected_index = int(selected_index.lstrip('DRAFT:TAKE_TURN'))
            else:
                draft_indices = [index for index in draft.dice_by_index.keys()]
                selected_index = random.randint(0, len(draft_indices) - 1)
            selected_die = draft.dice_by_index[selected_index]
            draft.dice_by_index[selected_index] = None
            player.board.add_die_to_bench(selected_die)
    
    def build(self):
        duration = 2
        stage_alert = 'Build you team.'

        # Implement Build phase:
        self.push_down_message(stage_alert)

        time.sleep(duration)
    
    def fight(self):
        duration = 2
        stage_alert = 'Fighting!'

        # Implement Fight phase:
        self.push_down_message(stage_alert)

        time.sleep(duration)

    def get_living_player_count(self):
        living_player_count = 0

        for player in self.players:
            if player.alive:
                living_player_count = living_player_count + 1

        return living_player_count

    def push_down_game_state(self):
        self.push_down_message("Game state (represented as json)")

    def push_down_message(self, message):
        for player in self.players:
            player.session.send_message(message)
