from abc import ABCMeta, abstractmethod

class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def serialise(self):
        return ""

class LoadCommand(Command):
    def __init__(self, drone, warehouse, product, count):
        self.drone = drone
        self.warehouse = warehouse
        self.product = product
        self.count = count

    def serialise(self):
        return "{} L {} {} {}".format(self.drone, self.warehouse, self.product, self.count)

class UnloadCommand(Command):
    def __init__(self, drone, warehouse, product, count):
        self.drone = drone
        self.warehouse = warehouse
        self.product = product
        self.count = count

    def serialise(self):
        return "{} U {} {} {}".format(self.drone, self.warehouse, self.product, self.count)       

class DeliverCommand(Command):
    def __init__(self, drone, customer, product, count):
        self.drone = drone
        self.customer = customer
        self.product = product
        self.count = count

    def serialise(self):
        return "{} D {} {} {}".format(self.drone, self.customer, self.product, self.count)

class WaitCommand(Command):
    def __init__(self, drone, turns):
        self.drone = drone
        self.turns = turns

    def serialise(self):
        return "{} W {}".format(self.drone, self.turns)

def serialise(fname, commands):
    with open(fname, 'w') as f:
        f.write("{}\n".format(len(commands)))
        for command in commands:
            f.write("{}\n".format(command.serialise()))
