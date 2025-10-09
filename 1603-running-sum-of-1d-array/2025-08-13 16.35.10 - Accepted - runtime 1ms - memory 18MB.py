class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        lastVal = 0
        for i in nums:
            lastVal = lastVal + i
            answer.append(lastVal)
        return answer
        
        