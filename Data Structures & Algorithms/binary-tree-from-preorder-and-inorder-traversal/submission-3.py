# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            # Base case: if there are no elements to construct the tree
            if left > right:
                return None
            
            # The current root is the current element in preorder
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1
            
            # Find the index of this root in inorder traversal
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root

        return build(0, len(inorder) - 1)