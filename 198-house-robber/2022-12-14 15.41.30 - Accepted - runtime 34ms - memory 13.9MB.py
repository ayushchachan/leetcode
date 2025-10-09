class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            # db[index] = max(nums)
            return max(nums)
        db = {}

        def money(index):
            if index in db:
                return db[index]
            
            if index == 0:
                db[index] = nums[index]
                return nums[index]
            if index == 1:
                db[index] = max(nums[0:2])
                return max(nums[0:2])
            
            temp_max = max( money(index-2) + nums[index], money(index-1) )
            db[index] = temp_max
            return temp_max

        return money(len(nums)-1)