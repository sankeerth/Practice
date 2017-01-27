tree = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]


def LCA(root, A, B):
    if tree[root] is None or root >= len(tree):
        return None
    if tree[root] == A or tree[root] == B:
        return root
    left = LCA(2*root+1, A, B)
    right = LCA(2*root+2, A, B)

    if left is not None and right is not None:
        return root

    return left if left is not None else right


node = LCA(0, 7, 6)
print(None if node is None else tree[node])
