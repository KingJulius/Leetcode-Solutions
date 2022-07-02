class Solution:  
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def solve(r, c, i):
            if i == len(word):
                return True
            if (r<0 or c<0 or 
                r>=ROWS or c>=COLS or
                word[i] != board[r][c] or
               (r, c) in path):
                return False
            path.add((r, c))
            res = (solve(r+1,c,i+1) or
                   solve(r-1,c,i+1) or
                   solve(r,c+1,i+1) or
                   solve(r,c-1,i+1))
            path.remove((r, c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if solve(i, j, 0):
                    return True
        return False