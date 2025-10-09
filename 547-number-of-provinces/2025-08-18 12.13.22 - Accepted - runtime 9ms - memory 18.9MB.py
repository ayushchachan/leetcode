class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # need to find the number of connected components
        
        # we'll use union find
        n = len(isConnected)
        uf = UnionFind3(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count()
        


class UnionFind3():
    def __init__(self, n):
        
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]
        
        self.components_count = n      # NUMBER OF CONNECTED COMPONENTS
    
    def count(self):
        return self.components_count
    
    def isConnected(self, x, y):
        return self.find_set(x) == self.find_set(y)
    
    def find_set(self, x):
        while self.id[x] != x:
            x = self.id[x]
        return x
    
    def union(self, p, q):
        pID = self.find_set(p)
        qID = self.find_set(q)
        
        if (pID == qID):
            return
        
        if (self.sz[pID] < self.sz[qID]):
            self.id[pID] = qID
            self.sz[qID] += self.sz[pID]
        else:
            self.id[qID] = pID
            self.sz[pID] += self.sz[qID]
            
        
        self.components_count -= 1

        