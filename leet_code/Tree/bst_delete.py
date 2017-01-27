class Tree(object):
    def __init__(self, d = None, l = None, r = None):
        self.data = d
        self.left = l
        self.right = r


def bst_insert(root, val):
    if root is None:
        root = Tree(v=val)
    else:
        if root.val > val:
            root.left = bst_insert(root.left, val)
        elif root.val < val:
            root.right = bst_insert(root.right, val)
        else:
            root.val = val
    return root


def bst_delete(root, data):
    if root is None:
        print("No such element found")
    elif data > root.data:
        root.right = bst_delete(root.right, data)
    elif data < root.data:
        root.left = bst_delete(root.left, data)
    else:
        if root.left is not None and root.right is not None:
            max_data = find_max(root.left)
            root.data = max_data
            root.left = bst_delete(root.left, max_data)
        else:
            temp = root
            root = root.left if root.left is not None else root.right
            del temp
    return root


def find_max(root):
    while root.right is not None:
        root = root.right
    return root.data


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

bst_delete(root, 8)

print_tree(root)