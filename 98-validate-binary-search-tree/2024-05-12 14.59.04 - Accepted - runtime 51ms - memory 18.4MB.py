# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(root, minR, maxR):
            if root == None:
                return True
            return (
                minR < root.val < maxR
                and validateBST(root.left, minR, root.val)
                and validateBST(root.right, root.val, maxR)
            )
        return validateBST(root,float('-inf'),float('inf'))

