# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = queue.Queue()
        i = 0
        res = []
        if(root == None):
            return []
        q.put((root, 0))
        while not q.empty():
            ele = q.get()
            if ele[1] >= i:
                res.append(ele[0].val)
                i += 1
            q.put((ele[0].right, ele[1] + 1)) if ele[0].right != None else ""
            q.put((ele[0].left, ele[1] + 1)) if ele[0].left != None else ""
        return res

