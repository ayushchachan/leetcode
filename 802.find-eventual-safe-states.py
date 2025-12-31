#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#


# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        return full_dfs(graph)


def dfs_visit(adj, s, color, order):

    color[s] = 1
    for v in adj[s]:
        if color[v] == 0:
            is_acyclic = dfs_visit(adj, v, color, order)
            if not is_acyclic:
                return False
        elif color[v] == 1:
            return False
    color[s] = 2
    return True


def full_dfs(Adj):
    color = dict()
    order = []
    for u in range(len(Adj)):
        color[u] = 0

    for u in range(len(Adj)):
        is_acyclic = dfs_visit(Adj, u, color, order)
        if not is_acyclic:
            return False
        return order


# @lc code=end
