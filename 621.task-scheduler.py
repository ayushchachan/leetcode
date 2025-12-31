#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter
import heapq
import string


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count_map = Counter(tasks)
        # print("counter =", count_map)
        pq = [(0, -count, word) for word, count in count_map.items()]
        heapq.heapify(pq)

        cycle = 0

        while len(pq) > 0:

            available_time, count, label = pq[0]

            if cycle >= available_time:
                count += 1
                if count < 0:
                    heapq.heapreplace(pq, (available_time + n + 1, count, label))
                else:
                    heapq.heappop(pq)
            cycle += 1

        # print("order =", order)
        return cycle


# tasks = ["A", "A", "A", "B", "B", "B"]
# S = Solution()
# S.leastInterval(tasks, 2)
# @lc code=end
