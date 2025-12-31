#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = [[]]
        Q = [[]]
        if root is not None:
            order[0].append(root.val)
            Q[0].append(root)

        while len(Q[-1]) > 0:
            Q.append([])
            order.append([])

            for u in Q[-2]:
                if u.left is not None:
                    Q[-1].append(u.left)
                    order[-1].append(u.left.val)

                if u.right is not None:
                    Q[-1].append(u.right)
                    order[-1].append(u.right.val)
            if len(order) % 2 == 0:
                order[-1].reverse()
        order.pop()
        return order


# @lc code=end
