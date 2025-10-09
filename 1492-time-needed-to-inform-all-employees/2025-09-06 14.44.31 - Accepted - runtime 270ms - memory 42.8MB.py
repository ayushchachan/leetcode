class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        adj = []
        visiting_time = []
        
        for i in range(n):
            adj.append([])
            visiting_time.append(-1)
        for i in range(n):
            p_i = manager[i]                ## p_i is parent[i]
            if p_i == -1:
                continue
            adj[p_i].append(i)
        
        
        ## Now graph is ready
        # print("adj = \n", adj)
        global_time = 0
        from collections import deque
        Q = deque()
        Q.append(headID)
        visiting_time[headID] = 0
        
        while len(Q) != 0:
            u = Q.popleft()
            time_u = informTime[u]
            for v in adj[u]:
                if visiting_time[v] == -1:          ## i.e. not visited before
                    Q.append(v)
                    visiting_time[v] = visiting_time[u] + time_u
                    global_time = max(global_time, visiting_time[v])
        return global_time
            
# n = 7
# headID = 6
# manager = [1,2,3,4,5,6,-1]
# informTime = [0,6,5,4,3,2,1]        

# S = Solution()
# x = S.numOfMinutes(n, headID, manager, informTime)
# print(x)