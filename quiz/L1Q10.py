from sources.search import Frontier, ExplicitGraph, generic_search, print_actions


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


class BFSFrontier(DFSFrontier):
    """
    Implements a frontier container appropriate for breadth-first search.
    """

    def __iter__(self):
        while self.container:
            yield self.container.pop(0)


def main():
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
                                   'Wellington', 'Gold Coast'],
                            edge_list=[('Christchurch', 'Gold Coast'),
                                       ('Christchurch', 'Auckland'),
                                       ('Christchurch', 'Wellington'),
                                       ('Wellington', 'Gold Coast'),
                                       ('Wellington', 'Auckland'),
                                       ('Auckland', 'Gold Coast')],
                            starting_list=['Christchurch'],
                            goal_nodes={'Gold Coast'})
    my_itinerary = next(generic_search(flights, DFSFrontier()), None)
    print_actions(my_itinerary)


if __name__ == "__main__":
    main()
