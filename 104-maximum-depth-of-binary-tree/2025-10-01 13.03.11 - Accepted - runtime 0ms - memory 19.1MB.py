# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        Q = [[]]
        if root is not None:
            Q[0].append(root)
        while len(Q[-1]) != 0:
            Q.append([])
            for u in Q[-2]:
                if u.left is not None:
                    Q[-1].append(u.left)
                if u.right is not None:
                    Q[-1].append(u.right)
        # print(Q)
        return len(Q) - 1