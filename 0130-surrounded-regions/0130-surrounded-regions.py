class Solution(object):
    def solve(self, board):
       rows=len(board)
       cols=len(board[0])
       visited=[[False]*cols for _ in range(rows)]
       directions=((-1,0),(1,0),(0,-1),(0,1))
       def dfs(r,c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"  or
                visited[r][c]):
                return
            visited[r][c]=True
            for dr,dc in directions:
                new_row=r+dr
                new_col=c+dc
                dfs(new_row,new_col)
       for r in range(rows):
        for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    dfs(r, c)

       for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and not visited[r][c]:
                board[r][c] = "X"