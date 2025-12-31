#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = dict()
        color = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            adj[i] = []

        for v, u in prerequisites:
            adj[u].append(v)

        order = []

        def dfs_visit(adj, s):
            nonlocal order

            color[s] = 1  ## gray color

            for v in adj[s]:
                if color[v] == 0:
                    is_acyclic = dfs_visit(adj, v)

                    if not is_acyclic:
                        return False
                elif color[v] == 1:
                    return False

            color[s] = 2
            order.append(s)
            return True

        for u in range(numCourses):
            if color[u] == 0:
                is_acyclic = dfs_visit(adj, u)
                if not is_acyclic:
                    return []

        order.reverse()
        return order


# @lc code=end
