
# color = 0 for white   ==> not visited
# color = 1 for gray    ==> being explored
# color = 2 for black   ==> completed

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        Adj = {}
        color = {}
        for i in range(numCourses):
            Adj[i] = []
            color[i] = 0
        for v, u in prerequisites:
            Adj[u].append(v)
        # print("Adj =", Adj)
        # print("color =", color)
        return full_dfs(Adj, color)
            
def dfs_visit(s, Adj, color):
    color[s] = 1
    # print("dfs_visit called with s =", s)
    # print("Adj =", Adj)
    # print("color =", color)

    for v in Adj[s]:
        if color[v] == 0:       ## i.e. not visited yet
            is_acyclic = dfs_visit(v, Adj, color)
            if not is_acyclic:
                return False
        elif color[v] == 1:
            # print("dfs_visit exit with cycle s =", s)
            return False
    color[s] = 2
    # print("dfs_visit exit without cycle s =", s)
    return True


def full_dfs(Adj, color = None):
    if color is None:
        color = {}
        for u in Adj:
            color[u] = 0        ## initially all vertices will be white colored i.e. not visited yet
    for u in Adj:
        if color[u] == 0:
            is_acyclic = dfs_visit(u, Adj, color)
            if not is_acyclic:
                return False
    return True

