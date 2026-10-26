# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subr):
            if (not node) and (not subr):
                return True
            elif (not node) or (not subr):
                return False
            elif node.val==subr.val:
                    return dfs(node.left, subr.left) and dfs(node.right, subr.right)
            else:
                return False
        
        if not root:
            return False
        elif not subRoot:
            return True
        elif dfs(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # return self.isSubtree(root, subRoot)

