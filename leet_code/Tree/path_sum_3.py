from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution(object):
    def __init__(self):
        self.res = 0

    def pathSum(self, root, val):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def path_sum(r, cur_sum):
            global res
            if r is not None:
                cur_sum += r.val
                if dict_sum[cur_sum - val]:
                    self.res += dict_sum[cur_sum-val]
                dict_sum[cur_sum] += 1
                path_sum(r.left, cur_sum)
                path_sum(r.right, cur_sum)
                dict_sum[cur_sum] -= 1

        cur_sum = 0
        dict_sum = defaultdict(int)
        dict_sum[0] = 1
        path_sum(root, cur_sum)
        return self.res

r = deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
s = Solution()
print(s.pathSum(r, 22))
