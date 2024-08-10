from sources.search import Frontier, ExplicitGraph, generic_search, print_actions


class OrderedExplicitGraph(ExplicitGraph):
    """
    Implements a graph container appropriate for ordered depth-first search
    """

    def __init__(self, nodes, edges, starting_list, goal_nodes):
        super().__init__(nodes, sorted(edges, reverse=True), starting_list, goal_nodes)

    def estimated_cost_to_goal(self, node):
        raise NotImplementedError


class DFSFrontier(Frontier):
    """
    Implements a frontier container appropriate for depth-first search.
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
            yield self.container.pop()


def main():
    print(sorted({('S', 'A'), ('S', 'G'), ('A', 'G')}, reverse=True))
    graph = OrderedExplicitGraph(nodes=set('SAG'),
                                 edges={('S', 'A'), ('S', 'G'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})

    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    graph = OrderedExplicitGraph(nodes=set('SABG'),
                                 edges={('S', 'A'), ('S', 'B'),
                                        ('B', 'S'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    flights = OrderedExplicitGraph(nodes={'Christchurch', 'Auckland',
                                          'Wellington', 'Gold Coast'},
                                   edges={('Christchurch', 'Gold Coast'),
                                          ('Christchurch', 'Auckland'),
                                          ('Christchurch', 'Wellington'),
                                          ('Wellington', 'Gold Coast'),
                                          ('Wellington', 'Auckland'),
                                          ('Auckland', 'Gold Coast')},
                                   starting_list=['Christchurch'],
                                   goal_nodes={'Gold Coast'})
    my_itinerary = next(generic_search(flights, DFSFrontier()), None)
    print_actions(my_itinerary)


if __name__ == "__main__":
    main()
