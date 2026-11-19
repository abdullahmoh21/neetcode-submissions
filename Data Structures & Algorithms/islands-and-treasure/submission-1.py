class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j, 0))
        while q:
            i, j, distance = q.popleft()

            if grid[i][j] == INF:
                grid[i][j] = distance

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = i + dr, j + dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                
                if (nr, nc) in visited or grid[nr][nc] != INF:
                    continue
                
                visited.add((nr, nc))
                q.append((nr, nc, distance + 1))
        

                
                

            

