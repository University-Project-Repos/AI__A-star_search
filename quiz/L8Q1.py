from operator import mul
from functools import reduce


def posterior(prior, likelihood, observation):
    p = [(k, j) if observation[i] else (1 - k, 1 - j) for i, (j, k) in enumerate(likelihood)]
    true = reduce(mul, [i for (i, j) in p], 1) * prior
    false = reduce(mul, [j for (i, j) in p], 1) * (1 - prior)
    return true / (true + false)


def main():
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    observation = (True, True, True)
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    observation = (True, False, True)
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    observation = (False, False, True)
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    observation = (False, False, False)
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))


if __name__ == "__main__":
    main()
