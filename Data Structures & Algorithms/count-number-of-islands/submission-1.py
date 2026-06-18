class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            if (r >= 0 and r < rows) and (c >= 0 and c < cols) and (grid[r][c] != "0"):
                grid[r][c] = "0"
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r, c - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    island_count += 1
        
        return island_count