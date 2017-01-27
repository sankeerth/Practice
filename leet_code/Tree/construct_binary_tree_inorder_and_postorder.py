class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def construct_binary_tree_inorder_postorder(in_array, post_array, low, high):
    global post_index
    if low <= high:
        root = TreeNode(post_array[post_index])
        in_index = in_array.index(post_array[post_index])
        post_index -= 1
        if low == high:
            return root
        root.right = construct_binary_tree_inorder_postorder(in_array, post_array, in_index+1, high)
        root.left = construct_binary_tree_inorder_postorder(in_array, post_array, low, in_index-1)
        return root


in_array = [4, 2, 8, 5, 1, 3, 7, 6]
post_array = [4, 8, 5, 2, 7, 6, 3, 1]
post_index = len(post_array) - 1
r = construct_binary_tree_inorder_postorder(in_array, post_array, 0, len(in_array)-1)
in_order(r)
