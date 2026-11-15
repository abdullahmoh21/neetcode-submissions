class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set([0])
        q = deque([0])
        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)

        
        return len(visited) == n


            
            

