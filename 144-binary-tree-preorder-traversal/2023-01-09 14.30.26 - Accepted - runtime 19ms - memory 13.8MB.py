# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        S = []
        if root:
            S.append(root)
        result = []

        while S:
            x = S.pop()
            result.append(x.val)
            if x.right:
                S.append(x.right)
            if x.left:
                S.append(x.left)
        return result
        
