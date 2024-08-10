def neighbours(q):
    q = list(q)
    return [tuple(k) for k in [q[:i] + [q[j]] + q[i + 1:j] + [q[i]] + q[j + 1:]
            for i in range(len(q)) for j in range(len(q))] if len(k) == len(q)]


def main():
    print(list(neighbours((1, 2))))
    print(sorted(neighbours((1, 3, 2))))
    print(sorted(neighbours((1, 2, 3))))
    print(list(neighbours((1,))))

    for neighbour in sorted(neighbours((1, 2, 3, 4, 5, 6, 7, 8))):
        print(neighbour)

    for neighbour in sorted(neighbours((2, 3, 1, 4))):
        print(neighbour)


if __name__ == "__main__":
    main()
