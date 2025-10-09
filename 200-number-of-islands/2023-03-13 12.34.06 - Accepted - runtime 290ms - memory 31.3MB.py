class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        m = len(grid)
        n = len(grid[0])

        visit = dict()

        components = 0

        for i in range(m):
            for j in range(n):
                k = self.index(n, i, j)
                if grid[i][j] == '1' and k not in visit:
                    # print("-----")
                    components += 1
                    self.dfs_visit(i, j, m, n, visit)
        return components

    def dfs_visit(self, i, j, m, n, visit):
        grid = self.grid
        k = self.index(n, i, j)
        visit[k] = True

        k = self.index(n, i - 1, j)
        if i > 0 and grid[i - 1][j] == '1' and k not in visit:
            self.dfs_visit(i - 1, j, m, n, visit)

        k = self.index(n, i + 1, j)
        if i < m - 1 and grid[i + 1][j] == '1' and k not in visit:
            self.dfs_visit(i + 1, j, m, n, visit)

        k = self.index(n, i, j - 1)
        if j > 0 and grid[i][j - 1] == '1' and k not in visit:
            self.dfs_visit(i, j - 1, m, n, visit)

        k = self.index(n, i, j + 1)
        if j < n - 1 and grid[i][j + 1] == '1' and k not in visit:
            self.dfs_visit(i, j + 1, m, n, visit)

    def index(self, n, r, c):
        return n * r + c

