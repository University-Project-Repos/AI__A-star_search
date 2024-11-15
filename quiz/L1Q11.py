from itertools import dropwhile
from sources.search import Frontier, Graph, Arc, generic_search, print_actions


class FunkyNumericGraph(Graph):
    """
    A graph where nodes are numbers. A node (number) n leads to n - 1 and n + 2.
    Nodes that are divisible by 10 are goal nodes.
    """

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        yield Arc(tail_node, tail_node - 1, label="1down", cost=1)
        yield Arc(tail_node, tail_node + 2, label="2up", cost=1)

    def starting_nodes(self):
        yield self.starting_number

    def is_goal(self, node):
        return node % 10 == 0

    def estimated_cost_to_goal(self, node):
        raise NotImplementedError


class BFSFrontier(Frontier):
    """
    Implements a frontier container appropriate for breadth-first search.
    """

    def __init__(self):
        """
        The constructor takes no argument. It initialises the container to an empty list.
        """
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        while self.container:
            yield self.container.pop(0)


def main():
    graph = FunkyNumericGraph(4)

    for node in graph.starting_nodes():
        print(node)
    graph = FunkyNumericGraph(4)

    for arc in graph.outgoing_arcs(7):
        print(arc)
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))


if __name__ == "__main__":
    main()
