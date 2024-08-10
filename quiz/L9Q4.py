import itertools, copy
from sources.csp import scope, satisfies, CSP


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in scope(c)}

    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()

        for x_val in csp.var_domains[x]:
            assignment = {x: x_val}

            for y_vals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: y_val for y, y_val in zip(ys, y_vals)})

                if satisfies(assignment, c):
                    new_domain.add(x_val)
                    break

        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain

            for c_prime in set(csp.constraints) - {c}:
                if x in scope(c_prime):
                    for z in scope(c_prime):
                        if x != z:
                            tda.add((z, c_prime))
    return csp


simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })


def main():
    csp = arc_consistent(simple_csp)

    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))
    csp = CSP(var_domains={x: set(range(10)) for x in 'abc'},
              constraints={lambda a, b, c: 2 * a + b + 2 * c == 10})
    csp = arc_consistent(csp)

    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))


if __name__ == "__main__":
    main()
