# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root.left,root.right)
    def checkSymmetric(self,root1,root2):
        if(root1 == None):
            return root2 == None
        if(root2 ==None):
            return root1 == None
        return root1.val == root2.val and self.checkSymmetric(root1.left,root2.right) and self.checkSymmetric(root1.right,root2.left)
        