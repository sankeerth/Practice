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


def construct_binary_tree_inorder_preorder(in_array, pre_array, low, high):
    global pre_index
    if low <= high:
        root = TreeNode(pre_array[pre_index])
        in_index = in_array.index(pre_array[pre_index])
        pre_index += 1
        if low == high:
            return root
        root.left = construct_binary_tree_inorder_preorder(in_array, pre_array, low, in_index-1)
        root.right = construct_binary_tree_inorder_preorder(in_array, pre_array, in_index+1, high)
        return root


pre_index = 0
in_array = [3,6,7,8,9,10,11]
pre_array = [6,3,11,8,7,10,9]
in_array = [4,2,8,5,1,3,7,6]
pre_array = [1,2,4,5,8,3,6,7]

r = construct_binary_tree_inorder_preorder(in_array, pre_array, 0, len(in_array)-1)
in_order(r)
