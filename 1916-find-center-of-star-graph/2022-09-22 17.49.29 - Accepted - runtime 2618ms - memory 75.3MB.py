# There is an undirected star graph consisting of n nodes labeled 
# from 1 to n. A star graph is a graph where there is one center node 
# and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] 
# indicates that there is an edge between the nodes ui and vi. 
# Return the center of the given star graph.

class Solution:
    def findCenter(self, edges):
        g = self.construct_graph(len(edges) + 1, edges)
        for u in g:
            if len(g[u]) == len(edges):
                return u
        raise Exception("Bug in Code")
    
    def construct_graph(self, n, edges):
        G = dict()
        for i in range(1, n + 1):
            G[i] = set()
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        print(G)
        return G
        