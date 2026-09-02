class Solution(object):
    def isValidBST(self, root):
        def helper(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return  False        # ye kya hoga?
            left_ok = helper(node.left, low,node.val)      # high yahan kya?
            right_ok = helper(node.right, node.val, high)    # low yahan kya?
            return left_ok and right_ok
        
        return helper(root, float('-inf'), float('inf'))