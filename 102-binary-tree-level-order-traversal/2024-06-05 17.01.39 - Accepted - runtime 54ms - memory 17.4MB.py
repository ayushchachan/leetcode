# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        q.put((root,0))
        res = []
        while(not q.empty()):
            ele = q.get()
            if(ele[0] == None):
                continue
            if(len(res) < ele[1] + 1):
                res.append([ele[0].val])
            else:
                res[ele[1]].append(ele[0].val)
            q.put((ele[0].left,ele[1] + 1))
            q.put((ele[0].right,ele[1] + 1))
        return res

        