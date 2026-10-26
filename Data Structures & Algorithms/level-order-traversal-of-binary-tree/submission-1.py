# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ml = []
        def addl(node, idx):
            if len(ml)<idx+1 and node.val is not None:
                ml.append([])
            print(ml, node.val)
            ml[idx].append(node.val)
            if node.left is not None:
                addl(node.left,idx+1)
            if node.right is not None:
                addl(node.right, idx+1)
            return
        addl(root, 0)
        return ml
        