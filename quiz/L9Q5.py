import itertools
import copy
from sources.csp import CSP, scope, satisfies


cryptic_puzzle = CSP(
    var_domains={
        't': set(range(10)),
        'w': set(range(10)),
        'o': set(range(10)),
        'f': set(range(10)),
        'u': set(range(10)),
        'r': set(range(10)),
        'x1': set(range(10)),
        'x2': set(range(10)),
        'x3': set(range(10)),
        },
    constraints={
        lambda o, r, x1: o + o == r + 10 * x1,
        lambda w, u, x1, x2: w + w + x1 == u + 10 * x2,
        lambda t, o, x2, x3: t + t + x2 == o + 10 * x3,
        lambda f, x3: f == x3,
        lambda t: 0 < t < 10,
        lambda f: 0 < f < 10,
        lambda w: 0 <= w < 10,
        lambda o: 0 <= o < 10,
        lambda u: 0 <= u < 10,
        lambda r: 0 <= r < 10,
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6
        })


def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())

    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}

        if all(satisfies(assignment, c) for c in csp.constraints):
            yield assignment


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


def main():
    print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
    print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['r']))
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['w']))
    new_csp = arc_consistent(cryptic_puzzle)
    solutions = []

    for solution in generate_and_test(new_csp):
        solutions.append(sorted((x, v) for x, v in solution.items() if x in "twofur"))
    print(len(solutions))
    solutions.sort()
    print(solutions[0])
    print(solutions[5])


if __name__ == "__main__":
    main()
