#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        Q = [[]]
        if root is not None:
            Q[0].append(root)

        while len(Q[-1]) > 0:
            Q.append([])

            for u in Q[-2]:
                if u.left is not None:
                    Q[-1].append(u.left)
                if u.right is not None:
                    Q[-1].append(u.right)
        Q.pop()
        answer = []
        for level in Q:
            answer.append(level[-1].val)
        return answer


# @lc code=end
