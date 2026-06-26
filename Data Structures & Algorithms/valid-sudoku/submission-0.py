class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        rowHash = {i: set() for i in range(ROWS)}
        colHash = {i: set() for i in range(COLS)}
        boxHash = {i: set() for i in range(int((ROWS * COLS) / 9))}
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])
                if num > 9 or num < 1:
                    return False
                if num in rowHash[row]:
                    return False
                if num in colHash[col]:
                    return False
                box = (row // 3) * 3 + (col // 3)
                if num in boxHash[box]:
                    return False
                rowHash[row].add(num)
                colHash[col].add(num)
                boxHash[box].add(num)
        return True