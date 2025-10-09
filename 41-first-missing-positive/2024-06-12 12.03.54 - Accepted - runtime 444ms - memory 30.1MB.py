
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def makeRightPosition(i):
            while(True):
                if nums[i] == None or nums[i] == i + 1 or nums[i] > len(nums) or nums[i] < 1 :
                        return
                if(nums[i] != i + 1):
                    if(nums[nums[i] - 1] == nums[i]):
                        nums[i] = None
                        return
                    nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
        
        i = 0
        for i in range(len(nums)):
            makeRightPosition(i)
        
        mis = 1
        for i in range(len(nums)):
            if(nums[i] == None or nums[i] != mis):
                return mis
            mis += 1
        return mis
                    
        