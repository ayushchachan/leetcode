class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        m = len(grid)
        n = len(grid[0])

        visit = dict()

        component_size = 0
        max_component_size = 0

        for i in range(m):
            for j in range(n):
                k = self.index(n, i, j)
                if grid[i][j] == 1 and k not in visit:

                    component_size = self.dfs_visit(i, j, m, n, visit)
                    # print("component size =", component_size)
                    if component_size > max_component_size:
                        max_component_size = component_size
        return max_component_size

    def dfs_visit(self, i, j, m, n, visit):
        component_size = 1
        grid = self.grid
        k = self.index(n, i, j)
        visit[k] = True

        k = self.index(n, i - 1, j)
        if i > 0 and grid[i - 1][j] == 1 and k not in visit:
            component_size += self.dfs_visit(i - 1, j, m, n, visit)

        k = self.index(n, i + 1, j)
        if i < m - 1 and grid[i + 1][j] == 1 and k not in visit:
            component_size += self.dfs_visit(i + 1, j, m, n, visit)

        k = self.index(n, i, j - 1)
        if j > 0 and grid[i][j - 1] == 1 and k not in visit:
            component_size += self.dfs_visit(i, j - 1, m, n, visit)

        k = self.index(n, i, j + 1)
        if j < n - 1 and grid[i][j + 1] == 1 and k not in visit:
            component_size += self.dfs_visit(i, j + 1, m, n, visit)

        return component_size

    def index(self, n, r, c):
        return n * r + c
        
