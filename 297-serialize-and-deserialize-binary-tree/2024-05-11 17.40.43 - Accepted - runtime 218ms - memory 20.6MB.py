#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST

# @lc code=start
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




import heapq
import queue
from collections import deque


class HuffmanNode:
    def __init__(self, x, key=None):
        self.key = key
        self.val = x
        self.left = None
        self.right = None

    def __lt__(self, b):
        return self.val < b.val

    def __gt__(self, b):
        return self.val > b.val


def getFrequencies(root):
    d = {}
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        p = q.get()
        strP = ""
        if p == None:
            strP = str(p)
        else:
            strP = str(p.val)
        if strP in d:
            if p != None:
                d[str(p.val)] += 1
            else:
                d[str(p)] += 1
        else:
            if p != None:
                d[str(p.val)] = 1
            else:
                d[str(p)] = 1
        if p != None:
            q.put(p.left)
            q.put(p.right)
    return d


def getHuffmanTree(f):
    def traversal(root, code):
        if root.key != None:
            d[root.key] = code
        else:
            traversal(root.left, code + "0")
            traversal(root.right, code + "1")

    d = {}
    q = []
    for k in f.keys():
        heapq.heappush(q, HuffmanNode(f[k], k))

    while len(q) != 0:
        a = heapq.heappop(q)
        # print("A" , a.val,a.key)
        b = None
        if len(q) == 0:
            traversal(a, "")
            # print(d)
            return d
        else:
            b = heapq.heappop(q)
            # print("B" , b.val,b.key)
        node = HuffmanNode(a.val + b.val)
        node.left = a
        node.right = b
        heapq.heappush(q, node)

    # def traversal(root):
    #     if(root == None):
    #         return
    #     print(root.val,root.key)
    #     traversal(root.left)
    #     traversal(root.right)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # print(getFrequencies(root))
        s = ""
        Codec.codes = getHuffmanTree(getFrequencies(root))
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            e = q.get()
            if e == None:
                s += Codec.codes[str(None)]
                continue

            s += Codec.codes[str(e.val)]
            q.put(e.left)
            q.put(e.right)

        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        codesO = {}
        for k in Codec.codes.keys():
            codesO[Codec.codes[k]] = k
        head = None
        currWord = ""
        q = deque()

        ## Head
        i = 0
        while i < len(data):
            c = data[i]
            currWord += c
            if currWord in codesO:
                head = TreeNode(int(codesO[currWord]))
                q.append(head)
                currWord = ""
                break
            i += 1
        i += 1

        while i < len(data):
            currNode = q.popleft()
            # Left Node
            currCode = ""
            while currCode not in codesO:
                currCode += data[i]
                i += 1
            value = codesO[currCode]
            if value == "None":
                leftN = None
            else:
                leftN = TreeNode(int(value))
                q.append(leftN)

            # Right Node
            currCode = ""
            while currCode not in codesO:
                currCode += data[i]
                i += 1

            value = codesO[currCode]
            if value == "None":
                rightN = None
            else:
                rightN = TreeNode(int(value))
                q.append(rightN)

            currNode.left = leftN
            currNode.right = rightN            
        return head


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:


# @lc code=end
