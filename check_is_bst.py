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

prev = float('-inf')
def check_is_bst_inorder(root):
    global prev
    if root is None:
        return True
    if not check_is_bst_inorder(root.left):
        return False
    if prev > root.data:
        return False
    prev = root.data
    return check_is_bst_inorder(root.right)


def check_is_bst(root, min_val, max_val):
    if root is None:
        return True
    return root.data > min_val and root.data < max_val and check_is_bst(root.left, min_val, root.data) and check_is_bst(root.right, root.data, max_val)


def change_bst(root):
    if root is not None:
        change_bst(root.left)
        if root.data == 5:
            root.data = 15
        change_bst(root.right)


def print_tree(root):
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
print(check_is_bst_inorder(root))
print(check_is_bst(root, float('-inf'), float('inf')))

change_bst(root)
print_tree(root)

print(check_is_bst(root, float('-inf'), float('inf')))
print(check_is_bst_inorder(root))