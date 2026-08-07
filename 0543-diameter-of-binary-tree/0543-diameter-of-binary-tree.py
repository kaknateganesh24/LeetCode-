# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter=0
        self.height(root)
        return self.max_diameter
    def height(self,root):
        if root is None:
            return 0
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        self.max_diameter=max(self.max_diameter,left_height+right_height)
        return 1+max(left_height,right_height)
