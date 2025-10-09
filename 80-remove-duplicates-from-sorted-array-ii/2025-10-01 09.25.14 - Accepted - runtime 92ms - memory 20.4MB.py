class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        val = nums[0]

        f_o = 0             ## index of first occurence of val
        l_o = 0             ## index of last occurence of val

        nums[index] = val
        index += 1

        i = 1
        N = len(nums)
        while (i < N):
            while (i < N and nums[i] == val):
                l_o = i
                i += 1

            if (l_o > f_o):
                nums[index] = val
                index += 1
            if (i < N):
                val = nums[i]
                f_o = i
                nums[index] = val
                index += 1
                i += 1
        return index