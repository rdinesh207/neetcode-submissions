# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node and node.next:
            if node.next.next==head.next:
                return True
            head = head.next
            node = node.next.next
        return False


            
        