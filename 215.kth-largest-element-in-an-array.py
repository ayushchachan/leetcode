#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-u for u in nums]
        heapq.heapify(max_heap)

        for i in range(k):
            x = heapq.heappop(max_heap)
        return -1 * x


# @lc code=end
