# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) != 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                merged_lists.append(self.merge_two_lists(lists[i],lists[i+1] if i+1 < len(lists) else None))
            
            lists = merged_lists
        return lists[0]


    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current = head

        while list1 or list2:
            if not list1:
                current.next = list2
                list2 = list2.next
            elif not list2:
                current.next = list1
                list1 = list1.next
            
            elif list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        return head.next

            
            





            