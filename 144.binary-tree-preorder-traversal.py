#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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

# @lc code=end

