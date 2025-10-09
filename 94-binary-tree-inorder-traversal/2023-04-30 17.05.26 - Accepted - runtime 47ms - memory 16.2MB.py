# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        S = [root]
        answer = []
        while S:
            x = S[-1]
            while x:
                x = x.left
                if x:
                    S.append(x)


            while S and  S[-1].right is None:
                answer.append(S.pop().val)
            if S:
                x = S.pop()
                answer.append(x.val)
                S.append(x.right)
        return answer