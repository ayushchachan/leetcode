#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        k = N % groupSize

        if k != 0:
            return False

        heapq.heapify(hand)

        for i in range(k):
            buffer = []
            buffer.append(heapq.heappop(hand))
            for j in range(groupSize - 1):
                x = heapq.heappop(hand)
                if x - buffer[-1] > 1:
                    return False
                buffer.append(x)
        return True


# @lc code=end
