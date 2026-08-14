"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        nodes = {}
        current = head
        index = 0

        while current:
            nodes[current] = Node(x = current.val)
            current = current.next
        

        current = head

        while current:

            if current.next:
                nodes[current].next = nodes[current.next]
            if current.random:
                nodes[current].random = nodes[current.random]
            current = current.next
        
        return nodes[head]