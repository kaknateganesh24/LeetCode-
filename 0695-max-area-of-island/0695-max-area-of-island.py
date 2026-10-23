class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited[r][c] == True:
                return 0

            visited[r][c] = True
            area = 1

            for dr, dc in direction:
                new_r = dr + r
                new_c = dc + c
                area = area + dfs(new_r, new_c)

            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == False:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea