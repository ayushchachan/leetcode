import heapq


class Node:
    def __init__(self, k, f) -> None:
        self.k = k
        self.f = f

    def __lt__(self, b):
        if self.f == b.f:
            return self.k < b.k
        
        return self.f < b.f


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key in d.keys():
            heapq.heappush(h, Node(key, d[key]))
            if(len(h) > k):
                heapq.heappop(h)

        return map(lambda ele : ele.k ,h)

