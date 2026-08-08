# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        next_node = head
        while next_node:
            next_node = current.next
            current.next = prev        
            
            
            prev = current
            if next_node:
                current = next_node

        return current