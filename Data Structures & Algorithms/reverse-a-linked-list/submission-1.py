# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        def dfs(node):
            if not node:
                return
            if not node.next:
                new_head.next = node
                return node
            next_node = dfs(node.next)
            next_node.next = node
            return node
        node = dfs(head)
        if node:
            node.next = None
        return new_head.next
                

        