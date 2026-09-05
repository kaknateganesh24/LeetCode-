# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result=[]
        queue=deque([root])
        level_number=0
        while queue:
            level_size=len(queue)
            level_list=[]
            for i in range(level_size):
                node=queue.popleft()
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_number%2==1:
                level_list.reverse()
            result.append(level_list)
            level_number+=1
        return result
