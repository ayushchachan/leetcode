from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        return len(bfs(rooms, 0)) == len(rooms)


def bfs(adj, s):
    visited = {}
    
    Q = deque()
    Q.append(s)
    
    while len(Q) != 0:
        u = Q.popleft()
        visited[u] = True
        
        for v in adj[u]:
            if v not in visited:
                Q.append(v)
    return visited
        