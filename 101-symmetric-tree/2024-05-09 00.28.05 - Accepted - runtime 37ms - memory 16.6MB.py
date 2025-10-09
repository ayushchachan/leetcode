# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True
        return self.checkSymmetric(root.left,root.right)
    def checkSymmetric(self,a,b):
        if(a == None):
            if(b != None):
                return False
            return True
            
        if(b == None):
            if(a != None):
                return False
            return True
        return a.val == b.val and self.checkSymmetric(a.left,b.right) and self.checkSymmetric(a.right,b.left) 
        