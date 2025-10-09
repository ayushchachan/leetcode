#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque


class MyStack:

    def __init__(self):
        self.current = deque()
        self.residual = deque()

    def push(self, x: int) -> None:
        self.current.append(x)

    def pop(self) -> int:
        while len(self.current) != 1:
            self.residual.append(self.current.popleft())

        answer = self.current.pop()

        self.current, self.residual = self.residual, self.current
        return answer

    def top(self) -> int:
        return self.current[-1]

    def empty(self) -> bool:
        return len(self.current) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
