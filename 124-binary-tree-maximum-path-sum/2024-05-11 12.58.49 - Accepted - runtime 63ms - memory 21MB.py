# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        resMax = float("-inf")

        def maxSum(root):
            nonlocal resMax  # Declare resMax as nonlocal
            leftSum = maxSum(root.left) if root.left != None else 0
            rightSum = maxSum(root.right) if root.right != None else 0
            resMax = max(resMax, root.val + leftSum + rightSum)
            res = max(max(root.val + leftSum, root.val + rightSum), root.val)
            resMax = max(res, resMax)
            return res

        maxSum(root)
        return resMax

