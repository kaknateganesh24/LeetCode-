# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        return self.helper(root, False)
    def helper(self, node, is_left):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            if is_left:
                return node.val    # ye leaf hai aur left child tha - value return karo
            else:
                return 0
        left_sum = self.helper(node.left, True)
        right_sum = self.helper(node.right, False)
        return left_sum + right_sum
            