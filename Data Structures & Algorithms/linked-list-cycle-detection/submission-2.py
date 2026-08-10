# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # due to the index thing, the cycle always should end at the second node in the list.

        seen = set()
        tail = head
        for i in range(1000):
            if not tail:
                return False
            
            if tail in seen:
                return True
            
            seen.add(tail)

            tail = tail.next
        
        return False
