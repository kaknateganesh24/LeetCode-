# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        result=self.isheight(root)
        return result!=-1
    def isheight(self,root):
        if root is None :
            return 0
        left_height=self.isheight(root.left)
        if left_height ==-1:
             return -1

        right_height=self.isheight(root.right)
        if right_height ==-1:
             return -1
        
        if abs(left_height-right_height)>1:
            return -1

        return 1 + max(left_height,right_height)