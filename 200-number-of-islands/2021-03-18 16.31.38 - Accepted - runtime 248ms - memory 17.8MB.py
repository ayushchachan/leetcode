class Solution:    
    def numIslands(self, grid):
        self.m = len(grid);
        self.n = len(grid[0]);

        nZeroes = 0;

        for ls in grid:
            nZeroes += ls.count('0');

        uf1 = UnionFind(self.m * self.n);

        for i in range(self.m):
            for j in range(self.n):
                #print("i = ", i, ", j = ", j);
                h1 = i*self.n + j;
                e1 = int(grid[i][j]);
                if (e1 == 1):

                    ## checking top                 
                    if (self.isValid(i - 1, j) and int(grid[i - 1][j]) == 1):
                        #print("top exists");
                        
                        h2 = (i - 1)*self.n + j;
                        uf1.union(h2, h1)

                    ## checking bottom
                    if (self.isValid(i + 1, j) and int(grid[i + 1][j]) == 1):
                        #print("bottom exists");
 
                        h2 = (i + 1)*self.n + j;
                        uf1.union(h2, h1);
                        
                   
                    ## checking left
                    if (self.isValid(i, j - 1) and  int(grid[i][j - 1]) == 1):
                        
                        h2 = (i)*self.n + j - 1;
                        uf1.union(h2, h1);

                    ## checking right
                    if (self.isValid(i, j + 1) and int(grid[i][j + 1]) == 1):
                        
                        h2 = (i)*self.n + j + 1;
                        uf1.union(h2, h1);
        return uf1.noOfconnectedComponents() - nZeroes;

    def isValid(self, i, j):
        return (0 <= i < self.m) and (0 <= j < self.n);




    


class UnionFind():
    def __init__(self, n):
        self.id = [i for i in range(n)];
        self.sz = [1 for i in range(n)];
        self.count = n;     ##no. of connected components
        
    def find(self, p):
        #print('p = ', p);
        while (len(self.id) > p >= 0 and self.id[p] != p):
            #print('p = ', p);
            p = self.id[p];
        return self.id[p];

    def union(self, p, q):
        if (self.find(p) != self.find(q)):
            pRoot = self.find(p);
            qRoot = self.find(q);

            if (self.sz[qRoot] < self.sz[pRoot]):
                self.id[qRoot] = pRoot;
                self.sz[pRoot] = self.sz[pRoot] + self.sz[qRoot];

            else:
                self.id[pRoot] = qRoot;
                self.sz[qRoot] = self.sz[qRoot] + self.sz[pRoot];
 
            self.count -= 1;

    def noOfconnectedComponents(self):
        return self.count;

a = [[1], [1]]

s = Solution();
##print(s.numIslands(a))

