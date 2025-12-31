#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        x = root
        parent_x = None
        while x is not None:
            if val < x.val:
                parent_x, x = x, x.left
            else:
                parent_x, x = x, x.right
        if val < parent_x.val:
            parent_x.left = TreeNode(val)
        else:
            parent_x.right = TreeNode(val)
        return root


# @lc code=end
