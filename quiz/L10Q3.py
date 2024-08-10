from itertools import combinations


def conflict_count(q):
    return len([1 for i in range(len(q)) for j in range(len(q)) if (q[i], q[j])
                in combinations(q, 2) and abs(j - i) == abs(q[i] - q[j])])


def neighbours(q):
    q = list(q)
    return [tuple(k) for k in [q[:i] + [q[j]] + q[i + 1:j] + [q[i]] + q[j + 1:]
            for i in range(len(q)) for j in range(len(q))] if len(k) == len(q)]


def greedy_descent(q):
    num = conflict_count(q)
    print("Assignment:", q, "Number of conflicts:", num)

    if num == 0:
        print("A solution is found.")
    else:
        nxt = sorted([(conflict_count(i), i) for i in neighbours(q)])[0]

        if nxt[0] < num:
            greedy_descent(nxt[1])
        elif nxt[0] == num:
            print("A local minimum is reached.")


def main():
    greedy_descent((1, 2, 3, 4, 5, 6))
    greedy_descent((6, 5, 3, 4, 2, 1))
    greedy_descent((2, 1, 3, 4, 6, 5))
    greedy_descent((1,))
    greedy_descent((1, 2))
    greedy_descent(tuple(range(1, 4)))
    greedy_descent(tuple(range(1, 6)))
    greedy_descent(tuple(range(1, 11)))


if __name__ == "__main__":
    main()
