# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = collections.deque()

        queue.append(root)

        while queue[0]:
            node = queue.popleft()

            if abs(self.get_height(node.left) - self.get_height(node.right)) > 1:
                return False

            queue.append(node.left)
            queue.append(node.right)
        
        return True

    def get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        return max(self.get_height(node.left), self.get_height(node.right)) + 1