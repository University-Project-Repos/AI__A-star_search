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
        'Disease': {
            'Parents': [],
            'CPT': {
                (): 0.00001
            }},

        'Test': {
            'Parents': ['Disease'],
            'CPT': {
                (True,): 0.99,
                (False,): 0.01,
            }},
    }
    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))
    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
