class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1 for _ in range(n)]
        components = n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])    # flatten
            return parents[x]
        
        def union(u, v):
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return
            
            if size[root_u] > size[root_v]:    
                parents[root_v] = root_u
                size[root_v] += root_u
            else:
                parents[root_u] = root_v
                size[root_u] += root_v

            components -= 1

        for u, v in edges:
            union(u, v)
        
        return components




