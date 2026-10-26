# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        mergedlist = []
        while len(lists)>1:
            mergedlist = []
            for i in range(0, len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedlist.append(self.merge2(l1, l2))
            lists=mergedlist
        return lists[0]

    def merge2(self, l1, l2):
        start = ListNode()
        end = start
        while l1 and l2:
            if l1.val<l2.val:
                end.next = l1
                l1 = l1.next
            else:
                end.next = l2
                l2 = l2.next
            end = end.next
        if l1:
            end.next = l1
        if l2:
            end.next = l2
        return start.next

