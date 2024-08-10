FILE_PATH = '../sources/spam-labelled.csv'


def learn_likelihood(file, pseudo_count=0):
    eg = [list(map(int, k.split(','))) for k in open(file).readlines()[1:]]
    res, p = {i: [[0], [0]] for i in range(12)}, sum([int(l[-1]) for l in eg])
    [[res[i][row[-1]].append(j) for i, j in enumerate(row[:-1])] for row in eg]
    return [((pseudo_count + sum(j[0])) / (pseudo_count * 2 + (200 - p)),
             (pseudo_count + sum(j[1])) / (pseudo_count * 2 + p))
            for i, j in res.items()]


def main():
    likelihood = learn_likelihood(FILE_PATH)
    print(len(likelihood))
    print([len(item) for item in likelihood])

    likelihood = learn_likelihood(FILE_PATH)
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

    likelihood = learn_likelihood(FILE_PATH, pseudo_count=1)
    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

    likelihood = learn_likelihood(FILE_PATH, pseudo_count=1)
    print("\n".join([format(p1, ".5f") + "  " + format(p2, ".5f")
                     for p1, p2 in likelihood]))


if __name__ == "__main__":
    main()
