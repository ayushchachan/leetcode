#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        fresh_oranges = 0
        rotten_oranges = deque()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append((i, j))

        minutes = 0
        while len(rotten_oranges) > 0:

            R = len(rotten_oranges)

            for k in range(R):
                i, j = rotten_oranges.popleft()
                # print("checking --> ", (i, j))

                ## check up
                if i > 0 and grid[i - 1][j] == 1:
                    rotten_oranges.append((i - 1, j))
                    grid[i - 1][j] = 2
                    fresh_oranges -= 1

                ## check bottom
                if i < M - 1 and grid[i + 1][j] == 1:
                    rotten_oranges.append((i + 1, j))
                    grid[i + 1][j] = 2
                    fresh_oranges -= 1

                ## check left
                if j > 0 and grid[i][j - 1] == 1:
                    rotten_oranges.append((i, j - 1))
                    grid[i][j - 1] = 2
                    fresh_oranges -= 1

                ## check right
                if j < N - 1 and grid[i][j + 1] == 1:
                    rotten_oranges.append((i, j + 1))
                    grid[i][j + 1] = 2
                    fresh_oranges -= 1

            if len(rotten_oranges) > 0:
                minutes += 1
        if fresh_oranges != 0:
            return -1
        return minutes


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

S = Solution()
print(S.orangesRotting(grid))
# @lc code=end
