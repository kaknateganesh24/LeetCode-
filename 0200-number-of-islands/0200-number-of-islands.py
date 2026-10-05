class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col):
            visited[row][col] = True

            # Down
            new_row = row + 1
            new_col = col
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == "1" and
                not visited[new_row][new_col]):
                dfs(new_row, new_col)

            # Up
            new_row = row - 1
            new_col = col
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == "1" and
                not visited[new_row][new_col]):
                dfs(new_row, new_col)

            # Right
            new_row = row
            new_col = col + 1
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == "1" and
                not visited[new_row][new_col]):
                dfs(new_row, new_col)

            # Left
            new_row = row
            new_col = col - 1
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == "1" and
                not visited[new_row][new_col]):
                dfs(new_row, new_col)

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row, col)
                    count += 1

        return count