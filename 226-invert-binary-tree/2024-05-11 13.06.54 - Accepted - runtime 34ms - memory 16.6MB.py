# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            root.left, root.right = root.right, root.left
            invert(root.left) if root.left != None else ""
            invert(root.right) if root.right != None else ""
            return root
        if(root != None):
            return invert(root)
        return root


