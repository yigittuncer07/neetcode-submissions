# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        stack = []

        def dfs(node):
            if not node:
                return 

            if not stack or node.val >= stack[-1]:
                nonlocal ans
                ans += 1
                stack.append(node.val)

            if node.left:
                val = dfs(node.left)
                if val and val == stack[-1]:
                    stack.pop()
            if node.right:
                val = dfs(node.right)
                if val and val == stack[-1]:
                    stack.pop()
            return node.val
        
        dfs(root)
        return ans