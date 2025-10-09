class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = 0
        prev = None
        for i in range(1,len(nums)):
            curr = 1 if nums[i] - nums[i-1] > 0 else (-1 if nums[i] - nums[i-1] < 0 else 0)
            if(prev == None and curr != 0):
                prev = curr
                N += 1
            else:
                if(curr != prev and curr != 0):
                    prev = curr
                    N += 1
        return N + 1