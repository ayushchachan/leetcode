#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        parent = dict()

        connected_components = 0

        for s in range(n):
            if s not in parent:
                parent[s] = None
                connected_components += 1
                ## starts bfs(G, s)

                Q = deque()
                Q.append(s)

                while len(Q) > 0:
                    u = Q.popleft()
                    for v in range(n):
                        if isConnected[u][v] == 1 and v not in parent:
                            Q.append(v)
                            parent[v] = u

        return connected_components


# @lc code=end
