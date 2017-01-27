tree = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]


def print_all_ancestors(root, data):
    if tree[root] is None or root > len(tree):
        return 0
    else:
        left = 2 * root + 1
        right = 2 * root + 2
        if tree[root] == data or print_all_ancestors(left, data) or print_all_ancestors(right, data):
            print(tree[root])
            return 1


print_all_ancestors(0, 5)
