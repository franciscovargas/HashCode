
class Simulator:

    # for all orders you find the closest warehouse+drone(back, forth)
    def __init__: (self, world, scheduler):
        self.world = world
        self.scheduler = scheduler

    def sim_loop(self):
        turns_left = self.max_turns
        while (turns_left > 0 and not self.scheduler.stop):
            update_rules = self.scheduler.decide(turns_left)
            # update dictionary of shit.
            self.world.update(update_rules)
            turns_left -= 1


    
