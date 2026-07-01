class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        import heapq

        m, n  = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:

            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    
        max_heap = [(-dist[0][0], 0, 0)]
        visited = set() 

        visited.add((0, 0))
        while max_heap:
            
            safeness, x, y = heapq.heappop(max_heap)
            safeness = -safeness

            if (x, y) == (m - 1, n - 1):
                return safeness

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(max_heap, (-min(safeness, dist[nx][ny]), nx, ny))
        