#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque
class RecentCounter:

    def __init__(self):
        self.Q = deque()
        

    def ping(self, t: int) -> int:
        while (len(self.Q) > 0 and self.Q[0] < t - 3000):
            self.Q.popleft()
        
        self.Q.append(t)
        return len(self.Q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

