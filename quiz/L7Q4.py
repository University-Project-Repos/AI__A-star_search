from operator import mul
from functools import reduce
from itertools import product


def joint_prob(network, assignment):
    return reduce(mul, [p[0] if p[1] else (1 - p[0]) for p in
                        [(network[i]['CPT'].get(tuple([assignment[b] for b in network[i]['Parents']])), assignment[i])
                         for i in assignment.keys()]], 1)


def query(network, query_var, evidence):
    probs = []

    for item in [None, True]:
        if item:
            evidence[query_var] = item
        prob, hidden_vars = 0, network.keys() - evidence.keys()

        for values in product((True, False), repeat=len(hidden_vars)):
            nets = dict({var: val for var, val in zip(hidden_vars, values)}.
                        items() | evidence.items())
            prob += joint_prob(network, nets)
        probs.append(prob)
    return {True: probs[1] / probs[0], False: 1 - probs[1] / probs[0]}


def main():
    network = {
        'Virus': {
            'Parents': [],
            'CPT': {
                (): 0.01
            }},

        'A': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.95,
                (False,): 0.1,
            }},

        'B': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},
    }
    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
