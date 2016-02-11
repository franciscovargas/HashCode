
class Simulator:

    # for all orders you find the closest warehouse+drone(back, forth)
    def __init__: (self, world, scheduler):
        self.world = world
        self.scheduler = scheduler
        # self.turns_left = 

    def sim_loop(self):
        turns_left = self.max_turns
        while (turns_left > 0 and not self.scheduler.stop):
            update_rules = self.scheduler.run()
            # update dictionary of shit.
            self.world.update(update_rules)
            turns_left -= 1


    
