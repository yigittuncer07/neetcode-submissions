# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        # ans node
        ans = ListNode(0, head)
        should_set_ans = True
        
        # node pointing to previous groups head
        prev_head = head
        current_head = None

        current = head
        prev = None
        while True:
            # check if next k nodes exist
            end_node = self.check_next_k(current, k)
            if end_node:
                while True:
                    # reversal block
                    nxt = current.next
                    current.next = prev
                    prev = current
                    current = nxt

                    # if at final node of reversal, break
                    if prev == end_node:
                        if should_set_ans:
                            ans.next = prev
                            should_set_ans = False
                        else:
                            prev_head.next = prev
                            prev_head = current_head
                        current_head = current
                        break
            else:
                prev_head.next = current
                break
        return ans.next
                



    def check_next_k(self, head, k) -> Optional[ListNode]:
        curr = head
        for i in range(k - 1):
            if not curr:
                return None
            curr = curr.next
        
        return curr