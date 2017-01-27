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


def min_depth_of_tree(root):
    """find the min depth of the tree by calculating the
    min depth of left and right subtree recursively"""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    left_depth = float('inf') if root.left is None else min_depth_of_tree(root.left)
    right_depth = float('inf') if root.right is None else min_depth_of_tree(root.right)

    return min(left_depth, right_depth) + 1


depth = 0
min_depth = float('inf')


def min_depth_of_tree_check_leaf(root):
    """find the min depth of the tree by calcualting and updating
    the depth of the tree when a leaf node is reached"""
    global depth, min_depth
    if root is not None:
        depth += 1
        min_depth_of_tree_check_leaf(root.left)
        if root.left is None and root.right is None:
            if depth < min_depth:
                min_depth = depth
        min_depth_of_tree_check_leaf(root.right)
        depth -= 1
    return min_depth



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

print(min_depth_of_tree(root))

print(min_depth_of_tree_check_leaf(root))