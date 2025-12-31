#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


# @lc code=start
class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        originalVal = image[sr][sc]

        if image[sr][sc] == color:
            return image

        M, N = len(image), len(image[0])

        from collections import deque

        Q = deque()

        Q.append((sr, sc))
        while len(Q) > 0:
            i, j = Q.popleft()
            image[i][j] = color

            ## upper element
            if i > 0 and image[i - 1][j] == originalVal:
                Q.append((i - 1, j))

            ## bottom element
            if i < M - 1 and image[i + 1][j] == originalVal:
                Q.append((i + 1, j))

            ## left element
            if j > 0 and image[i][j - 1] == originalVal:
                Q.append((i, j - 1))

            ## right element
            if j < N - 1 and image[i][j + 1] == originalVal:
                Q.append((i, j + 1))
        return image


# @lc code=end
