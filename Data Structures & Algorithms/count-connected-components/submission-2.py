class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return
            
            if size[u] > size[v]:
                parent[root_v] = root_u
                size[root_v] += size[root_u]
            else:
                parent[root_u] = root_v
                size[root_u] += size[root_v]

            components -= 1
        
        for u, v in edges:
            union(u, v)
        
        return components
            

