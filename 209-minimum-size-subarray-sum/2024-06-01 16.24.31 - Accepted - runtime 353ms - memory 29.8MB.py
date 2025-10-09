class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #[1,3,2,2,4,3]
        sumCurr = nums[0]
        res = len(nums)
        if(target > sum(nums)):
            return 0
        i = 0;j = 0
        while(j < len(nums) and i < len(nums)):
            if(sumCurr >= target):
                res = min(res,j - i + 1)
                sumCurr = sumCurr - nums[i]
                i += 1
                if(i >= len(nums)):
                    return res
                
            else:
                j += 1
                if(j >= len(nums)):
                    return res
                sumCurr = sumCurr + nums[j]
            print(sumCurr,i,j,res)
        return res
            


        