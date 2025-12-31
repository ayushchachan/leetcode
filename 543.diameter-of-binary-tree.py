#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(s):
            nonlocal answer

            if s is None:
                return -1
            else:
                height_left = dfs(s.left)
                height_right = dfs(s.right)

                answer = max(answer, 2 + height_left + height_right)
                height = 1 + max(height_left, height_right)
            # print("dfs returned answer =", answer)
            # print("---------------dfs exiting-----------------")
            return height

        dfs(root)
        return answer


# @lc code=end
