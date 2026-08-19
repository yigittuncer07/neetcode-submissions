# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = collections.deque()
        queue.append(root)

        def is_same_tree(n1,n2) -> bool:
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            elif n1.val != n2.val:
                return False

            return is_same_tree(n1.left, n2.left) and is_same_tree(n1.right, n2.right)
            


        while queue:

            node = queue.popleft()


            if node.val == subRoot.val:
                if is_same_tree(node, subRoot):
                    return True
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return False