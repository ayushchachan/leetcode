class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        d = {}
        for i in range(len(nums) - 2):
            if nums[i] in d:
                continue
            twoSum = self.twoSum(nums, i + 1, -nums[i])
            if len(twoSum) == 0:
                continue
            for ele in twoSum:
                res.append([nums[i],ele[0],ele[1]])
            d[nums[i]] = True

        return res

    def twoSum(self, nums, i, target):
        l = i
        h = len(nums) - 1
        res = []
        while l < h:
            if nums[l] + nums[h] == target:
                res.append([nums[l], nums[h]])
                templ = nums[l]
                tempH = nums[h]
                while l < h and nums[l] == templ:
                    l += 1
                while l < h and nums[h] == tempH:
                    h -= 1
            elif nums[l] + nums[h] < target:
                l += 1
            else:
                h -= 1
        return res

