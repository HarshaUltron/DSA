from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # step 1: collect rotten + count fresh
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # no fresh oranges
        if fresh == 0:
            return 0

        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS
        while queue:
            size = len(queue)
            infected = False

            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                        infected = True

            if infected:
                time += 1

        return time if fresh == 0 else -1