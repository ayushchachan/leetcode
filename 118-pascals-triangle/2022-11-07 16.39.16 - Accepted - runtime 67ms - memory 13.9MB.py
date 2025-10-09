class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(2, numRows + 1):
            temp = [1]
            recent = result[-1]
            
            for j in range(len(recent) - 1):
                temp.append(recent[j] + recent[j + 1])
            temp.append(1)
            result.append(temp)
        return result
        