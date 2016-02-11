class World:
    def __init__(self, rows, columns, drones, maxturns, maxload, products):
        self.rows = rows
        self.columns = columns
        self.drones = drones
        self.max_turns = maxturns
        self.max_load = maxload
        self.products = products

        self.warehouses = []
        self.orders = []

    def add_warehouse(self, x, y, stock):
        self.warehouses.append(Warehouse(x,y,stock, self))

    def add_order(self, x, y, size, components):
        self.orders.append(Order(x,y,size,components, self))

    @staticmethod
    def load(fname):
        with open(fname, 'r') as f:
            data = f.read()

        lines = data.split('\n')

        world_params = lines[0]
        product_count = int(lines[1].strip())
        product_weights = [int(x.strip()) for x in lines[2].split(' ')]

        rows, columns, drones, maxturns, maxload = [int(x.strip()) for x in world_params.split(' ', 5)]
        
        world = World(rows, columns, drones, maxturns, maxload, product_weights[:product_count])

        warehouses = int(lines[3].strip())

        w_lines = warehouses*2

        for w in range(warehouses):
            x, y = [int(x.strip()) for x in lines[4 + w*2 + 0].split(' ', 2)]
            stock = [int(x.strip()) for x in lines[4 + w*2 + 1].split(' ', product_count)]
            world.add_warehouse(x, y, stock)

        offset = 4+w_lines
        orders = int(lines[offset].strip())

        o_lines = orders*3

        offset = offset+1

        for o in range(orders):
            x, y = [int(x.strip()) for x in lines[offset + o*3 + 0].split(' ', 2)]
            size = int(lines[offset + o*3 + 1])
            components = [int(x.strip()) for x in lines[offset + o*3 + 2].split(' ', size)]
            world.add_order(x,y,size, components)

        return world

class Warehouse:
    def __init__(self, x, y, stock, world):
        self.x = x
        self.y = y
        self.stock = stock
        self._world = world

class Order:
    def __init__(self, x, y, size, components, world):
        self.x = x
        self.y = y
        self.size = size
        self.components = components
        self._world = world

    def compute_total_weight(self):
        return sum([self._world.products[i] for i in self.components])

