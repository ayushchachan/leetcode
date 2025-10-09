
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def makeRightPosition(i):
            while(True):
                if(nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]):
                    nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
                else:
                    return
        
        i = 0
        for i in range(len(nums)):
            makeRightPosition(i)
        
        mis = 1
        for i in range(len(nums)):
            if(nums[i] == None or nums[i] != mis):
                return mis
            mis += 1
        return mis
                    
        