
class Board:

    def __init__(self):
        self.relic_1 = None
        self.relic_2 = None
        self.relic_3 = None
        self.relic_4 = None
        self.relic_5 = None

        self.bench_slot_1 = None
        self.bench_slot_2 = None
        self.bench_slot_3 = None
        self.bench_slot_4 = None
        self.bench_slot_5 = None
        self.bench_slot_6 = None
        self.bench_overflow_slot = None

        self.active_unit_positions = {}
    
    def add_die_to_bench(self, die):
        if not self.bench_slot_1:
            self.bench_slot_1 = die
        elif not self.bench_slot_2:
            self.bench_slot_2 = die
        elif not self.bench_slot_3:
            self.bench_slot_3 = die
        elif not self.bench_slot_4:
            self.bench_slot_4 = die
        elif not self.bench_slot_5:
            self.bench_slot_5 = die
        elif not self.bench_slot_6:
            self.bench_slot_6 = die
        else:
            self.bench_overflow_slot = die
