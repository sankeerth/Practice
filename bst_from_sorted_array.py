class Tree(object):
    """structure of the tree"""
    def __init__(self, d = None, l = None, r = None):
        self.data = d
        self.left = l
        self.right = r


def print_tree(root):
    """print the tree in ascending order (in order traversal)"""
    if root is not None:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)


def bst_from_sorted_array(array, low, high):
    """create a BST from sorted array with the mid of the array as root node and recursively
        call the function with values to the left of mid as left subtree and values to the
        right of mid as right subtree"""
    root = None
    if low <= high:
        mid = int(low + (high - low)/2)
        root = Tree(d=array[mid])
        root.left = bst_from_sorted_array(array, low, mid - 1)
        root.right = bst_from_sorted_array(array, mid + 1, high)
    return root

sorted_array = [i+1 for i in range(7)]
r = bst_from_sorted_array(sorted_array, 0, len(sorted_array)-1)

print_tree(r)