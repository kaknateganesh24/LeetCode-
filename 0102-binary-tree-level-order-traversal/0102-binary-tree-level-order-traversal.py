# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None :
            return []
        result=[]
        queue=[root]
        
        while queue:
            level_size=len(queue)
            current_level=[]
            for i in range (level_size):
                node=queue.pop(0)
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(current_level)
        return result

