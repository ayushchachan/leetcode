class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)
        while end > start:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        return -1