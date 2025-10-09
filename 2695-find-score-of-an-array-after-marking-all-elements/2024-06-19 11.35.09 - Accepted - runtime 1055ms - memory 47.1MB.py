#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
class Solution:
    class MyObj:
        def __init__(self,val,i) -> None:
            self.flag = False
            self.val = val
            self.index = i
        def __lt__(self,b):
            return self.val < b.val

    def findScore(self, nums: List[int]) -> int:
        def sortFunc(e):
            return e.val
        d = {}
        for i in range(len(nums)):
            nums[i] = self.MyObj(nums[i],i)
            d[i] = nums[i]
        
        nums.sort(key = sortFunc)
        s = 0
        for ele in nums:
            if(ele.flag):
                continue
            i = ele.index
            d[i].flag = True
            s += ele.val
            if(i - 1 >= 0):
                d[i-1].flag = True
            if(i + 1 < len(nums)):
                d[i+1].flag = True
        return s
        
# @lc code=end