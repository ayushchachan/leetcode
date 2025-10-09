class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        max_sum = -float('inf')

        for i in range(len(nums)):
            cur_sum += nums[i]

            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0


        return max_sum
        
