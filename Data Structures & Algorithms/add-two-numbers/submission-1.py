# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        

        c1, c2 = l1, l2
        new_head = ListNode()
        current = new_head
        carry = 0
        while c1 and c2:

            csum = c1.val + c2.val + carry

            carry = math.floor(csum / 10)

            csum = csum % 10

            current.next = ListNode(val=csum)
            current = current.next

            c1 = c1.next
            c2 = c2.next

        while c1:
            csum = c1.val + carry
            carry = math.floor(csum / 10)
            csum = csum % 10
            current.next = ListNode(val=csum)
            current = current.next

            c1 = c1.next
        while c2:
            csum = c2.val + carry
            carry = math.floor(csum / 10)
            csum = csum % 10
            current.next = ListNode(val=csum)
            current = current.next

            c2 = c2.next

        if carry:
            current.next = ListNode(val=carry)

        return new_head.next
                    

        