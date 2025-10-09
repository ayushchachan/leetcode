class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        N = len(nums)
        index = 0

        for i in range(N):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
