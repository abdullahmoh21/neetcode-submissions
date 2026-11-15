class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)



        visited = set([0])
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            children = adj[node]
            visited.add(node)
            for c in children:
                if c not in visited:
                    q.append(c)
        
        return len(visited) == n


            
            

