from itertools import combinations


def conflict_count(q):
    return len([1 for i in range(len(q)) for j in range(len(q)) if (q[i], q[j])
                in combinations(q, 2) and abs(j - i) == abs(q[i] - q[j])])


def main():
    print(conflict_count((1, 2)))
    print(conflict_count((1, 3, 2)))
    print(conflict_count((1, 2, 3)))
    print(conflict_count((1,)))
    print(conflict_count((1, 2, 3, 4, 5, 6, 7, 8)))
    print(conflict_count((2, 3, 1, 4)))


if __name__ == "__main__":
    main()
