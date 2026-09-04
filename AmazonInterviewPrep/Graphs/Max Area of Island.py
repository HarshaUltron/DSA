from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        max_area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:

                    area = 0
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = 0  # mark visited

                    while queue:
                        r, c = queue.popleft()
                        area += 1

                        directions = [(1,0), (-1,0), (0,1), (0,-1)]

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < row and 
                                0 <= nc < col and 
                                grid[nr][nc] == 1):

                                grid[nr][nc] = 0
                                queue.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area