class Tree(object):
    def __init__(self, d = None, l = None, r = None):
        self.data = d
        self.left = l
        self.right = r


def bst_insert(root, data):
    if root is None:
        root = Tree(d=data)
    elif data > root.data:
        root.right = bst_insert(root.right, data)
    else:
        root.left = bst_insert(root.left, data)
    return root


def bst_LCA(root, A, B):
    if root is None:
        return None
    if root.data == A or root.data == B:
        return root
    left = bst_LCA(root.left, A, B)
    right = bst_LCA(root.right, A, B)

    if left is not None and right is not None:
        return root

    return left if left is not None else right


def print_tree(root):
    if root is not None:
        print(root.data)
        print_tree(root.left)
        print_tree(root.right)


root = bst_insert(None, 4)
bst_insert(root, 2)
bst_insert(root, 8)
bst_insert(root, 5)
bst_insert(root, 11)
bst_insert(root, 7)
bst_insert(root, 6)
bst_insert(root, 3)

print_tree(root)

lca = bst_LCA(root, 6, 3)
print(lca.data)