class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        safe_node_list = set()
        full_dfs(graph, safe_node_list)
        return sorted(safe_node_list)
    
## returns True if u is safe node else False
def dfs_visit(adj, u, color, safe_node_list):
    # print("--------------------------------")
    # print("dfs_visit called on", u)
    # print("safe_node_list =", safe_node_list)
    color[u] = 1                ## gray
    
    if not adj[u]:
        safe_node_list.add(u)
        color[u] = 2                ## black
        return True
    
    is_u_safe_node = True    
    for v in adj[u]:
        
        if color[v] == 0:
            is_v_safe_node = dfs_visit(adj, v, color, safe_node_list)
            if not is_v_safe_node:
                is_u_safe_node = False
        
        elif color[v] == 1:           ## gray
            ## then it's a back edge and hence cycle
            is_u_safe_node = False

        elif color[v] == 2 and v not in safe_node_list:           ## gray
            ## then it's a cycle
            is_u_safe_node = False
    
    
    color[u] = 2                ## black
    if is_u_safe_node:
        safe_node_list.add(u)
        
    # print("dfs_visit exit called on", u)
    # print("safe_node_list =", safe_node_list)
    # print("--------xxx--------xxx--------xxx--------")
    return is_u_safe_node
        
    
    
    

def full_dfs(adj, safe_node_list):
    N = len(adj)
    color = [0] * N
    
    
    for u in range(N):
        if color[u] == 0:
            is_u_safe_node = dfs_visit(adj, u, color, safe_node_list)
    
    
        
        
        
        
            
S = Solution()

g = [[0],[2,3,4],[3,4],[0,4],[]]

# print(S.eventualSafeNodes(g))
