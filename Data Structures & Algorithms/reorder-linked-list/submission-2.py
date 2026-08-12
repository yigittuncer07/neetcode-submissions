# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # cut off the list
        prev.next = None
        middle = slow

        # reverse after the middle 
        prevN = None
        while middle:
            nextN = middle.next
            middle.next = prevN
            prevN = middle
            middle = nextN

        current_second_half = prevN
        
        current = head
        while current and current_second_half:
            nextN = current.next
            current.next = current_second_half
            nextN2 = current_second_half.next
            if nextN:
                current_second_half.next = nextN
            current = nextN
            current_second_half = nextN2
