from operator import mul
from functools import reduce

FILE_PATH = '../sources/spam-labelled.csv'


def posterior(prior, likelihood, observation):
    p = [(k, j) if observation[i] else (1 - k, 1 - j) for i, (j, k) in enumerate(likelihood)]
    true = reduce(mul, [i for (i, j) in p], 1) * prior
    false = reduce(mul, [j for (i, j) in p], 1) * (1 - prior)
    return true / (true + false)


def learn_prior(file, pseudo_count=0):
    eg = [int(list(row)[-1]) for row in open(file).read().split('\n')[1:-1]]
    return (pseudo_count + sum([i for i in eg])) / (pseudo_count * 2 + len(eg))


def learn_likelihood(file, pseudo_count=0):
    eg = [list(map(int, k.split(','))) for k in open(file).readlines()[1:]]
    res, p = {i: [[0], [0]] for i in range(12)}, sum([int(l[-1]) for l in eg])
    [[res[i][row[-1]].append(j) for i, j in enumerate(row[:-1])] for row in eg]
    return [((pseudo_count + sum(j[0])) / (pseudo_count * 2 + (200 - p)),
             (pseudo_count + sum(j[1])) / (pseudo_count * 2 + p))
            for i, j in res.items()]


def nb_classify(prior, likelihood, input_vector):
    p = posterior(prior, likelihood, input_vector)
    return ("Not Spam", 1 - p) if p < 0.5 else ("Spam", p)


def main():
    prior = learn_prior(FILE_PATH)
    likelihood = learn_likelihood(FILE_PATH)
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))

    prior = learn_prior(FILE_PATH, pseudo_count=1)
    likelihood = learn_likelihood(FILE_PATH, pseudo_count=1)
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))


if __name__ == "__main__":
    main()
