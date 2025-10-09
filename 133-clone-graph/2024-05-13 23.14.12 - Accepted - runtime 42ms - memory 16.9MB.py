"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if(node == None):
            return None
        q = deque()
        head = Node(node.val)
        currNode = head
        q.append((node, currNode))
        visitedNodes = set()
        visitedNodes2 = {}
        visitedNodes.add(node)
        visitedNodes2[node] = currNode
        while len(q):
            ele, cloneEle = q.popleft()
            for neigh in ele.neighbors:
                if neigh in visitedNodes:
                    cloneEle.neighbors.append(visitedNodes2[neigh])
                    continue
                newNode = Node(neigh.val)
                cloneEle.neighbors.append(newNode)
                q.append((neigh, newNode))
                visitedNodes.add(neigh)
                visitedNodes2[neigh] = newNode
        return head

