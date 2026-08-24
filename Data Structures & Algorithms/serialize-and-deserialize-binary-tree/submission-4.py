# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        queue = collections.deque()

        queue.append(root)

        ans = []

        while queue:
            curr = queue.popleft()

            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                ans.append(curr.val)

            else:
                ans.append(None)
            

        while ans and not ans[-1]:
            ans.pop()

        return json.dumps(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        stack = json.loads(data)[::-1]

        if not stack:
            return None

        previous_level = []
        current_level = [TreeNode(stack.pop())]
        ans = current_level[0]


        while stack:
            for parent in previous_level:
                if not stack:
                    break
                for i in range(2):
                    if not stack:
                        break
                    val = stack.pop()
                    if not i % 2:
                        if val is not None:
                            parent.left = TreeNode(val)
                            current_level.append(parent.left)
                        else:
                            parent.left = val
                    else:
                        if val is not None:
                            parent.right = TreeNode(val)
                            current_level.append(parent.right)
                        else:
                            parent.right = val

            previous_level = current_level[:]
            current_level = []


        return ans





















