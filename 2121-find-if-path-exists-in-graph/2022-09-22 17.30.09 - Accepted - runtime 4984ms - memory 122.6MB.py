class Solution:
    def validPath(self, n, edges, source, destination):
        if (source == destination):
            return True
        g = self.construct_graph(n ,edges)
        # sleep(2)
        visit = {}
        Q = [[source]]
        
        while Q[-1]:
            print("Q =", Q)
            Q.append([])
            
            for u in Q[-2]:
                print("u = ", u)
                # sleep(1)
                visit[u] = True
                
                for v in g[u]:
                    print("v =", v)
                    # sleep(1)
                    if v == destination:
                        return True
                    if v not in visit:
                        Q[-1].append(v)
                
        return False
    
    def construct_graph(self, n, edges):
        G = dict()
        for i in range(n):
            G[i] = set()
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        print(G)
        return G
            
 