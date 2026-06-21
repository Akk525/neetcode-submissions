class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0

        def dfs(r, c):
            if (r >= 0 and r < ROWS) and (c >= 0 and c < COLS) and grid[r][c] != "0":
                grid[r][c] = "0"
                dfs(r - 1, c)        
                dfs(r, c + 1)        
                dfs(r + 1, c)        
                dfs(r, c - 1)
                    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)
        return island_count