class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(r, c, visited):
            visited.add((r, c))

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS) and (nc >= 0 and nc < COLS) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    bfs(nr, nc, visited)
        
        for row in range(ROWS):
            bfs(row, 0, pacific)
            bfs(row, COLS - 1, atlantic)

        for col in range(COLS):
            bfs(0, col, pacific)
            bfs(ROWS - 1, col, atlantic)
        
        return list(pacific & atlantic)