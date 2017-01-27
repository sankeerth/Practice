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


def tree_to_array(root, array):
    """in order traversal of the tree is stored in the array"""
    if root is not None:
        tree_to_array(root.left, array)
        array.append(root.data)
        tree_to_array(root.right, array)


def change_bst(root, a, b):
    """swap the values of nodes in BST"""
    if root is not None:
        change_bst(root.left, a, b)
        if root.data == a:
            root.data = b
        elif root.data == b:
            root.data = a
        change_bst(root.right, a, b)

prev = float('-inf')
first_element = None
second_element = None

def recover_bst(root):
    global prev, first_element, second_element
    if root is not None:
        recover_bst(root.left)
        if prev > root.data:
            if first_element is None:
                first_element = prev
            second_element = root.data
        prev = root.data
        recover_bst(root.right)


root = bst_insert(None, 10)
bst_insert(root, 5)
bst_insert(root, 15)
bst_insert(root, 4)
bst_insert(root, 7)
bst_insert(root, 14)
bst_insert(root, 17)

original_tree = []
edited_tree = []
recovered_tree = []


tree_to_array(root, original_tree)
change_bst(root, 14, 15)
tree_to_array(root, edited_tree)

print(original_tree)
print(edited_tree)

recover_bst(root)

print(first_element, second_element)

change_bst(root, first_element, second_element)
tree_to_array(root, recovered_tree)

print(recovered_tree)