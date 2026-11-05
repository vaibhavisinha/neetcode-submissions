class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        components = 0
        visited = [False] * n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)

        def bfs(node):
            q = [node]
            visited[node]=True
            while q:
                curr = q.pop(0)
                # print(curr)
                for nei in graph[curr]:
                    if visited[nei]: continue
                    visited[nei]=True
                    q.append(nei)
        for i in range(n):
            if visited[i]: continue
            components += 1
            bfs(i)
        return components