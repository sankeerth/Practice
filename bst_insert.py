class Tree(object):
    """structure of the tree"""
    def __init__(self, d = None, l = None, r = None):
        self.data = d
        self.left = l
        self.right = r


def bst_insert(root, data):
    """traverse the tree and insert the data when the condition is met"""
    if root is None:
        root = Tree(d=data)
    elif data > root.data:
        root.right = bst_insert(root.right, data)
    else:
        root.left = bst_insert(root.left, data)
    return root


def print_tree(root):
    """print the tree in ascending order (in order traversal)"""
    if root is not None:
        print_tree(root.left)
        print(root.data)
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