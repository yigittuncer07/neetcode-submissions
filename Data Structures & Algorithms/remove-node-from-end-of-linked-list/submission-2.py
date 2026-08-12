# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
    
        target = length - n

        
        i = None
        j = head
        k = head.next

        for _ in range(target):
            
            i = j
            j = j.next
            k = k.next

        if not i:
            return k
        i.next = k

        return head



