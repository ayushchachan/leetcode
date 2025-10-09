# In a town, there are n people labeled from 1 to n. 
# There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] 
# representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists 
# and can be identified, or return -1 otherwise.

class Solution:
    def findJudge(self, n, trust):
        g = self.construct_graph(n, trust)
        for u in g:
            if len(g[u][1]) == n - 1 and len(g[u][0]) == 0:
                return u
        return -1
    
    def construct_graph(self, n, edges):
        G = dict()
        for i in range(1, n + 1):
            G[i] = (set(), set())       ## (outgoing edges, incoming edges)
        for u, v in edges:
            G[u][0].add(v)
            G[v][1].add(u)

        return G