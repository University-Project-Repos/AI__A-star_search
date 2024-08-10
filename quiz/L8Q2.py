FILE_PATH = '../sources/spam-labelled.csv'

def learn_prior(file, pseudo_count=0):
    eg = [int(list(row)[-1]) for row in open(file).read().split('\n')[1:-1]]
    return (pseudo_count + sum([i for i in eg])) / (pseudo_count * 2 + len(eg))


def main():
    prior = learn_prior(FILE_PATH)
    print("Prior probability of spam is {:.5f}.".format(prior))

    prior = learn_prior(FILE_PATH)
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))

    prior = learn_prior(FILE_PATH, pseudo_count = 1)
    print(format(prior, ".5f"))

    prior = learn_prior(FILE_PATH, pseudo_count = 2)
    print(format(prior, ".5f"))

    prior = learn_prior(FILE_PATH, pseudo_count = 10)
    print(format(prior, ".5f"))

    prior = learn_prior(FILE_PATH, pseudo_count = 100)
    print(format(prior, ".5f"))

    prior = learn_prior(FILE_PATH, pseudo_count = 1000)
    print(format(prior, ".5f"))


if __name__ == "__main__":
    main()
