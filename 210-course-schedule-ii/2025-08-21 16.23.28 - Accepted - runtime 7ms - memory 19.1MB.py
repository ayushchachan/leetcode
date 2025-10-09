# @lc app=leetcode id=207 lang=python3
# [207] Course Schedule
# @lc code=start


def makeGraph(prereq, n):
    G = {}
    for i in range(n):
        G[i] = []
    for ele in prereq:
        fro, to = ele
        G[fro].append(to)
    return G


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
    # print("dfs_visit exit without cycle s =", s)
    order.append(s)
    return True


def full_dfs(Adj):
    color = {}
    for u in Adj:
        color[u] = 0        ## initially all vertices will be white colored i.e. not visited yet
    
    order = []      ## topological ordering
    
    for u in Adj:
        if color[u] == 0:
            is_acyclic = dfs_visit(u, Adj, color, order)
            if not is_acyclic:
                return (False, [])
    return (True, order)



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       adj = makeGraph(prerequisites, numCourses)
       
       is_acyclic, order = full_dfs(adj)
    #    order.reverse()
       return order
       

