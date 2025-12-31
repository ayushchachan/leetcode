#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            answer = 0
            for l in grid:
                answer += l[0]
            return answer
        minPath = [[0 for _ in range(n)] for _ in range(m)]

        minPath[m - 1][n - 1] = grid[m - 1][n - 1]

        for i in range(m - 2, -1, -1):
            minPath[i][n - 1] = grid[i][n - 1] + minPath[i + 1][n - 1]

        for j in range(n - 2, -1, -1):
            minPath[m - 1][j] = grid[m - 1][j] + minPath[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                minPath[i][j] = grid[i][j] + min(minPath[i + 1][j], minPath[i][j + 1])

        return minPath[0][0]


# @lc code=end
