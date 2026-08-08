# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev        
            
            
            prev = current
            current = next_node

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        
        return new_head




