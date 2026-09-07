"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs version
        if not node:
            return None

        stack = []
        hm = {node: Node(node.val)}
        stack.append(node)

        while stack:

            curr = stack.pop()

            for nei in curr.neighbors:
                if nei not in hm:
                    hm[nei] = Node(nei.val)
                    stack.append(nei)

                hm[curr].neighbors.append(hm[nei])
        
        return hm[node]