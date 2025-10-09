import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        todo = []
        time_now = 0

        for i, task in enumerate(tasks):
            todo.append((i, task[0], task[1]))

        todo = sorted(todo, key=lambda x: x[1], reverse=True)

        queue = []
        order = []

        while todo or queue:

            while todo and time_now >= todo[-1][1]:
                i, et, pt = todo.pop()
                heapq.heappush(queue, (pt, i))

            if not queue:
                if todo:
                    time_now = todo[-1][1]
            else:
                time, index = heapq.heappop(queue)
                order.append(index)
                time_now += time

        return order
