#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        from collections import deque

        q = deque()
        if root is not None:
            q.append(root)

        while len(q) != 0:
            x = q.popleft()

            if x.left == None and x.right == None:
                if x.val == targetSum:
                    return True

            if x.left is not None:
                q.append(x.left)
                x.left.val += x.val

            if x.right is not None:
                q.append(x.right)
                x.right.val += x.val

        return False


# @lc code=end
