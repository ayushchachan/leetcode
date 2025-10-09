class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        Adj = {}
        color = {}
        for i in range(numCourses):
            Adj[i] = []
            color[i] = 0
        for v, u in prerequisites:
            Adj[u].append(v)
        # print("Adj =", Adj)
        # print("color =", color)
        return list(full_dfs(Adj)[::-1])
            
def dfs_visit(s, Adj, color, order):
    color[s] = 1
    # print("dfs_visit called with s =", s)
    # print("Adj =", Adj)
    # print("color =", color)

    for v in Adj[s]:
        if color[v] == 0:       ## i.e. not visited yet
            is_acyclic = dfs_visit(v, Adj, color, order)
            if not is_acyclic:
                return False
        elif color[v] == 1:
            # print("dfs_visit exit with cycle s =", s)
            return False
    color[s] = 2
    order.append(s)
    # print("dfs_visit exit without cycle s =", s)
    return order


def full_dfs(Adj):
    
    color = {}
    for u in Adj:
        color[u] = 0        ## initially all vertices will be white colored i.e. not visited yet
    
    order = []
    for u in Adj:
        if color[u] == 0:
            is_acyclic = dfs_visit(u, Adj, color, order)
            if not is_acyclic:
                return []
    return order

S = Solution()
prerequisites = [[0,1]]
print(S.findOrder(2, prerequisites))