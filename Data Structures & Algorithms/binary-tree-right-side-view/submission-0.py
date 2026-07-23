# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        st, res = [root], []

        while st:
            len_st = len(st)
            right_node = None
            for _ in range(len_st):
                node = st.pop(0)
                if not node: continue
                right_node = node.val
                if node.left : st.append( node.left )
                if node.right : st.append( node.right)
            if right_node: res.append(right_node)
        return res
