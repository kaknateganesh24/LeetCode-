class Solution(object):
    def orangesRotting(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        fresh_count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1
        minutes=0
        directions=((0,-1),(0,1),(-1,0),(1,0))
        while queue and fresh_count>0:
            minutes +=1
            for _ in range(len(queue)):
                row,col=queue.popleft()
                for dr,dc in directions:
                    new_row= row+dr
                    new_col=col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1:
                        grid[new_row][new_col]=2
                        fresh_count-=1
                        queue.append((new_row,new_col))
        if fresh_count>0:
            return -1
        return minutes