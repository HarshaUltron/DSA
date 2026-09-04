from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1

                    # start BFS
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = "0"

                    while queue:
                        r, c = queue.popleft()

                        # 4 directions
                        directions = [(1,0), (-1,0), (0,1), (0,-1)]

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < rows and 
                                0 <= nc < cols and 
                                grid[nr][nc] == "1"):

                                queue.append((nr, nc))
                                grid[nr][nc] = "0"

        return count