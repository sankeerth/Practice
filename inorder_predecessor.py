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

prev = None
def inorder_predecessor(root, data):
    global prev
    if root is not None:
        inorder_predecessor(root.left, data)
        if root.data == data:
            print(prev)
        prev = root.data
        inorder_predecessor(root.right, data)


root = bst_insert(None, 15)
bst_insert(root, 10)
bst_insert(root, 20)
bst_insert(root, 8)
bst_insert(root, 12)
bst_insert(root, 16)
bst_insert(root, 25)

inorder_predecessor(root, 12)