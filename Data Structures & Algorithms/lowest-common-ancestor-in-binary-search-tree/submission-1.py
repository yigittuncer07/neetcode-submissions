# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans = root
        current = root
        while current:
            if current.val == p.val or current.val == q.val:
                return current

            if p.val < current.val and q.val < current.val:
                ans = current 
                current = current.left

            elif p.val > current.val and q.val > current.val:
                ans = current
                current = current.right

            else:
                ans = current
                break
            
        return ans