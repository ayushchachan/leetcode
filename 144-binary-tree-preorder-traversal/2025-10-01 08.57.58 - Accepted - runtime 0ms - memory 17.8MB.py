
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        stack = []
        if root != None:
            stack.append(root)
        answer = []

        while (len(stack) != 0):
            x = stack.pop()
            answer.append(x.val)

            if x.right is not None:
                stack.append(x.right)

            if x.left is not None:
                stack.append(x.left)
        
        return answer