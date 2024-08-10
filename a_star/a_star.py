"""
COSC367 A* Routing Assignment
Author: Adam Ross
"""

from a_star.graph import RoutingGraph
from heapq import heappush, heappop


class AStarFrontier(RoutingGraph):
    """
    Class for A* routing
    """
    def __init__(self, input_map):
        super().__init__(input_map)
        self.pruned = set()
        self.heap = []
        self.count = 1

    def add(self, path):
        if path[-1].head not in self.pruned:
            heappush(self.heap, (self.map.estimated_cost_to_goal(path[-1].head) +
                                 sum([edge.cost for edge in path]), self.count, path))
            self.count += 1

    def __iter__(self):
        while self.heap:
            _, _, path = heappop(self.heap)

            if path[-1].head not in self.pruned:
                self.pruned.add(path[-1].head)
                yield path
