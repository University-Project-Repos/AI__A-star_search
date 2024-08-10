"""
COSC367 A* Routing Assignment
Author: Adam Ross
"""

from sources.search import Graph, Arc
from math import inf


class RoutingGraph(Graph):
    """
    Represents the input map in the form of a graph.
    """
    def __init__(self, input_map):
        if isinstance(input_map, str):
            self.map = [c for c in [r.strip() for r in input_map.strip().splitlines()]]
            self.GOAL = [(self.map.index(r), r.index(c)) for r in self.map for c in r if c == "G"][0]
        else:
            self.map = input_map
        self.COST = 2
        self.paths = {
            "N": (-1, 0),
            "NE": (-1, 1),
            "E": (0, 1),
            "SE": (1, 1),
            "S": (1, 0),
            "SW": (1, -1),
            "W": (0, -1),
            "NW": (-1, -1)
        }

    def is_goal(self, node):
        return node[:-1] == self.GOAL

    def starting_nodes(self):
        dct = dict({str(i): i for i in range(10)}.items() | {"S": inf}.items())
        return [(self.map.index(r), i, dct[char]) for r in self.map for i, char in enumerate(r) if char in dct]

    def outgoing_arcs(self, tail):
        for path in self.paths:
            x, y = tail[1] + self.paths[path][1], tail[0] + self.paths[path][0]

            if self.map[y][x] not in ["X", "+", "-", "|"] and tail[2] > 0:
                yield Arc(tail, (y, x, tail[2] - 1), path, self.COST)

        if self.map[tail[0]][tail[1]] == "F" and tail[2] < 9:
            yield Arc(tail, (tail[0], tail[1], 9), "Fuel up", 5)

    def estimated_cost_to_goal(self, tail):
        return max(abs(tail[0] - self.GOAL[0]), abs(tail[1] - self.GOAL[1])) * self.COST
