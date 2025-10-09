class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, n in enumerate(nums):
            if n in index:
                index[n].append(i)
            else:
                index[n] = [i]

        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in index:
                if n == n2:
                    if len(index[n]) > 1:
                        return index[n]
                    else:
                        continue

                index_n2 = index[n2]
                return (i, index_n2[0])


        
