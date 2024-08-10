from math import inf


def max_value(tree):
    try:
        if int(tree):
            return tree
    except:
        value = -inf

        for b in range(len(tree)):
            value = max(value, min_value(tree[b]))
        return value


def min_value(tree):
    try:
        if int(tree):
            return tree
    except:
        value = inf

        for b in range(len(tree)):
            value = min(value, max_value(tree[b]))
        return value


if __name__ == '__main__':
    tree = 3
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [1, 2, 3]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [1, 2, [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [[1, 2], [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [[1, 2], [3, 4]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [[2, 3, 4], [1, 100, -100]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    # From the lecture notes
    tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))

    tree = [[1, 4], [3, 5], [2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
