# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = set()
        answer = []
        stack = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            x = stack.pop()

            if x not in visited:
                visited.add(x)
                if x.right is not None:
                    stack.append(x.right)
                stack.append(x)
                if x.left is not None:
                    stack.append(x.left)
            else:
                answer.append(x.val)
        return answer
        