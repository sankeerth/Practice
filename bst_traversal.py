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


def print_tree_ascending(root):
    """in order traversal of binary tree prints in ascending order"""
    if root is not None:
        print_tree_ascending(root.left)
        print(root.data)
        print_tree_ascending(root.right)


def print_tree_descending(root):
    """reverse in order traversal of binary tree prints in descending order"""
    if root is not None:
        print_tree_descending(root.right)
        print(root.data)
        print_tree_descending(root.left)


root = bst_insert(None, 15)
bst_insert(root, 10)
bst_insert(root, 20)
bst_insert(root, 8)
bst_insert(root, 12)
bst_insert(root, 16)
bst_insert(root, 25)

print("ascending")
print_tree_ascending(root)
print("descending")
print_tree_descending(root)