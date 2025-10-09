#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]):
        g = []                  ## g is original graph
        adj = []                ## adj is undirected graph
        
        for i in range(n):
            adj.append(set())
            g.append(set())
        
        for u, v in connections:
            adj[u].add(v)
            adj[v].add(u)
            g[u].add(v)
        
        countInversion = 0

        ## start at 0
        from collections import deque
        Q = deque()
        Q.append(0)
        visited = {0}
        while len(Q) != 0:
            u = Q.popleft()
            
            for v in adj[u]:                
                if v not in visited:
                    if v in g[u]:
                        countInversion += 1
                    Q.append(v)
                    visited.add(v)
        return countInversion
                    
# @lc code=end

