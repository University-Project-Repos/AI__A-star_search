import re


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


def forward_deduce(kb):
    model = []
    [model.append(head) for head, body in
     [clause for clause in [(head, body) for head, body in list(clauses(kb)) * ((len(list(clauses(kb)))**2) - 1)]]
     if not (head in model or False in [atom in model for atom in body])]
    return set(model)


def main():
    kb = """
    a :- b.
    b.
    """
    print(", ".join(sorted(forward_deduce(kb))))

    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """
    print(", ".join(sorted(forward_deduce(kb))))

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
    print(", ".join(sorted(forward_deduce(kb))))


if __name__ == "__main__":
    main()
