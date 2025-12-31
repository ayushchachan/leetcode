#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#


# @lc code=start
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        M, N = len(mat), len(mat[0])
        dist = [[-1 for _ in range(N)] for _ in range(M)]

        from collections import deque

        Q = deque()

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    Q.append((i, j))

        while len(Q) > 0:
            i, j = Q.popleft()

            ## start bfs at row, col

            ## check left
            if j > 0 and dist[i][j - 1] == -1:
                dist[i][j - 1] = dist[i][j] + 1
                Q.append((i, j - 1))

            ## check right
            if j < N - 1 and dist[i][j + 1] == -1:
                dist[i][j + 1] = dist[i][j] + 1
                Q.append((i, j + 1))

            ## check above
            if i > 0 and dist[i - 1][j] == -1:
                dist[i - 1][j] = dist[i][j] + 1
                Q.append((i - 1, j))

            ## check below
            if i < M - 1 and dist[i + 1][j] == -1:
                dist[i + 1][j] = dist[i][j] + 1
                Q.append((i + 1, j))

        return dist


S = Solution()

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

S.updateMatrix(mat)
# @lc code=end
