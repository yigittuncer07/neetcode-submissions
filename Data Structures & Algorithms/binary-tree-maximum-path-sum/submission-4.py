# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        
        def dfs(root) -> int:
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            nonlocal ans
            ans = max(ans, root.val + max(0,left_max) + max(0,right_max))

            return root.val + max(left_max, right_max, 0)

        dfs(root)
        return ans