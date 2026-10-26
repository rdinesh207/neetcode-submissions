# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(m, n):
            # print(m.val, n.val)
            if m is None or n is None:
                if m is None and n is None:
                    return True
                else:
                    return False
            if m.val==n.val:
                # print(m.val, n.val)
                if m.val is None:
                    return True
                else:
                    return dfs(m.left, n.left) and dfs(m.right, n.right)
                
            return False
        return dfs(p,q)
        