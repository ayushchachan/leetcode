import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        Q = [-i for i in piles]
        heapq.heapify(Q)

        for i in range(k):
            x = abs(heapq.heappop(Q))
            y = x - x // 2
            heapq.heappush(Q, -y)

        return -sum(Q)