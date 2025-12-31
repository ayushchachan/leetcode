#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from collections import deque


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        land_count = 0
        Q = deque()

        boundary_count = 0

        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_count += 1
                    if (i == 0) or (j == 0) or (i == m - 1) or (j == n - 1):
                        visited.add(get_hash(i, j, n))
                        boundary_count += 1
                        Q.append((i, j))

        while len(Q) > 0:
            i, j = Q.popleft()

            ## check above
            if (
                (i > 0)
                and (grid[i - 1][j] == 1)
                and (get_hash(i - 1, j, n) not in visited)
            ):
                Q.append((i - 1, j))
                visited.add(get_hash(i - 1, j, n))
                boundary_count += 1

            ## check below
            if (
                (i < m - 1)
                and (grid[i + 1][j] == 1)
                and (get_hash(i + 1, j, n) not in visited)
            ):
                Q.append((i + 1, j))
                visited.add(get_hash(i + 1, j, n))
                boundary_count += 1

            ## check left
            if (
                (j > 0)
                and (grid[i][j - 1] == 1)
                and (get_hash(i, j - 1, n) not in visited)
            ):
                Q.append((i, j - 1))
                visited.add(get_hash(i, j - 1, n))
                boundary_count += 1

            ## check right
            if (
                (j < n - 1)
                and (grid[i][j + 1] == 1)
                and (get_hash(i, j + 1, n) not in visited)
            ):
                Q.append((i, j + 1))
                visited.add(get_hash(i, j + 1, n))
                boundary_count += 1

        return land_count - boundary_count


def get_hash(i, j, n):
    return (i * n) + j


S = Solution()
grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
]

print(S.numEnclaves(grid))
# @lc code=end
