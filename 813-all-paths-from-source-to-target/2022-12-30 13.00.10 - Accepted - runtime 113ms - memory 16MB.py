class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        self.Adj = graph
        n = len(graph)


        self.all_paths = {}      ## all_paths[u] will contain all paths from u to n - 1
        self.all_paths[n - 1] = [[n - 1]]

        self.find_all_paths(0)
        return self.all_paths[0]

    def find_all_paths(self, u):
        if u in self.all_paths:
            return self.all_paths[u]

        paths_from_u = []
        for v in self.Adj[u]:
            if v in self.all_paths:       ## all paths available from v to n-1
                for l in self.all_paths[v]:
                    paths_from_u.append([u] + l)
            else:
                self.find_all_paths(v)
                for l in self.all_paths[v]:
                    paths_from_u.append([u] + l)
        self.all_paths[u] = paths_from_u
