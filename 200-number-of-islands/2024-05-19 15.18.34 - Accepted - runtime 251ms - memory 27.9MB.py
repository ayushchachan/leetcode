class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfComponents = 0
        visitedNodes = set()

        def validate(row, col):
            if (row, col) in visitedNodes:
                return False
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                return False
            if(grid[row][col] != "1"):
                return False
            return True

        def dfs(row, col):
            key = (row, col)

            visitedNodes.add(key)

            ##Up
            if validate(row - 1, col):
                dfs(row - 1, col)

            ##Down
            if validate(row + 1, col):
                dfs(row + 1, col)

            ##Left
            if validate(row, col - 1):
                dfs(row, col - 1)

            ##Right
            if validate(row, col + 1):
                dfs(row, col + 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                key = (r, c)
                if key in visitedNodes or grid[r][c] != "1":
                    continue
                noOfComponents += 1
                dfs(r, c)
        return noOfComponents

