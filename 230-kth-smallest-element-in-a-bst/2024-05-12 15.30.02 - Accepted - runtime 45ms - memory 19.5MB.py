# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k

        def preOrderTraversal():
            nonlocal count
            st = []
            st.append(root)
            while len(st):
                ##Traversing to the left
                while st[-1].left != None:
                    st.append(st[-1].left)
                ele = st.pop()
                count -= 1
                if count == 0:
                    return ele.val

                ##While ele.right
                while ele.right == None:
                    ele = st.pop()
                    count -= 1
                    if count == 0:
                        return ele.val
                
                st.append(ele.right)

        return preOrderTraversal()

