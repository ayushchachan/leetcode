
import heapq


class MedianFinder:
    def __init__(self):
        self.maxHeap = []  ## Left
        self.minHeap = []  ## Right

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -num)
            return
        median = self.findMedian()
        if len(self.maxHeap) == len(self.minHeap):
            if num <= median:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

        elif len(self.maxHeap) < len(self.minHeap):
            if num <= median:
                heapq.heappush(self.maxHeap, -num)
            else:
                ele = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -ele)

        else:
            if num >= median:
                heapq.heappush(self.minHeap, num)
            else:
                ele = heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, -ele)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()