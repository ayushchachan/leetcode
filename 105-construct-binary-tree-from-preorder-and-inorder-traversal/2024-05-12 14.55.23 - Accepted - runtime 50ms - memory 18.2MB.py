# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preOrderPointer = 0
        indexDict = {}
        for i in range(len(inorder)):
            indexDict[inorder[i]] = i

        head = None

        def buildTree(i, j):
            nonlocal preOrderPointer, head
            if i == j:
                newNode = TreeNode(preorder[preOrderPointer])
                preOrderPointer += 1
                return newNode
            elif i > j:
                return None
            else:
                node = TreeNode(preorder[preOrderPointer])
                preOrderPointer += 1
                node.left = buildTree(i, indexDict[node.val] - 1)
                node.right = buildTree(indexDict[node.val] + 1, j)
                return node

        return buildTree(0, len(inorder) - 1)


