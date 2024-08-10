from operator import mul
from functools import reduce


def joint_prob(network, assignment):
    return reduce(mul, [p[0] if p[1] else (1 - p[0]) for p in
                        [(network[i]['CPT'].get(tuple([assignment[b] for b in network[i]['Parents']])), assignment[i])
                         for i in assignment.keys()]], 1)


def main():
    network = {
        'A': {
            'Parents': [ ],
            'CPT': {
                (): 0.2
            }},
    }
    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))

    network = {
        'A': {
            'Parents': [ ],
            'CPT': {
                (): 0.2
            }},
    }
    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))

    network = {
        'A': {
            'Parents': [ ],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': [ 'A' ],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }
    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p))

    network = {
        'A': {
            'Parents': [ ],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': [ 'A' ],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }
    p = joint_prob(network, {'A': False, 'B': False})
    print("{:.5f}".format(p))

    network = {
        'Burglary': {
            'Parents': [ ],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [ ],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': [ 'Burglary', 'Earthquake' ],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': [ 'Alarm' ],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': [ 'Alarm' ],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }
    p = joint_prob(network, {
        'John': True, 'Mary': True,
        'Alarm': True, 'Burglary': True,
        'Earthquake': False
    })
    print("{:.8f}".format(p))


if __name__ == "__main__":
    main()
