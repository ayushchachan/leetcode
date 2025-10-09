# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.helper(nums, 0, len(nums) - 1)
        print(root)
        return root

    def helper(self, nums, i, j):
        if i > j:
            return None
        mid = (i + j) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, i, mid - 1)
        node.right = self.helper(nums, mid + 1, j)
        return node

