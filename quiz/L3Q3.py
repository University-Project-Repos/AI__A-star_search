import re
from sources.search import Frontier, Graph, generic_search, Arc


def clauses(knowledge_base):
    """
    Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = f"\\s*(?P<HEAD>{ATOM})\\s*"
    BODY   = f"\\s*(?P<BODY>{ATOM}\\s*(,\\s*{ATOM}\\s*)*)\\s*"
    CLAUSE = f"{HEAD}(:-{BODY})?\\."
    KB     = f"^({CLAUSE})*\\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):

    def __init__(self, kb, query):
        self.kb = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        yield self.query

    def outgoing_arcs(self, tail_node):
        new_tail = tail_node.copy()
        new_node = new_tail.pop()
        for node in [new_tail | set(edge[1]) for edge in self.kb if
                     new_node == edge[0]]:
            yield Arc(tail_node, node, label="top-down", cost=1)

    def estimated_cost_to_goal(self, node):
        pass

    def is_goal(self, node):
        return not node


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
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    query = {'a'}

    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    query = {'a', 'b', 'd'}

    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """
    query = {'program_is_correct'}

    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    kb = """
    a :- b.
    """
    query = {'c'}

    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")


if __name__ == "__main__":
    main()
