tree = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]
stack = []


def root_to_leaf_paths(root):
    if tree[root] is not None and root < len(tree):
        stack.append(tree[root])
        left = 2 * root + 1
        right = 2 * root + 2
        if tree[left] is None and tree[right] is None:
            print(stack)
            stack.pop()
        else:
            root_to_leaf_paths(left)
            root_to_leaf_paths(right)
            stack.pop()

root_to_leaf_paths(0)