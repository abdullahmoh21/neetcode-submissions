class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(len(edges))]
        size = [1 for _ in range(len(edges))]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        cycle = None
        def union(u, v):
            nonlocal cycle
            root_u = find(u)
            root_v = find(v)

            # candidate edge since both nodes are already in same component
            if root_u == root_v:
                cycle = [u+1, v+1]
                return
            
            if size[root_u] > size[root_v]:
                parents[root_v] = root_u
                size[root_u] += size[root_v]
            else:
                parents[root_u] = root_v
                size[root_v] += size[root_u]
        
        for u, v in edges:
            union(u-1, v-1)
        
        return cycle


        





        # nodes = [[] for _ in range(len(edges) + 1)]
        # for u, v in edges:
        #     nodes[u].append(v)
        #     nodes[v].append(u)

        # visited = set()
        # cycle = None
        # def dfs(i):    
        #     print(f"At node {i}")        
        #     visited.add(i)

        #     for n in nodes[i]:
        #         print(f"Thinking of visiting child: {n}")
        #         if n in visited:
        #             cycle = [i, n]
        #             continue
        #         dfs(n)

        # dfs(1)
        # return cycle
        
