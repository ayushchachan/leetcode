#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreater = dict()
        nextGreater[nums2[-1]] = -1

        for i in range(len(nums2) - 2, -1, -1):
            if nums2[i + 1] > nums2[i]:
                nextGreater[nums2[i]] = nums2[i + 1]
            else:
                x = nextGreater[nums2[i + 1]]
                while x in nextGreater and x <= nums2[i]:
                    x = nextGreater[x]
                nextGreater[nums2[i]] = x

        answer = []

        for i in nums1:
            answer.append(nextGreater[i])
        return answer


# nums1 = [4, 1, 2, 0]
# nums2 = [3, 4, 2, 0, 1]

# S = Solution()
# print(S.nextGreaterElement(nums1, nums2))
# @lc code=end
