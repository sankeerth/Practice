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


def change_bst(root, a, b):
    """swap the values of nodes in BST"""
    if root is not None:
        change_bst(root.left, a, b)
        if root.data == a:
            root.data = b
        elif root.data == b:
            root.data = a
        change_bst(root.right, a, b)


def tree_to_array(root, array):
    """in order traversal of the tree is stored in the array"""
    if root is not None:
        tree_to_array(root.left, array)
        array.append(root.data)
        tree_to_array(root.right, array)

index = 0
def binary_tree_to_bst(root, array):
    """perform an inorder traversal of the binary tree and store the values.
    sort the values stored. perform an inorder traversal of binary tree again
    and replace the values with the values in the sorted array recursively"""
    global index
    if root is not None:
        binary_tree_to_bst(root.left, array)
        root.data = array[index]
        index += 1
        binary_tree_to_bst(root.right, array)


def print_tree(root):
    """print the tree in ascending order (in order traversal)"""
    if root is not None:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)


root = bst_insert(None, 4)
bst_insert(root, 2)
bst_insert(root, 6)
bst_insert(root, 1)
bst_insert(root, 3)
bst_insert(root, 5)
bst_insert(root, 7)

change_bst(root, 1, 4)
change_bst(root, 3, 5)
change_bst(root, 3, 6)

edited_tree = []

tree_to_array(root, edited_tree)

print(edited_tree)

edited_tree.sort()

print_tree(root)

print(edited_tree)

binary_tree_to_bst(root, edited_tree)

print_tree(root)

