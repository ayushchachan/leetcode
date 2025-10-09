from heapq import heapify, heappush, heappop
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        h = [(num, i) for i,num in enumerate(nums)]
        heapify(h)
        res = 0
        while h:
            num, i = heappop(h)
            if i not in visited:
                res += num
                if i-1>=0:
                    visited.add(i-1)
                if i+1<n:
                    visited.add(i+1)
                visited.add(i)
        return res