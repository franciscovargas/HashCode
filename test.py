import math
import numpy
import numpy as np
from collections import deque

class Planner(object):
	def __init__(self, world, simulator):
		self.world = world
		self.sim = simulator

	def run(self):
		costs = 


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

	def cost(self, order, drone):

		return 



def dist(w,d):
	return math.sqrt((w.x-d.x)*(w.x-d.x)+(w.y-d.y)*(w.y-d.y))