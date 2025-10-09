class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxCount = 0
        currCount = 0
        for i in range(len(nums)):
            if(i == 0):
                currCount += 1
            else:
                if(nums[i] == nums[i-1]):
                    continue
                elif(nums[i] == nums[i-1] + 1):
                    currCount += 1
                else:
                    currCount = 1
            maxCount = max(maxCount,currCount)
        return maxCount

        