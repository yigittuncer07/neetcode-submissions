"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs
        if not node:
            return None

        deq = collections.deque()
        hm = {
            node: Node(node.val)
        }
        deq.append(node)

        while deq:

            curr = deq.popleft()

            for nei in curr.neighbors:
                if nei not in hm:
                    hm[nei] = Node(nei.val)
                    deq.append(nei)
                hm[curr].neighbors.append(hm[nei])

        return hm[node]