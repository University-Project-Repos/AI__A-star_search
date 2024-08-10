def accuracy(p, c):
    return sum([1 for i, j in enumerate(p) if j == c[i]]) / len(p)


def main():
    print(accuracy((False, False, True, False), (True, True, False, False)))


if __name__ == "__main__":
    main()
