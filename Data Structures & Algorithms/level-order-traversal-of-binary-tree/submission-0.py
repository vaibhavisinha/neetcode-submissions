# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, st = [],[root]

        while st:
            len_st = len(st)
            temp = []
            for _ in range(len_st):
                node = st.pop(0)
                if node:
                    temp.append(node.val)
                    if node.left : st.append(node.left)
                    if node.right : st.append(node.right)
            res.append(temp[:])
        return res