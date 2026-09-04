from typing import List
from collections import deque

class Solution:
    def BFS(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            
            # Directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                row, col = queue.popleft()
                
                # Explore all 4 neighbors
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check bounds and if it's land ('1') and not visited
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == "1" and 
                        (new_row, new_col) not in visited):
                        
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
        
        # Find all islands
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        
        return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

df = Solution()
result = df.BFS(grid)
print(f"Number of islands: {result}")