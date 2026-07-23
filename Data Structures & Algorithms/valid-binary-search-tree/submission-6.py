# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(root, l_bound, r_bound):
            if not root: return True
            if root.val<=l_bound or root.val>=r_bound: return False
            return ( dfs(root.left, l_bound, root.val) and dfs(root.right, root.val, r_bound) )
        return (dfs(root, float('-inf'), float('inf')))