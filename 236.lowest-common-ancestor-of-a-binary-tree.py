#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        from collections import deque

        Q = deque()
        Q.append(root)
        parent = {root: None}
        height = {root: 0}

        while len(Q) > 0:
            x = Q.popleft()

            if x.left is not None:
                Q.append(x.left)
                parent[x.left] = x
                height[x.left] = height[x] + 1

            if x.right is not None:
                Q.append(x.right)
                parent[x.right] = x
                height[x.right] = height[x] + 1

            if p in parent and q in parent:
                break

        while height[q] > height[p]:
            q = parent[q]

        while height[p] > height[q]:
            p = parent[p]

        ## p and q are at same height

        while p != q:
            p = parent[p]
            q = parent[q]
        return p


# @lc code=end
