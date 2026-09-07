"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        hm = {}

        def dfs(node):
            if not node:
                return None
            if node in hm:
                return hm[node]

            hm[node] = Node(node.val)

            for nei in node.neighbors:
                hm[node].neighbors.append(dfs(nei))

            return hm[node]


        return dfs(node)                    
                    