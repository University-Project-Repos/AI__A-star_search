from sources.search import generic_search, print_actions
from a_star.a_star import AStarFrontier
from a_star.graph import RoutingGraph


def print_map(test_map, frontier, solution):
    """
    Prints a map with solution (*) and frontier (.) paths
    """
    graph = [list(row) for row in test_map.map]

    if solution:
        for i in solution[1:-1]:
            graph[i.head[0]][i.head[1]] = "*"

    for y, x, _ in frontier.pruned:
        if graph[y][x] == " ":
            graph[y][x] = "."

    for row in graph:
        print(''.join(row))


def test():
    map_str = """\
            +-------+
            |  9  XG|
            |X XXX  |
            | S  0F |
            +-------+
            """
    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print("  " + str(arc))

    node = (1, 1, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (1, 7, 2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 6, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 6, 9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))
    print("")
    map_str = """\
            +--+
            |GS|
            +--+
            """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print("  " + str(arc))

    node = (1, 1, 1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))
    print("")
    map_str = """\
            +------+
            |S    S|
            |  GXXX|
            |S     |
            +------+
            """

    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))

    map_str = """\
            +-------+
            |   G   |
            |       |
            |   S   |
            +-------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +-------+
            |     XG|
            |X XXX  |
            | S     |
            +-------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +-------+
            |  F  XG|
            |X XXXX |
            | 2     |
            +-------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +--+
            |GS|
            +--+
            """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +---+
            |GF2|
            +---+
            """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +----+
            | S  |
            | SX |
            | X G|
            +----+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +---------+
            |         |
            |    G    |
            |         |
            +---------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +----------+
            |    X     |
            | S  X  G  |
            |    X     |
            +----------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    print("")

    map_str = """\
            +----------------+
            |2             F |
            |XX   G 123      |
            |2XXXXXXXXXXXXXX |
            |  F             |
            |           F    |
            +----------------+
            """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
                +-------+
                |     XG|
                |X XXX  |
                | S     |
                +-------+
                """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                +--+
                |GS|
                +--+
                """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                +----+
                |    |
                | SX |
                | X G|
                +----+
                """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                    +------------+
                    |            |
                    |            |
                    |            |
                    |    S       |
                    |            |
                    |            |
                    | G          |
                    |            |
                    +------------+
                    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                    +------------+
                    |            |
                    |            |
                    |            |
                    |    S       |
                    |            |
                    |            |
                    | G          |
                    |            |
                    +------------+
                    """

    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                    +---------------+
                    |    G          |
                    |XXXXXXXXXXXX   |
                    |           X   |
                    |  XXXXXX   X   |
                    |  X S  X   X   |
                    |  X        X   |
                    |  XXXXXXXXXX   |
                    |               |
                    +---------------+
                    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                    +---------+
                    |         |
                    |    G    |
                    |         |
                    +---------+
                    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    print("")

    map_str = """\
                    +-------------+
                    |         G   |
                    | S           |
                    |         S   |
                    +-------------+
                    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def main():
    test()


if __name__ == '__main__':
    main()
