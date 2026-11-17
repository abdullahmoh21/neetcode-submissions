class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for i in range(n)]
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        visited = set()
        def dfs(i):
            visited.add(i)

            if not nodes[i]:
                return 
            
            for n in nodes[i]:
                if n not in visited:
                    dfs(n)
        
        count = 0
        for n, _ in enumerate(nodes):
            if n not in visited:
                dfs(n)
                count += 1
        
        return count