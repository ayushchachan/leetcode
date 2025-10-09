class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        left = 0
        up = 0
        r = 0
        c = -1
        res = []
        while True:
            ##Right
            c += 1
            if c > right:
                return res
            
            while c <= right:
                res.append(matrix[r][c])
                c += 1
            c -= 1
            up += 1
            ##Down
            r += 1
            if r > down:
                return res
            while r <= down:
                res.append(matrix[r][c])
                r += 1
            r -= 1
            right -= 1

            ##Left
            c -= 1
            if c < left:
                return res
            while c >= left:
                res.append(matrix[r][c])
                c -= 1
            c += 1
            down -= 1
            ##Up
            r -= 1
            if r < up:
                return res
            while r >= up:
                res.append(matrix[r][c])
                r -= 1
            r += 1
            left += 1

