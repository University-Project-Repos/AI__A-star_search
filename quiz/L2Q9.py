from sources.search import ExplicitGraph
from math import sqrt


class LocationGraph(ExplicitGraph):
    """
    Implements a graph container appropriate for ordered depth-first search
    """

    def __init__(self, nodes, locations, edges, starting_list, goal_nodes):
        edges = [(e[0], e[1], sqrt((locations[e[0]][0] - locations[e[1]][0])**2
                                   + (locations[e[0]][1] -
                                      locations[e[1]][1])**2)) for e in edges]
        edges += [(e[1], e[0], e[2]) for e in edges]
        super().__init__(nodes, sorted(set(edges)), starting_list, goal_nodes)

    def estimated_cost_to_goal(self, node):
        raise NotImplementedError


def main():
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B', 'C'),
                                 ('C', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})

    for arc in graph.outgoing_arcs('A'):
        print(arc)

    for arc in graph.outgoing_arcs('B'):
        print(arc)

    for arc in graph.outgoing_arcs('C'):
        print(arc)
    print(" ")
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10, 6),
                   'c': (10, 18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_list=['a'],
        goal_nodes={'c'})

    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)


if __name__ == "__main__":
    main()
