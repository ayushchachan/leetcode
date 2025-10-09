

def makeGraph(prereq, n):
    g = {}
    for i in range(n):
        g[i] = set()
    
    for u, v in prereq:
        g[u].add(v)
    
    return g

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = makeGraph(prerequisites, numCourses)
        return dfs(adj)

def dfs_visit(adj, s, color):
    # print("dfs_visit called with =", s)
    # print("color = ", color)
    color[s] = 1            ## gray
    
    for u in adj[s]:
        if color[u] == 0:
            has_cycle = dfs_visit(adj, u, color)
            if has_cycle:
                return True            
        elif color[u] == 1:
            return True
    
    color[s] = 2            ## black
    return False
        
    
        

def dfs(adj):
    n = len(adj)
    color = [0] * n                 ## 0 = white, 1 = gray, 2 = black
                                    ## initially all white
    for u in adj:
        if color[u] == 0:
            
            has_cycle = dfs_visit(adj, u, color)
            
            if has_cycle:
                return False
    return True
            
    
S = Solution()

numCourses = 2
prereq = [[1,0],[0,1]]        

# print(S.canFinish(numCourses, prereq))
        

