def learn_perceptron(wgt, bias, egs, rate, max_epochs):
    for epoch in range(1, max_epochs + 1):
        seen_error = False

        for vec, trg in egs:
            out = 0 if vec[0] * wgt[0] + vec[1] * wgt[1] + bias < 0 else 1

            if out != trg:
                seen_error = True
                wgt = [i + vec[wgt.index(i)] * rate * (trg - out) for i in wgt]
                bias += rate * (trg - out)

        if not seen_error:
            def perceptron(vec):
                return 0 if vec[0] * wgt[0] + vec[1] * wgt[1] + bias < 0 else 1
            return perceptron


def main():
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 0),
      ((1, 0), 0),
      ((1, 1), 1),
      ]
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)

    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0, 0)))
        print(classifier((0, 1)))
        print(classifier((1, 0)))
        print(classifier((1, 1)))
        print(classifier((2, 2)))
        print(classifier((-3, -3)))
        print(classifier((3, -1)))

    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
      ]
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)

    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0, 0)))
        print(classifier((0, 1)))
        print(classifier((1, 0)))
        print(classifier((1, 1)))
        print(classifier((2, 2)))
        print(classifier((-3, -3)))
        print(classifier((3, -1)))

    # From the lecture notes
    weights = [1, 1]
    bias = -2
    learning_rate = 0.5
    examples = [
      ((0, 4), 0),
      ((-2, 1), 1),
      ((3, 5), 0),
      ((1, 1), 1),
      ]
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)

    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0, 4)))
        print(classifier((-2, 1)))
        print(classifier((3, 5)))
        print(classifier((1, 1)))
        print(classifier((4, 4)))
        print(classifier((-3, 6)))
        print(classifier((3, -1)))


if __name__ == "__main__":
    main()
