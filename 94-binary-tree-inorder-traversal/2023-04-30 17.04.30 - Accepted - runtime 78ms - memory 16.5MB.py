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
        while len(S) > 0:
            print("S all =", None in S)
            x = S[-1]
            while x:
                print("entering 1st while loop")
                print("x = ", x.val)
                x = x.left
                if x:
                    S.append(x)
            print("exiting 1st while loop")

            while S and  S[-1].right is None:
                answer.append(S.pop().val)
                print("answer =", answer)
                print("S =", S)
            if S:
                print("YES")
                x = S.pop()
                answer.append(x.val)
                S.append(x.right)
        return answer