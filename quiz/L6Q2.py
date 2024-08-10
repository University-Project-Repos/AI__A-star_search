from math import inf


def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    try:
        if int(tree):
            return tree
    except:
        value = -inf

        for b in range(len(tree)):
            value = max(value, min_value(tree[b], alpha, beta))

            if value >= beta:
                if tree[b + 1:]:
                    print("Pruning:", ", ".join(map(str, tree[b + 1:])))
                return value
            alpha = max(alpha, value)
        return value


def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    try:
        if int(tree):
            return tree
    except:
        value = inf

        for b in range(len(tree)):
            value = min(value, max_value(tree[b], alpha, beta))

            if value <= alpha:
                if tree[b + 1:]:
                    print("Pruning:", ", ".join(map(str, tree[b + 1:])))
                return value
            beta = min(beta, value)
        return value


def main():
    # no pruning when the root is max
    # but one child pruned when the root is min
    tree = [[1, 2], [3, 4]]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))

    # changing the order of children affects
    # what is being pruned.
    tree = [[3, 4], [1, 2]]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))

    tree = [[2, 3, 4], [1, 100, -100]]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))

    # From the lecture notes
    tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))

    tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))

    tree = [3, [[1, 2], [[4, 5], [6, 7]]], 8]
    print("Game tree:", tree)
    print("Computing the utility of the root as a max node...")
    print("Root utility for maximiser:", max_value(tree))
    print("Computing the utility of the root as a min node....")
    print("Root utility for minimiser:", min_value(tree))


if __name__ == '__main__':
    main()
