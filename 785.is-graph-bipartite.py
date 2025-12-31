#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = dict()

        for s in range(len(graph)):
            if s not in color:
                color[s] = True  ## white color
                ## start bfs here

                Q = deque()
                Q.append(s)

                while len(Q) > 0:
                    u = Q.popleft()

                    for v in graph[u]:
                        if v not in color:
                            color[v] = not color[u]
                            Q.append(v)
                        else:
                            if color[v] == color[u]:
                                return False
        return True


# @lc code=end
