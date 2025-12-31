#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root.val == key:
            return None
        x = root
        parent_x = None

        while (x is not None) and (x.val != key):
            print("x = ", x.val)
            if key < x.val:
                parent_x, x = x, x.left
            else:
                parent_x, x = x, x.right
        if x is None:
            return None

        ## x is the node to delete
        if x.right is not None:
            ## find successor of x in x's right subtree
            parent_z, z = x, x.right
            while z.left is not None:
                parent_z, z = z, z.left

        else:
            ## find predecessor of x in x's left subtree
            parent_z, z = x, x.left
            while z.right is not None:
                parent_z, z = z, z.right

            ## z is the predecessor of x

        ## z is the successor of x
        x.val = z.val
        if z == parent_z.left:
            parent_z.left = None
        else:
            parent_z.right = None

        return root


# @lc code=end
