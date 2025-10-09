#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start

def makeRCZero(matrix,r,c):
    ##Make row zero
    for cIndex in range(len(matrix[0])):
        if(matrix[r][cIndex] in ['r','r-c']):
            break

        if(cIndex == c or matrix[r][cIndex] != 0):
            if(matrix[r][cIndex] == 'c'):
                matrix[r][cIndex] = 'r-c'

            elif(matrix[r][cIndex] == 'r-c'):
                matrix[r][cIndex] = 'r-c'

            else:
                matrix[r][cIndex] = 'r'

    ##Make col zero
    for rIndex in range(len(matrix)):
        if(matrix[rIndex][c] in ['c','r-c']):
            break
    
        if(rIndex == r or matrix[rIndex][c] != 0):
            if(matrix[rIndex][c] == 'r'):
                matrix[rIndex][c] = 'r-c'

            elif(matrix[rIndex][c] == 'r-c'):
                matrix[rIndex][c] = 'r-c'

            else:
                matrix[rIndex][c] = 'c'

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ele = matrix[r][c]
                if(self.isFlagged(ele)):
                    continue
                elif(ele == 0):
                    makeRCZero(matrix,r,c)
        print(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ele = matrix[r][c]
                if(self.isFlagged(ele)):
                    matrix[r][c] = 0
        
    def isFlagged(self,ele):
        if(ele in ['r','c','r-c']):
            return True
        return False
        
        
                
        
        
# @lc code=end


        