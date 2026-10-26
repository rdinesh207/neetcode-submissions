# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        first = head
        second = head.next
        while first.next:
            if (not second or not second.next or not second.next.next) or not first.next:
                return False
            if first.val==second.val:
                return True
            first = first.next
            second = second.next.next
        return False
            
        