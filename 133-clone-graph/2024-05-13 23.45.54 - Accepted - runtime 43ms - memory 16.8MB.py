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
        if node == None:
            return None
        newNode = Node(node.val)
        head = newNode
        visitedNodes = {}
        visitedNodes[node] = newNode
        q = deque()
        q.append(node)
        while(len(q)):
            ele = q.popleft()
            for neigh in ele.neighbors:
                if(neigh not in visitedNodes):
                    newNode = Node(neigh.val)
                    q.append(neigh)
                    visitedNodes[neigh] = newNode
                visitedNodes[ele].neighbors.append(visitedNodes[neigh])

        return head

