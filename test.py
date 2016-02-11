import math
import numpy
import numpy as np
from collections import deque
import collections

class Planner(object):
	def __init__(self, world, simulator):
		self.world = world
		self.sim = simulator

	def run(self):
		cost = self.cost_matrix(self.world)
		for i in range()


	def closest_drone(self):
		result = []
		for warehouse in self.world.warehouses:
			distance = float('inf')
			for drone in self.world.drones:
				if distance(warehouse, drone) < distance:
					distance = distance(warehouse, drone) + self.dt
			result.append(distance)
		return result

	def rank_orders(self, remaining_time):
		lookUp = closest_drone()
		order_times = {}
		for order in self.world.orders:
			max_dist = 0
			for good in order.components:
				dist = float('inf')
				for w_i, warehouse in enumerate(self.world.warehouses):
					if warehouse.stock[good] > 0:
						total_dist = lookUp[w_i] + dist(w,o)
						if total_dist < dist:
							dist = total_dist
				if dist > remaining_time:
					self.world.orders.remove(order)
					break
				elif dist > max_dist:
					max_dist = dist
			order_times[order] = max_dist



	@staticmethod
	def cost_matrix(world):
		orders = self.world.orders
		drones = [d from d in self.world.drones if d.dt == 0]
		#  filter warehouses for products
		warehouses = [w for w in self.world.warehouses]
		cost_mat =[[]*len(drones)]*len(orders)
		


		for i, ordr in enumerate(orders):
			for j, drone in enumerate(drones):
				components = collections.Counter(ordr).getitems()
				route = list()
				ware = warehouses[0]
				tot = float('inf')
				while len(components)> 0:
					ow = dist(ordr, warehouse)
					dw = dist(drone, warehouse)
					if tot > ow + dw:
						ware = warehouse
					
				# for warehouse in warehouses[1:]:
				cost_mat[i][j] = ware
		return cost_mat

	def cost(self, order, drone):

		return 



def dist(w,d):
	return math.sqrt((w.x-d.x)*(w.x-d.x)+(w.y-d.y)*(w.y-d.y))