class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        
        answer = []

        i = 0
        j = 0
        
        for k in range(m + n - 1):
            if k % 2 == 0:              ## k is even, upward movement
                while i >= 0 and j < n:
                    answer.append(mat[i][j])
                    i -= 1
                    j += 1
                if i == -1:
                    i = i + 1
                    if j == n:
                        i = i - 1
                if j == n:
                    j = j - 1
                    i = i + 2
            else:                       ## k is odd, downward movement
                while i < m and j >= 0:
                    answer.append(mat[i][j])
                    i += 1
                    j -= 1
                if j == -1:
                    j = j + 1
                    if i == m:
                        j = j - 1
                if i == m:
                        i = i - 1
                        j = j + 2
        return answer
                    
        
        
     